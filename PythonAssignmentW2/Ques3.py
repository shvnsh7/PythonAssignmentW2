import pandas as pd
daysofWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


dict={}
def ShortForm(day):
    sf=day[0:3]
    return sf

for i in range(7):
    days_dict={
        daysofWeek[i]: (i+1,ShortForm(daysofWeek[i]),daysofWeek[i].lower(),daysofWeek[i].upper(),len(daysofWeek[i]))  
    }
    #print(days_dict)
    dict.update(days_dict)

#print(dict)

df = pd.DataFrame.from_dict(dict, orient='index', columns=["Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
df.to_excel("days_info.xlsx", index_label="Name of the Day")











# import pandas as pd
# from tabulate import tabulate

# def create_day_info(day_name):
#     return [
#         daysofWeek.index(day_name) + 1,
#         day_name[:3],
#         day_name.lower(),
#         day_name.upper(),
#         len(day_name)
#     ]


# daysofWeek=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturay","Sunday")

# days_table = []

# for day_name in daysofWeek:
#     days_table.append([day_name] + create_day_info(day_name))

# # Generate the table
# headers = ['Day Name', 'Occurrence', 'Short Form', 'Lowercase', 'Uppercase', 'Length']
# table = tabulate(days_table, headers=headers, tablefmt='grid')

# # Store the table output
# table_output = f"Table:\n{table}"

# # Create a DataFrame from the table
# df = pd.DataFrame(days_table, columns=headers)

# # Save the DataFrame to an Excel file
# df.to_excel('days_table.xlsx', index=False)

# # Print the table output
# print(table_output)