import streamlit as st

#title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizes")
st.divider()

with st.sidebar:
    st.header("Controls")

    #Image
    images = st.file_uploader(
        "Upload the photos of your note",
        type=["jpg","jpeg",'png'],
        accept_multiple_files = True,
    )

    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            cols = st.columns(len(images))
            print(type(cols),type(images))

            st.subheader("Uploaded images")

            for i,img in enumerate(images):
                with cols[i]:
                    st.image(img)

    #difficulty
    selected_option = st.selectbox(
        "Enter the diffculty of your quiz",
        ("Easy","Medium","Hard"),
        index = None,
    )
    pressed = st.button("Click the button to initiate AI",type="primary")
st.markdown("""
    <style>
    /* Streamlit-এর toast কন্টেইনারকে টার্গেট করে পজিশন বদলানো */
    div.stToast {
        width: fit-content !important;
        min-width: unset !important;
        position: fixed;
        bottom: 20px;
        left: 20px;
        top: auto;
        right: auto;
    }
    </style>
""", unsafe_allow_html=True)

if pressed:
    if not images:
        # st.error("You must upload 1 image")
        st.toast(":red[You must upload 1 image]")
    if not selected_option:
        # st.error("You must select a difficulty")
        st.toast(":red[You must select a difficulty]")

    if images and selected_option:

        #Note
        with st.container(border=True):
            st.subheader("Your note")

            #the portion below will be replaced by API Call
            st.text("Note will be shwon here...!")

        #Audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")
        
            #the portion below will be replaced by API Call
            st.text("Audio transcript will be shwon here...!")

        #Quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
        
            #the portion below will be replaced by API Call
            st.text("Quiz will be shwon here...!")