import streamlit as st
import requests

st.title("🎬 Movie Recommendation System")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    if movie:
        url = f"http://127.0.0.1:8000/recommend/{movie}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "recommendations" in data:
                st.subheader("Recommended Movies")
                for m in data["recommendations"]:
                    st.write(m)
            else:
                st.error("Movie not found")