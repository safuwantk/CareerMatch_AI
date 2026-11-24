import pandas as pd
import numpy as np
import random

print("CareerMatch AI Project Started")
columns = [
    'student_id',
    'age',
    'qualification',
    'math_marks',
    'computer_marks',
    'english_marks',
    'statistics_marks',
    'python_skill',
    'java_skill',
    'cpp_skill',
    'sql_skill',
    'html_skill',
    'css_skill',
    'javascript_skill',
    'machine_learning_skill',
    'communication_skill',
    'problem_solving',
    'creativity',
    'leadership',
    'interest',
    'career'
]

print(columns)
qualifications = [
    'BCA',
    'BSc Computer Science',
    'BTech Computer Science',
    'MCA',
    'MSc Computer Science',
    'Diploma in Computer Science'
]

print(qualifications)
interests = [
    'Data Science',
    'Data Analysis',
    'Artificial Intelligence',
    'Web Development',
    'Software Development',
    'Cyber Security',
    'Database Management',
    'Cloud Computing'
]

print(interests)
careers = [
    'Data Scientist',
    'Data Analyst',
    'AI Engineer',
    'Machine Learning Engineer',
    'Web Developer',
    'Software Developer',
    'Cyber Security Analyst',
    'Database Administrator'
]

print(careers)
student_id = "S00001"

print("Student ID:", student_id)
age = random.randint(18, 30)

print("Student Age:", age)
qualification = random.choice(qualifications)

print("Qualification:", qualification)
math_marks = random.randint(40, 100)

computer_marks = random.randint(40, 100)

english_marks = random.randint(40, 100)

statistics_marks = random.randint(40, 100)

print("Maths Marks:", math_marks)
print("Computer Marks:", computer_marks)
print("English Marks:", english_marks)
print("Statistics Marks:", statistics_marks)
# Programming Skills

python_skill = random.randint(0, 10)

java_skill = random.randint(0, 10)

cpp_skill = random.randint(0, 10)

sql_skill = random.randint(0, 10)


# Web Development Skills

html_skill = random.randint(0, 10)

css_skill = random.randint(0, 10)

javascript_skill = random.randint(0, 10)


# Machine Learning Skill

machine_learning_skill = random.randint(0, 10)


# Display Skills

print("Python Skill:", python_skill)
print("Java Skill:", java_skill)
print("C++ Skill:", cpp_skill)
print("SQL Skill:", sql_skill)

print("HTML Skill:", html_skill)
print("CSS Skill:", css_skill)
print("JavaScript Skill:", javascript_skill)

print("Machine Learning Skill:", machine_learning_skill)
# Professional Skills

communication_skill = random.randint(0, 10)

problem_solving = random.randint(0, 10)

creativity = random.randint(0, 10)

leadership = random.randint(0, 10)


# Display Professional Skills

print("Communication Skill:", communication_skill)

print("Problem Solving:", problem_solving)

print("Creativity:", creativity)

print("Leadership:", leadership)
# Student Interest

interest = random.choice([
    "Data Science",
    "Web Development",
    "Artificial Intelligence",
    "Cyber Security",
    "Software Development",
    "Business Analytics"
])
print("Student Interest:", interest)
# Career Recommendation Logic

if interest == "Data Science":

    if python_skill >= 5 and statistics_marks >= 60:
        career = "Data Scientist"
    else:
        career = "Data Analyst"


elif interest == "Web Development":

    if html_skill >= 5 and css_skill >= 5:
        career = "Web Developer"
    else:
        career = "Frontend Developer"


elif interest == "Artificial Intelligence":

    if machine_learning_skill >= 5 and python_skill >= 5:
        career = "AI Engineer"
    else:
        career = "Machine Learning Engineer"


elif interest == "Cyber Security":

    if problem_solving >= 6 and sql_skill >= 4:
        career = "Cyber Security Analyst"
    else:
        career = "Security Analyst"


elif interest == "Software Development":

    if python_skill >= 5 or java_skill >= 5:
        career = "Software Developer"
    else:
        career = "Junior Software Developer"


else:
    career = "Business Analyst"


print("Recommended Career:", career)
# Generate 100,000 Student Records

students = []

