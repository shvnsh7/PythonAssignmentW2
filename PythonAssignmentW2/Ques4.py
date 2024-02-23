''''4. Use the python Faker module to generate fake data for the following.
	a. Create an excel sheet "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

	4a. WAF to return the empolyee name with top most salary
	4b. WAF to return the Business Unit with top most aggregated salary
	4c. WAF to return the employee name in each Business Unit with top most salary
	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
	4e. WAF to Update the Salary Details of an Employee in the Excel File'''
import pandas as pd
from faker import Faker
# from openpyxl.workbook import Workbook

fake = Faker() 
data = []
for e in range(50): 
    emp_id = fake.unique.random_number(digits=5)
    emp_name = fake.name()
    emp_email = fake.email()
    business_unit = fake.random_element(elements=('HR', 'Finance', 'IT', 'Sales'))
    salary = fake.random_number(digits=5)
    data.append([emp_id, emp_name, emp_email, business_unit, salary])
 
df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
# Save DataFrame to Excel
df.to_excel("Employee_Personal_Details.xlsx", index=False)

# WAF to return the empolyee name with top most salary
def get_employee_with_top_salary():   #top most salary
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    max_salary_row = df[df['Salary'] == df['Salary'].max()]
    return max_salary_row['EMP NAME'].iloc[0]

print("Emplyee With top salary: ",get_employee_with_top_salary())

# WAF to return the Business Unit with top most aggregated salary
def get_business_unit_with_top_salary():
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    aggregated_salary = df.groupby("Business Unit")["Salary"].sum()
    max_aggregated_salary = aggregated_salary.max()
    top_business_unit = aggregated_salary[aggregated_salary == max_aggregated_salary].index[0]
    return top_business_unit

print("Business unit with top salary: ",get_business_unit_with_top_salary())

file_path="Employee_Personal_Details.xlsx"
# WAF to return the employee name in each Business Unit with top most salary
def get_employee_with_top_salary_per_business_unit(file_path):
    df = pd.read_excel(file_path)
    top_employees = df.groupby("Business Unit").apply(lambda x: x.nlargest(1, "Salary"))
    return top_employees[["Business Unit", "EMP NAME"]]

print("Employees with top salary per business unit: ",get_employee_with_top_salary_per_business_unit(file_path))

# WAF Delete the Record of the Employee name from the Excel File with the least salary.
def delete_employee_with_least_salary():
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    min_salary = df["Salary"].min()
    df = df[df["Salary"] != min_salary]
    df.to_excel(file_path, index=False)
print("least_salary: ",delete_employee_with_least_salary())    
# print("least salary: ",delete_employee_with_least_salary(file_path="Employee_Personal_Details.xlsx"))

# WAF to Update the Salary Details of an Employee in the Excel File
def update_employee_salary(file_path, employee_name, new_salary):
    df = pd.read_excel(file_path)
    df.loc[df["EMP NAME"] == employee_name, "Salary"] = new_salary
    df.to_excel(file_path, index=False)
    
print("update_employee_salary",update_employee_salary())
    
    








# import pandas as pd
# from faker import Faker

# # Function to generate fake data and create the Excel file
# def generate_fake_data(file_name, num_records):
#     fake = Faker()

#     data = []
#     for _ in range(num_records):
#         emp_id = fake.random_int(min=1000, max=9999)
#         emp_name = fake.name()
#         emp_email = fake.email()
#         business_unit = fake.random_element(elements=('Sales', 'Marketing', 'Finance', 'IT'))
#         salary = fake.random_int(min=50000, max=100000)

#         data.append([emp_id, emp_name, emp_email, business_unit, salary])

#     df = pd.DataFrame(data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
#     df.to_excel(file_name, index=False)

# # Function to return the employee name with the topmost salary
# def get_employee_with_top_salary(file_name):
#     df = pd.read_excel(file_name)
#     max_salary = df['Salary'].max()
#     top_employee = df.loc[df['Salary'] == max_salary, 'EMP NAME'].values[0]
#     return top_employee

# # Function to return the business unit with the topmost aggregated salary
# def get_business_unit_with_top_salary(file_name):
#     df = pd.read_excel(file_name)
#     grouped_data = df.groupby('Business Unit')['Salary'].sum()
#     max_aggregated_salary = grouped_data.max()
#     top_business_unit = grouped_data.loc[grouped_data == max_aggregated_salary].index[0]
#     return top_business_unit

# # Function to return employee names in each business unit with the topmost salary
# def get_employee_with_top_salary_per_business_unit(file_name):
#     df = pd.read_excel(file_name)
#     result = {}
#     for business_unit in df['Business Unit'].unique():
#         filtered_data = df[df['Business Unit'] == business_unit]
#         max_salary = filtered_data['Salary'].max()
#         top_employee = filtered_data.loc[filtered_data['Salary'] == max_salary, 'EMP NAME'].values[0]
#         result[business_unit] = top_employee
#     return result

# # Function to delete the record of the employee with the least salary
# def delete_employee_with_least_salary(file_name):
#     df = pd.read_excel(file_name)
#     min_salary = df['Salary'].min()
#     df = df[df['Salary'] != min_salary]
#     df.to_excel(file_name, index=False)

# # Function to update the salary details of an employee
# def update_employee_salary(file_name, emp_name, new_salary):
#     df = pd.read_excel(file_name)
#     df.loc[df['EMP NAME'] == emp_name, 'Salary'] = new_salary
#     df.to_excel(file_name, index=False)

# # Generate fake data and create the Excel file
# generate_fake_data("Employee_Personal_Details.xlsx", 100)

# # Test the functions
# print(get_employee_with_top_salary("Employee_Personal_Details.xlsx"))
# print(get_business_unit_with_top_salary("Employee_Personal_Details.xlsx"))
# print(get_employee_with_top_salary_per_business_unit("Employee_Personal_Details.xlsx"))
# delete_employee_with_least_salary("Employee_Personal_Details.xlsx")
# update_employee_salary("Employee_Personal_Details.xlsx", "John Doe", 75000)


