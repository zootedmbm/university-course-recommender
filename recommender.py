import pandas as pd

# Load the courses dataset
courses = pd.read_csv('courses.csv')

# Sample student profile (you can modify these values or input them dynamically)
student_grades = {'Data Structures and Algorithms': 'B', 'Web Development': 'A'}
student_interests = ['Data Science', 'Machine Learning']

# Function to recommend courses
def recommend_courses(student_grades, student_interests):
    recommended_courses = []
    
    for index, row in courses.iterrows():
        # Check if student's interests match course tags
        if any(interest in student_interests for interest in row['interest_tags'].split(',')):
            # Score based on student's performance in similar courses
            score = 0
            for course, grade in student_grades.items():
                if course in row['course_name'] and grade in ['A', 'B']:  # Check if the student has done well in similar courses
                    score += 1
            if score > 0:
                recommended_courses.append(row['course_name'])
    
    return recommended_courses

# Run the recommendation system
recommended = recommend_courses(student_grades, student_interests)
print(f"Recommended Courses: {recommended}")
