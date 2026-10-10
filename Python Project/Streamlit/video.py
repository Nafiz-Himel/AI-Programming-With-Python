import streamlit as st

st.title("Video in streamlit",anchor=False)
st.divider()

video_file = st.file_uploader("Enter ur audio: ",
                              type=['mp4','mkv'],
                              )

button = st.button("Click to upload")
if button:
    if video_file:
        st.video(video_file)
        st.success("Uploaded..!")
    else:
        st.error("U must upload a file")