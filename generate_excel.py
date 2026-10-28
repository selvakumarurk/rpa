import pandas as pd
import os

data = {
    "EmployeeID": ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010", "E011", "E012", "E013", "E014", "E015"],
    "EmployeeName": ["Arun", "Ravi", "Kumar", "Priya", "Anjali", "Suresh", "Ramesh", "Deepa", "Sneha", "Vikram", "Rahul", "Kavya", "Pooja", "Rohit", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing", "Sales", "IT", "Finance", "HR", "Marketing", "Sales", "IT", "Finance", "HR", "Marketing"],
    "Salary": [50000, 45000, 55000, 60000, 40000, 42000, 52000, -5000, 46000, 41000, 43000, 51000, 56000, 47000, 42000],
    "Status": ["Active", "Active", "Inactive", "Active", "Active", "Active", "Active", "Active", "Active", "Active", "Active", "Active", "Inactive", "Active", "Active"]
}

# Add some invalid records deliberately:
# E008 has negative salary
# E003 and E013 are inactive
# We will also add a row with missing EmployeeID and one with missing Name
data["EmployeeID"].append("")
data["EmployeeName"].append("TestUser1")
data["Department"].append("IT")
data["Salary"].append(30000)
data["Status"].append("Active")

data["EmployeeID"].append("E017")
data["EmployeeName"].append("")
data["Department"].append("HR")
data["Salary"].append(35000)
data["Status"].append("Active")

df = pd.DataFrame(data)

out_dir = r"c:\Users\ayush\Downloads\Uipath-RPA-AutomationProjects-project\Uipath-RPA-AutomationProjects-project\RE Framework 1\Data\Input"
os.makedirs(out_dir, exist_ok=True)
df.to_excel(os.path.join(out_dir, "EmployeeRecords.xlsx"), index=False)
print("Created Excel file successfully.")
