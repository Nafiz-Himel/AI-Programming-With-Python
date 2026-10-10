import streamlit as st

st.title("Input your files",anchor = False)
st.divider()

#from strorage
st.image("Images/WhatsApp Image 2026-10-09 at 7.49.35 PM (1).jpeg")
#from url
st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb")

st.divider()
images = st.file_uploader("Enter ur image: (at max 2)",
                  type=['jpg','png','jpeg'],
                  accept_multiple_files = True,
                  )

print(type(images))


if images:
    if (len(images) > 2):
        st.warining("U uploaded more than 2 imges..!")
    cols = st.columns(len(images))

    for i,per_image in enumerate(images):
        with cols[i]:
            st.image(per_image)



# audio_vedio
#from directory
st.audio("Audio/welcome.mp3") #audio nei
st.divider()

audios = st.file_uploader("Upload ur audio: ",
                  type=['mp3','ogg','flac'],
                  )
if audios:
    st.audio(audios)
print(type(audios))

