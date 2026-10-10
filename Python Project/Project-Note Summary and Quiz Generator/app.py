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

    if selected_option:
        st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")
    else:
        st.error("You must select a difficulty")

    st.button("Click the button to initiate AI",type="primary")