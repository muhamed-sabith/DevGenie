import streamlit as st
import ollama

# Set page configuration
st.set_page_config(page_title="DevGenie - AI Academic Assistant")

# App Title
st.title("🚀 DevGenie - AI Academic Assistant")
st.write("Generate structured academic project ideas using Local LLM (Mistral)")

# Sidebar Feature Selection
feature = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Project Idea Generator",
        "Resume Description Generator",
        "Viva Questions Generator"
    ]
)

# User Inputs
domain = st.selectbox(
    "Select Domain",
    ["Data Science", "Machine Learning", "Web Development", "Cyber Security"]
)

level = st.selectbox(
    "Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

duration = st.selectbox(
    "Project Duration",
    ["1 Week", "2 Weeks", "1 Month"]
)

# Generate Button
if st.button("Generate"):

    # Prompt Engineering
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

    # Call Local LLM
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    # Display Output
    st.subheader("Generated Output")
    st.write(response['message']['content'])