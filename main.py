import streamlit as st
import streamlit_3d as sd


if(st.session_state.get("coord") is not None):
        coords=st.session_state["coord"] 
else:
    coords=[]
    st.session_state["coord"] = coords
st.markdown('''
    <style>
    .main .block-container{
        max-width: unset;
        padding-left: 5em;
        padding-right: 5em;
        padding-top: 1.5em;
        padding-bottom: 1em;
        }
    </style>
''', unsafe_allow_html=True)

st.write("## Streamlit 3D Annotations | DblClick to Annotate")
md=st.selectbox("3D Model:",["https://alteirac.com/models/helmet/scene.gltf","https://alteirac.com/models/engine/scene.gltf","https://alteirac.com/models/turbine/scene.gltf","https://alteirac.com/models/projector/scene.gltf","https://alteirac.com/models/car/scene.gltf","https://alteirac.com/models/captain/scene.gltf","https://alteirac.com/models/moto/scene.gltf"])
value = sd.streamlit_3d(model=md)
if value is not None:
    coords.append(value)
st.table(coords)