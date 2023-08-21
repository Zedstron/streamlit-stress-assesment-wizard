import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def stress_test():
    st.title("Stress Assessment Wizard")
    st.write("Answer a few questions to assess your stress level.")

    # Initialize answers dictionary
    answers = {}

    # Question 1
    q1 = st.selectbox("How often do you feel anxious or nervous?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
    answers["q1"] = {"score": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}[q1], "text": q1}

    # Question 2
    q2 = st.selectbox("How well do you sleep?", ["Very well", "Moderately well", "Not well", "Not at all"])
    answers["q2"] = {"score": {"Very well": 0, "Moderately well": 1, "Not well": 2, "Not at all": 3}[q2], "text": q2}

    # Question 3
    q3 = st.selectbox("How often do you experience physical symptoms like headaches or muscle tension?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
    answers["q3"] = {"score": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}[q3], "text": q3}

    # Question 4
    q4 = st.selectbox("How often do you find it hard to relax?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
    answers["q4"] = {"score": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}[q4], "text": q4}

    # Question 5
    q5 = st.selectbox("How often do you feel overwhelmed?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
    answers["q5"] = {"score": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}[q5], "text": q5}

    # Question 6
    q6 = st.selectbox("How often do you feel irritable or angry?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
    answers["q6"] = {"score": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}[q6], "text": q6}

    # Question 7
    q7 = st.selectbox("How often do you have trouble concentrating?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
    answers["q7"] = {"score": {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Always": 4}[q7], "text": q7}

    # Calculate total stress score
    total_score = sum(answer["score"] for answer in answers.values())
    percentage = (total_score / 32) * 100
    
    st.progress(percentage, "Your Stress Status")

    # Store the assessed score
    store_assessment(total_score)

    # Display the score distribution graph
    display_score_distribution()

def store_assessment(score):
    # Load or create a DataFrame to store assessments
    try:
        assessments = pd.read_csv("assessments.csv")
    except FileNotFoundError:
        assessments = pd.DataFrame(columns=["Date", "Score"])

    # Add the new assessment
    new_row = {"Date": pd.Timestamp.now(), "Score": score}
    assessments = assessments.append(new_row, ignore_index=True)

    # Save the DataFrame
    assessments.to_csv("assessments.csv", index=False)

def display_score_distribution():
    try:
        assessments = pd.read_csv("assessments.csv")
        st.subheader("The average score rated by the audience till now")
        plt.figure(figsize=(10, 6))
        plt.hist(assessments["Score"], bins=[0, 10, 15, 20, 25, 30], edgecolor="black")
        plt.xlabel("Stress Score")
        plt.ylabel("Frequency")
        plt.title("Average Audience Stress Distribution")
        st.pyplot(plt)
    except FileNotFoundError:
        st.warning("No assessments have been made yet.")

if __name__ == "__main__":
    stress_test()
