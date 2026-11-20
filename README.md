# Implement-Various-Types-of-Visualization-in-Python

Aim: To write a Python program to implement various types of visualization in Python.

Algorithm:

1.Start.

2.Import Pandas and Matplotlib libraries.

3.Create a dataset.

4.Create a DataFrame.

5.Draw a bar chart.

6.Draw a line chart.

7.Draw a pie chart.

8.Draw a histogram.

9.Display all visualizations.

10.Stop.

Source Code:

# Various Types of Visualization in Python

import pandas as pd

import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Name": ["Arun", "Bala", "Charan", "Divya",
             "Esha", "Farhan", "Geeta", "Hari"],

   "Marks": [65, 72, 90, 65, 78, 88, 95, 70]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# 1. Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

# 2. Line Chart
plt.figure()
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart
plt.figure()
plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Student Marks - Pie Chart")
plt.show()

# 4. Histogram
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Student Marks - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
<img width="1460" height="1013" alt="Screenshot 2026-11-20 192149" src="https://github.com/user-attachments/assets/e5a6b2aa-a36a-4857-9553-fcb84d7abe6c" />
<img width="1622" height="1046" alt="image" src="https://github.com/user-attachments/assets/3ad548de-9cfe-4376-a5e2-39ed92d303da" />
<img width="1776" height="1092" alt="image" src="https://github.com/user-attachments/assets/baae4de8-22f8-415e-8d3d-0ce7cf239a7b" />
<img width="1561" height="1086" alt="image" src="https://github.com/user-attachments/assets/1b38ebb8-ad80-4235-91ed-ac7e0ba767a5" />
