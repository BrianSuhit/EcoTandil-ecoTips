import streamlit as st

from advisor import EcoAdvisor
from catalogs import DROP_OFF_POINTS, WASTE_OPTIONS

st.title("EcoTandil - ecoTips 🌱")
st.write(
    "Generador de tips ambientales para estudiantes. Elegí un residuo y el "
    "Punto Limpio donde lo vas a llevar para recibir un consejo claro y fácil "
    "de seguir."
)

waste = st.selectbox("Elegí un residuo", options=WASTE_OPTIONS)
drop_off_point = st.selectbox("Elegí un Punto Limpio", options=DROP_OFF_POINTS)


@st.cache_resource
def get_advisor() -> EcoAdvisor:
    return EcoAdvisor()


if st.button("Generar tip"):
    with st.spinner("Generando un tip..."):
        tip, is_error = get_advisor().generate_tip(waste, drop_off_point)
    if is_error:
        st.error(tip)
    else:
        st.success(tip)
