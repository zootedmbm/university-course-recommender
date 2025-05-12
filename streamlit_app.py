import streamlit as st
import pandas as pd

# Load the courses dataset
courses = pd.read_csv('courses.csv')

# Streamlit app for user input
st.title("University Course Recommender")
st.write("Enter your previous course performance and interests:")

# Get student grades and interests
student_grades = {}
num_courses = st.number_input("How many courses have you taken?", 1, 10)
for i in range(num_courses):
    course_name = st.text_input(f"Enter Course {i+1} Name:")
    grade = st.selectbox(f"Grade for {course_name}: ", ["A", "B", "C", "D", "F"])
    student_grades[course_name] = grade

student_interests = st.text_input("Enter your interests (comma-separated):").split(',')

# Function to recommend courses (same as before)
def recommend_courses(student_grades, student_interests):
    recommended_courses = []
    for index, row in courses.iterrows():
        if any(interest in student_interests for interest in row['interest_tags'].split(',')):
            score = 0
            for course, grade in student_grades.items():
                if course in row['course_name'] and grade in ['A', 'B']:
                    score += 1
            if score > 0:
                recommended_courses.append(row['course_name'])
    return recommended_courses

# Display recommendations
recommended = recommend_courses(student_grades, student_interests)
st.write(f"Recommended Courses: {', '.join(recommended)}")
