#1 python3 -m venv venv
#2 cd venv
#3 Scripts\activate.bat
#4 cd..
#5 pip install -r requirements.txt
#6 streamlit run src/app.py

# pip install streamlit
# pip freeze | findstr streamlit >> requirements.txt

# pip install streamlit-extras 
# pip freeze | findstr streamlit-extras >> requirements.txt

import streamlit as st
from streamlit_extras.let_it_rain import rain
import base64

def example():
    rain(
        emoji="🌮",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true" allow="autoplay" style="">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


# st.write("# Auto-playing Audio!")

# st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
st.markdown("![Alt Text](https://media.tenor.com/RQKAyM7ZHA0AAAAM/banana-dance.gif)")

autoplay_audio("local_audio.mp3")


example()
