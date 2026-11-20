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
