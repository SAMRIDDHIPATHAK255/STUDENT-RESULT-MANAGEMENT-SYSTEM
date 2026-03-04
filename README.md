# STUDENT-RESULT-MANAGEMENT-SYSTEM

# 🎓 AI-Enhanced Student Result Management System
An intelligent desktop-based Student Result Management System built using Python, Tkinter, and Machine Learning.
The system calculates student grades, predicts pass/fail using Logistic Regression, stores records in CSV format, and provides graphical insights using data visualization.

📌 Project Overview

This project integrates:

📊 Data Analysis

🤖 Machine Learning (Logistic Regression)

🖥️ GUI Application using Tkinter

📈 Data Visualization using Matplotlib & Seaborn

📂 CSV File Handling using Pandas

The application allows users to:

Enter student marks

Calculate total, average, and grade

Predict pass/fail using a trained ML model

Save student data

View performance analytics through graphs

🛠️ Technologies Used

Python 3.x

Tkinter (GUI)

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

🧠 Machine Learning Model

Algorithm Used: Logistic Regression

Problem Type: Binary Classification (Pass/Fail)

Training/Test Split: 80/20

Evaluation Metrics:

Accuracy Score

Confusion Matrix

Classification Report

Prediction Logic:

Total Marks ≥ 200 → Pass (1)

Total Marks < 200 → Fail (0)

📂 Project Structure
AI-Student-Result-System/
│
├── results.csv        # Dataset file
├── main.py            # Main Python application
└── README.md          # Project documentation
⚙️ Features
1️⃣ Calculate Result

Computes:

Total Marks

Average

Grade (A+, A, B, C, F)

2️⃣ AI Predict Pass/Fail

Uses trained Logistic Regression model

Predicts result instantly

3️⃣ Save Student Data

Appends new student record to CSV file

4️⃣ Show Average Graph

Displays bar chart of subject-wise average marks

5️⃣ Show Correlation Heatmap

Displays correlation matrix between subjects and result

🖥️ GUI Preview

The interface includes:

Input fields for:

Division

Hindi

English

Maths

Science

History

Geography

Buttons for all major functionalities

Interactive message boxes for outputs

📊 Dataset Requirements

The results.csv file must contain the following columns:

Roll

Div

Hindi

English

Maths

Science

History

Geograpgy

Total (optional, auto-generated if missing)

Result (auto-generated)

🚀 How to Run the Project

Install required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn

Place results.csv in the same folder as the Python file.

Run the program:

python main.py
🎯 Learning Outcomes

This project demonstrates:

Practical implementation of supervised learning

Integration of ML model with GUI

Real-time prediction system

Data visualization techniques

File handling and persistent storage

📈 Future Improvements

Add database integration (MySQL)

Add student login system

Deploy as web app using Flask

Add performance trend analysis

Improve model with more advanced algorithms

👩‍💻 Author

Samriddhi Pathak
Data Science & Machine Learning Enthusiast
