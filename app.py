"""Wage Brush Economics — your brush size = your wage."""
import streamlit as st
from streamlit_drawable_canvas import st_canvas

from src.economics import brush_label, wage_to_brush
from src.presets import PRESETS

st.set_page_config(page_title="Wage Brush Economics", page_icon="🖌️")
st.title("🖌️ Wage Brush Economics")
st.caption("Income inequality you can paint. Brush size = hourly wage.")

with st.sidebar:
    st.header("💼 Pick a job")
    for p in PRESETS:
        if st.button(f"{p['job']} — ${p['wage']}/hr", key=p["job"]):
            st.session_state.wage = p["wage"]
    st.divider()

if "wage" not in st.session_state:
    st.session_state.wage = 15

wage = st.slider("Hourly wage ($/hr)", 7, 500, st.session_state.wage,
                 help="Min wage → hairline. CEO → roller.")
st.session_state.wage = wage
scale = st.radio("Brush scaling", ["linear", "sqrt"], horizontal=True,
                 help="linear = honest proportion. sqrt = area-corrected so CEOs can still draw.")
brush = wage_to_brush(wage, scale)

c1, c2, c3 = st.columns(3)
c1.metric("Wage", f"${wage}/hr")
c2.metric("Brush", f"{brush}px")
c3.metric("Class", brush_label(brush))

color = st.color_picker("Paint color", "#1f77b4")

canvas = st_canvas(
    fill_color="rgba(255,255,255,0)",
    stroke_width=brush,
    stroke_color=color,
    background_color="#fafafa",
    height=400,
    width=700,
    drawing_mode="freedraw",
    key="wage-brush",
)

st.info(
    f"At ${wage}/hr you paint with a **{brush}px** brush. "
    "Try $7 (hairline) vs $500 (roller) — draw the same house with both."
)
