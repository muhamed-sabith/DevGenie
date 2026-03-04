import streamlit as st
import ollama

# Page config
st.set_page_config(page_title="DevGenie - AI Academic Assistant", layout="wide")

# Title
st.title("🚀 DevGenie - AI Academic Assistant")
st.markdown("Generate structured academic project ideas using a Local LLM (Mistral)")

# Sidebar Feature Selection
feature = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Project Idea Generator",
        "Viva Questions Generator"
    ]
)

col1, col2, col3 = st.columns(3)

with col1:
    domain = st.selectbox(
        "Select Domain",
        [
            "Data Science",
            "Machine Learning",
            "Web Development",
            "Cyber Security",
            "MERN Stack",
            "Android Development",
            "Cloud Computing",
            "Artificial Intelligence"
        ]
    )

with col2:
    level = st.selectbox(
        "Skill Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

with col3:
    duration = st.selectbox(
        "Project Duration",
        ["1 Week", "2 Weeks", "1 Month"]
    )
# Generate Button
if st.button("Generate"):

    if feature == "Project Idea Generator":
        prompt = f"""
        Generate a structured academic project idea in {domain}.
        Skill level: {level}
        Duration: {duration}

        Provide:
        1. Project Title
        2. Problem Statement
        3. Tech Stack
        4. Dataset Suggestion
        5. Step-by-step Implementation Plan
        """

    elif feature == "Resume Description Generator":
        prompt = f"""
        Write a professional resume project description 
        for a {level} level {domain} academic project.
        """

    elif feature == "Viva Questions Generator":
        prompt = f"""
        Generate 8 viva questions with answers 
        for a {domain} project suitable for {level} level.
        """

    # Spinner (Professional UX)
    with st.spinner("Generating using Local LLM..."):
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

    # Output Section
    st.subheader("📌 Generated Output")
    st.markdown(response['message']['content'])