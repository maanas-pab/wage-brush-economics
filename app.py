"""Wage Brush Economics — your brush size = your wage."""
import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas

from src.economics import brush_label, hours_to_earn, paint_multiplier, wage_to_brush
from src.house import house_template
from src.presets import PRESETS

st.set_page_config(page_title="Wage Brush Economics", page_icon="🖌️", layout="wide")
st.markdown(
    "<style>.stApp {max-width: 1100px; margin: auto;} canvas {border-radius: 12px;}</style>",
    unsafe_allow_html=True,
)
st.title("🖌️ Wage Brush Economics")
st.caption("Income inequality you can paint. Brush size = hourly wage.")

with st.sidebar:
    st.header("💼 Pick a job")
    for p in PRESETS:
        if st.button(f"{p['job']} — ${p['wage']}/hr", key=p["job"]):
            st.session_state.wage = p["wage"]
    st.divider()
    st.subheader("📊 US wages (2024)")
    try:
        df = pd.read_csv("data/wages_2024.csv")
        # NOTE: st.bar_chart pulls Altair, which is broken on
        # Streamlit Cloud's Python 3.14 runtime. dataframe is dependency-free.
        st.dataframe(
            df[["occupation", "hourly_median"]],
            hide_index=True,
            use_container_width=True,
        )
        st.caption("Source: BLS OES 2024, rounded. CEO capped at $500 for canvas.")
    except FileNotFoundError:
        st.caption("Wage dataset missing.")

if "wage" not in st.session_state:
    st.session_state.wage = 15

wage = st.slider("Hourly wage ($/hr)", 7, 500, int(st.session_state.wage),
                 help="Min wage → hairline. CEO → roller.")
st.session_state.wage = wage
scale = st.radio("Brush scaling", ["linear", "sqrt"], horizontal=True,
                 help="linear = honest proportion. sqrt = area-corrected so CEOs can still draw.")
brush = wage_to_brush(wage, scale)
color = st.color_picker("Paint color", "#1f77b4")
stroke_color = color + "ff" if color.startswith("#") and len(color) == 7 else color

c1, c2, c3 = st.columns(3)
c1.metric("Wage", f"${wage}/hr")
c2.metric("Brush", f"{brush}px")
c3.metric("Class", brush_label(brush))

with st.expander("💰 What does this wage mean? (labor value)", expanded=True):
    mult = paint_multiplier(wage)
    rent_hours = hours_to_earn(2000, wage)
    house_hours = hours_to_earn(450_000, wage)
    e1, e2, e3 = st.columns(3)
    e1.metric("Paint per stroke", f"{mult:.1f}×", "vs min-wage worker")
    e2.metric("Hours for $2k rent", f"{rent_hours:.1f}h")
    e3.metric("Hours for $450k house", f"{house_hours:,.0f}h")
    st.caption(
        "A CEO covers rent in 4 hours. A minimum-wage worker needs 276. "
        "Same house, different brushes — same economy, different lives."
    )

tab_paint, tab_compare = st.tabs(["🎨 Free paint", "⚖️ Same house challenge"])

with tab_paint:
    col_opts, col_clear = st.columns([3, 1])
    show_guide = col_opts.checkbox("Show house template to trace 🏠", value=True)
    if col_clear.button("🧹 Clear canvas"):
        st.rerun()
    bg = None
    try:
        bg = house_template() if show_guide else None
    except Exception:
        bg = None
    canvas = st_canvas(
        fill_color="rgba(255,255,255,0)",
        stroke_width=brush,
        stroke_color=stroke_color,
        background_color="#fafafa",
        background_image=bg,
        height=400,
        width=700,
        drawing_mode="freedraw",
        key="wage-brush",
    )
    st.info(
        f"At ${wage}/hr you paint with a **{brush}px** brush. "
        "Try $7 (hairline) vs $500 (roller) — draw the same house with both."
    )

with tab_compare:
    st.write("Draw the **same house** 🏠 with both brushes. Left = $7.25 minimum wage, right = $500 CEO.")
    left, right = st.columns(2)
    with left:
        st.markdown("**🧾 Minimum wage — 1px hairline**")
        st_canvas(
            fill_color="rgba(255,255,255,0)",
            stroke_width=wage_to_brush(7.25, scale),
            stroke_color=stroke_color,
            background_color="#fff",
            height=300,
            width=340,
            drawing_mode="freedraw",
            key="brush-min",
        )
    with right:
        st.markdown("**👑 CEO — giant roller**")
        st_canvas(
            fill_color="rgba(255,255,255,0)",
            stroke_width=wage_to_brush(500, scale),
            stroke_color=stroke_color,
            background_color="#fff",
            height=300,
            width=340,
            drawing_mode="freedraw",
            key="brush-ceo",
        )
    st.caption("Tip: on mobile the canvases stack — still the same challenge, just scroll.")

st.divider()
st.caption("Wage Brush Economics · paint inequality · BLS OES 2024 · MIT")