for i in range(100000):

    student = {}

    # Student Academic Details
    student['student_id'] = i + 1
    student['age'] = random.randint(18, 30)

    student['qualification'] = random.choice([
        "Plus Two",
        "Diploma",
        "Degree",
        "Post Graduation"
    ])

    student['math_marks'] = random.randint(40, 100)
    student['computer_marks'] = random.randint(40, 100)
    student['english_marks'] = random.randint(40, 100)
    student['statistics_marks'] = random.randint(40, 100)

    # Technical Skills
    student['python_skill'] = random.randint(0, 10)
    student['java_skill'] = random.randint(0, 10)
    student['cpp_skill'] = random.randint(0, 10)
    student['sql_skill'] = random.randint(0, 10)
    student['html_skill'] = random.randint(0, 10)
    student['css_skill'] = random.randint(0, 10)
    student['javascript_skill'] = random.randint(0, 10)
    student['machine_learning_skill'] = random.randint(0, 10)

    # Professional Skills
    student['communication_skill'] = random.randint(0, 10)
    student['problem_solving'] = random.randint(0, 10)
    student['creativity'] = random.randint(0, 10)
    student['leadership'] = random.randint(0, 10)

    # Student Interest
    student['interest'] = random.choice([
        "Data Science",
        "Web Development",
        "Artificial Intelligence",
        "Cyber Security",
        "Software Development",
        "Business Analytics"
    ])

    # Career Recommendation
    interest = student['interest']

    if interest == "Data Science":
        if student['python_skill'] >= 5 and student['statistics_marks'] >= 60:
            career = "Data Scientist"
        else:
            career = "Data Analyst"

    elif interest == "Web Development":
        if student['html_skill'] >= 5 and student['css_skill'] >= 5:
            career = "Web Developer"
        else:
            career = "Frontend Developer"

    elif interest == "Artificial Intelligence":
        if student['machine_learning_skill'] >= 5 and student['python_skill'] >= 5:
            career = "AI Engineer"
        else:
            career = "Machine Learning Engineer"

    elif interest == "Cyber Security":
        if student['problem_solving'] >= 6 and student['sql_skill'] >= 4:
            career = "Cyber Security Analyst"
        else:
            career = "Security Analyst"

    elif interest == "Software Development":
        if student['python_skill'] >= 5 or student['java_skill'] >= 5:
            career = "Software Developer"
        else:
            career = "Junior Software Developer"

    else:
        career = "Business Analyst"

    student['career'] = career

    students.append(student)


# Convert into DataFrame

df = pd.DataFrame(students, columns=columns)

print("Dataset Created Successfully!")
print("Total Students:", len(df))
print("Total Columns:", len(df.columns))

print(df.head())

# Save Dataset

df.to_csv("CareerMatch_100000.csv", index=False)

print("Dataset Saved Successfully!")
# Dataset Inspection

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCareer Distribution:")
print(df['career'].value_counts())
import matplotlib.pyplot as plt
import seaborn as sns

# Career Distribution

plt.figure(figsize=(12, 6))

sns.countplot(
    data=df,
    y='career',
    order=df['career'].value_counts().index
)

plt.title("Career Distribution of Students")
plt.xlabel("Number of Students")
plt.ylabel("Career")

plt.tight_layout()
plt.show()
# Career Distribution Visualization

plt.figure(figsize=(12, 7))

sns.countplot(
    data=df,
    y='career',
    order=df['career'].value_counts().index
)

plt.title("Career Distribution of 100000 Students")
plt.xlabel("Number of Students")
plt.ylabel("Career")

plt.tight_layout()
plt.show()
# Correlation Analysis

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation = numeric_df.corr()

plt.figure(figsize=(14, 10))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Student Skills Correlation Heatmap")

plt.tight_layout()
plt.show()
# Correlation Heatmap

numeric_df = df.select_dtypes(include=['number'])

correlation = numeric_df.corr()

plt.figure(figsize=(14, 10))

sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')

plt.title("Student Skills Correlation Heatmap")

plt.tight_layout()
print("\nCorrelation Matrix:")
print(correlation.round(2))
plt.show()
# STEP 9 - Data Cleaning

# Check Missing Values
print("Missing Values Before Cleaning:")
print(df.isnull().sum().sum())

# Remove Duplicate Records
df.drop_duplicates(inplace=True)

# Check Data Types
print("\nDataset Data Types:")
print(df.dtypes)

# Check Dataset Shape
print("\nFinal Dataset Shape:")
print(df.shape)

# Save Clean Dataset
df.to_csv("CareerMatch_Cleaned.csv", index=False)

print("\nData Cleaning Completed Successfully!")
# STEP 10 - Feature Engineering

# Average Marks
df['average_marks'] = df[
    ['math_marks',
     'computer_marks',
     'english_marks',
     'statistics_marks']
].mean(axis=1)

# Total Marks
df['total_marks'] = df[
    ['math_marks',
     'computer_marks',
     'english_marks',
     'statistics_marks']
].sum(axis=1)

# Technical Skill Score
df['technical_skill_score'] = df[
    ['python_skill',
     'java_skill',
     'cpp_skill',
     'sql_skill',
     'html_skill',
     'css_skill',
     'javascript_skill',
     'machine_learning_skill']
].mean(axis=1)

# Professional Skill Score
df['professional_skill_score'] = df[
    ['communication_skill',
     'problem_solving',
     'creativity',
     'leadership']
].mean(axis=1)

print("\nFeature Engineering Completed!")

print(df.head())

print("\nNew Dataset Shape:")
print(df.shape)

# Save Updated Dataset
df.to_csv("CareerMatch_Featured.csv", index=False)
print("hello")