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
        padding-left: 2em;
        padding-right: 2em;
        padding-top: 1.5em;
        padding-bottom: 1em;
        }
    </style>
''', unsafe_allow_html=True)

st.write("## Streamlit 3D Annotations | DblClick to Annotate")
md=st.selectbox("3D Model:",["https://alteirac.com/models/helmet/scene.gltf","https://alteirac.com/models/engine/scene.gltf","https://alteirac.com/models/turbine/scene.gltf","https://alteirac.com/models/projector/scene.gltf","https://alteirac.com/models/car/scene.gltf","https://alteirac.com/models/captain/scene.gltf","https://alteirac.com/models/moto/scene.gltf"])
value = sd.streamlit_3d(height=600,model=md,points=[{"description":"LEFT_LIGHT","data-position":{"x":0.4595949207254826,"y":0.40998085773554555,"z":0.33846317660071373},"data-normal":{"x":-0.18705895743345607,"y":-0.3420641705224677,"z":0.9208697246020658}}])
if value is not None:
    coords.append(value) 
st.table(coords)
with st.expander("Code"):
    st.code(body=f'''

    # pip install streamlit-3d
    import streamlit as st 
    import streamlit_3d as sd

    md=st.selectbox("3D Model:",["https://alteirac.com/models/helmet/scene.gltf",
                                 "https://alteirac.com/models/engine/scene.gltf"
                                 ])
    # if you want to load existing Annotations:                                
    value = sd.streamlit_3d(height=600,model=md,points=[{{"description":"LEFT_LIGHT",
                                            "data-position":{{"x":0.4595949207254826,"y":0.40998085773554555,"z":0.33846317660071373}},
                                            "data-normal":{{"x":-0.18705895743345607,"y":-0.3420641705224677,"z":0.9208697246020658}}}}
                                            ])
    # if you simply want to show the model:
    # value = sd.streamlit_3d(model=md,height=700)                                        
    st.write(value)''' ,language="python")