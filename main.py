import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        st.header("Post Length")
        selected_length = st.selectbox("Select post length", options=["short", "medium", "long"])
    with col2:
        st.header("Language")
        selected_language = st.selectbox("Select post language", options=["English", "Hinglish"])
    with col3:
        st.header("Tag")
        selected_tag = st.selectbox("Select post tag", options=fs.get_posts())
        
    if st.button("Generate Post"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)
        
if __name__ == "__main__":
    main()