import pandas as pd

employees = pd.DataFrame({
    "employee_id": ["E101", "E102", "E103", "E104"],
    "employee_name": ["Anitha", "Rahul", "Priya", "Kavin"],
    "department": ["AI & ML", "Sales", "HR", "IT"],
    "location": ["Chennai", "Chennai", "Bangalore", "Chennai"]
})

employees.to_excel(
    "data/employee_corrections.xlsx",
    index=False
)

print("Excel file created successfully!")