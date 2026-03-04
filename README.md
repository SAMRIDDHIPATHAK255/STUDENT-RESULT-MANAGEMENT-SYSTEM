# STUDENT-RESULT-MANAGEMENT-SYSTEM

# 🎓 AI-Enhanced Student Result Management System
Here is a **properly formatted GitHub README** for your project:

---

# 🎓 AI-Enhanced Student Result Management System

## 📌 Overview

The AI-Enhanced Student Result Management System is a desktop-based application developed using Python and Tkinter that integrates Machine Learning for intelligent academic result prediction. The system allows users to enter student marks for six subjects, automatically calculate total marks, average, and grade, and predict pass/fail status using a trained Logistic Regression model. It also provides data visualization features and supports persistent storage using CSV files.

---

## 🚀 Features

* ✅ Calculate Total Marks and Average
* ✅ Generate Grade (A+, A, B, C, F)
* ✅ AI-based Pass/Fail Prediction
* ✅ Save Student Records to CSV
* ✅ Subject-wise Average Bar Graph
* ✅ Correlation Heatmap Visualization

---

## 🛠️ Technologies Used

* Python 3.x
* Tkinter (GUI)
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🧠 Machine Learning Details

* **Algorithm:** Logistic Regression
* **Type:** Binary Classification (Pass/Fail)
* **Train-Test Split:** 80% Training, 20% Testing
* **Evaluation Metrics:**

  * Accuracy Score
  * Confusion Matrix
  * Classification Report

**Prediction Rule:**

* Total Marks ≥ 200 → Pass
* Total Marks < 200 → Fail

---

## 📂 Project Structure

```
AI-Student-Result-System/
│
├── results.csv        # Dataset file
├── main.py            # Main application file
└── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2️⃣ Place Dataset

Ensure `results.csv` is in the same directory as the Python file.

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 📊 Dataset Requirements

The `results.csv` file should contain the following columns:

* Roll
* Div
* Hindi
* English
* Maths
* Science
* History
* Geograpgy
* Total (optional – auto-generated if missing)
* Result (auto-generated if missing)

---

## 🎯 Learning Outcomes

This project demonstrates:

* Integration of Machine Learning into a GUI application
* Supervised learning implementation
* Model evaluation techniques
* Data visualization
* File handling and data persistence

---

## 🔮 Future Enhancements

* Deploy as a web application using Flask
* Add database integration (MySQL)
* Implement advanced ML algorithms for comparison
* Add student login and authentication system

---

## 👩‍💻 Author

**Samriddhi Pathak**
Data Science & Machine Learning Enthusiast

---
