"""Wage Brush Economics — your brush size = your wage."""
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Wage Brush Economics", page_icon="🖌️")
st.title("🖌️ Wage Brush Economics")
st.caption("Income inequality you can paint. Brush size = hourly wage.")

wage = st.slider("Hourly wage ($/hr)", 7, 500, 15, help="Min wage → hairline. CEO → roller.")
brush = int(1 + (wage - 7) / (500 - 7) * 59)  # 1px → 60px

c1, c2, c3 = st.columns(3)
c1.metric("Wage", f"${wage}/hr")
c2.metric("Brush", f"{brush}px")
c3.metric("Class", "Hairline" if brush < 8 else "Roller" if brush > 40 else "Brush")

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
