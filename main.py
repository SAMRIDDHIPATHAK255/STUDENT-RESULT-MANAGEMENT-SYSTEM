from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



df = pd.read_csv("results.csv", index_col=0)


if "Total" not in df.columns:
    df["Total"] = df[["Hindi","English","Science","Maths","History","Geograpgy"]].sum(axis=1)

df["Result"] = df["Total"].apply(lambda x: 1 if x >= 200 else 0)


X = df[["Hindi","English","Science","Maths","History","Geograpgy"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
cls_model = LogisticRegression()
cls_model.fit(X_train, y_train)


y_pred = cls_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc*100:.2f}%")


print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))



root = Tk()
root.title("AI-Enhanced Student Result Management System")
root.geometry("650x550")
root.configure(bg="#f0f0f0")

Label(root, text="AI-Enhanced Student Result System",
      font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)


frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=10)


labels = ["Division", "Hindi", "English", "Maths", "Science", "History", "Geography"]
entries = {}

for i, label in enumerate(labels):
    Label(frame, text=label + ":", font=("Arial", 12), bg="#f0f0f0").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = Entry(frame, font=("Arial", 12), width=20)
    entry.grid(row=i, column=1, pady=5)
    entries[label] = entry


def calculate_result():
    try:
        marks = [float(entries[sub].get()) for sub in labels[1:]]
        total = sum(marks)
        avg = total / 6

        # Grade logic
        if avg >= 90:  grade = 'A+'
        elif avg >= 80: grade = 'A'
        elif avg >= 70: grade = 'B'
        elif avg >= 60: grade = 'C'
        else: grade = 'F'

        messagebox.showinfo("Result",
                            f"Total Marks: {total}\nAverage: {avg:.2f}\nGrade: {grade}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")


def predict_pass_fail():
    try:
        marks = [float(entries[sub].get()) for sub in labels[1:]]
        arr = np.array(marks).reshape(1, -1)

        result = cls_model.predict(arr)[0]
        msg = "PASS 🎉" if result == 1 else "FAIL ❌"

        messagebox.showinfo("AI Prediction", f"Predicted Result: {msg}")

    except:
        messagebox.showerror("Error", "Please fill all fields correctly!")


def save_to_csv():
    try:
        div = entries["Division"].get()
        marks = [float(entries[sub].get()) for sub in labels[1:]]
        total = sum(marks)

        new_row = {
            "Roll": len(df) + 1,
            "Div": div,
            "Hindi": marks[0],
            "English": marks[1],
            "Maths": marks[2],
            "Science": marks[3],
            "History": marks[4],
            "Geograpgy": marks[5],
            "Total": total,
            "Result": 1 if total >= 200 else 0
        }

        df.loc[len(df)] = new_row
        df.to_csv("results.csv")

        messagebox.showinfo("Success", "Student data saved!")

    except:
        messagebox.showerror("Error", "Invalid input. Cannot save!")


def show_average_graph():
    sub_means = df[["Hindi","English","Science","Maths","History","Geograpgy"]].mean()
    sub_means.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average")
    plt.show()

def show_correlation():
    plt.figure(figsize=(7,5))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


Button(root, text="Calculate Result", command=calculate_result,
       bg="#90ee90", font=("Arial", 12), width=20).pack(pady=10)

Button(root, text="AI Predict Pass/Fail", command=predict_pass_fail,
       bg="#87cefa", font=("Arial", 12), width=20).pack(pady=5)

Button(root, text="Save Student to CSV", command=save_to_csv,
       bg="#f4a460", font=("Arial", 12), width=20).pack(pady=5)

Button(root, text="Show Average Graph", command=show_average_graph,
       bg="#dda0dd", font=("Arial", 12), width=20).pack(pady=5)

Button(root, text="Show Correlation Heatmap", command=show_correlation,
       bg="#ffa07a", font=("Arial", 12), width=20).pack(pady=5)

root.mainloop()


