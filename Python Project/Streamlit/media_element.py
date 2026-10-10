import streamlit as st

st.title("Input your files",anchor = False)
st.divider()

images = st.file_uploader("Enter ur image: ",
                  type=['jpg','png','jpeg'],
                  accept_multiple_files = True,
                  )

print(type(images))


if images:
    cols = st.columns(len(images))

    for i,per_image in enumerate(images):
        with cols[i]:
            st.image(per_image)
