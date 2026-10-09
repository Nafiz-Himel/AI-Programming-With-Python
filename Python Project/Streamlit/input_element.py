import streamlit as st

st.title("Input your Information", anchor=False)
st.divider()

name = st.text_input("Enter your name:",placeholder="Type ur name....")
print(type(name))
st.write(f"Your name is: :green[{name}]")

st.divider()

age = st.number_input("Enter your age: ",value=None,placeholder="Type ur age....")
print(type(age))
st.write(f"Your age is: :green[{age}]")

password = st.text_input("Enter your password:", type="password",placeholder="Type ur pass....")
print(type(password))
st.write(f"Your password is: :green[{password}]")


pressed = st.button("Cclick the BUtton",type="primary")

if pressed:
    st.write(f":green[Your name is {name} and your age is {age} and password is :red[{password}]]")