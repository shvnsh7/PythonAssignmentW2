from tabulate import tabulate

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

print(dict)


print("{:<15} {:<12} {:<10} {:<15} {:<15} {:<7}".format(
    "Name of the Day", "Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"
))
for day, info in dict.items():
    print("{:<15} {:<12} {:<10} {:<15} {:<15} {:<7}".format(
        day, *info
    ))
# def ShortForm(day):
#     sf = day[0:3]
#     return sf

# dict_table = []
# headers = ['Name of the Day', 'Occurrences', 'Short Form', 'Name in Lower', 'Name in upper', 'Length']
# for i in range(7):
#     day = daysofWeek[i]
#     row = [
#         day,
#         i + 1,
#         ShortForm(day),
#         day.lower(),
#         day.upper(),
#         len(day)
#     ]
#     dict_table.append(row)

# print(tabulate(dict_table, headers, tablefmt="grid"))



# def create_day_information(day_name):
#     return [
#         daysofWeek.index(day_name) + 1,
#         day_name[:3],
#         day_name.lower(),
#         day_name.upper(),
#         len(day_name)
#     ]
# # print(create_day_info())

# days_table = []

# for day_name in daysofWeek:
#     days_table.append([day_name] + create_day_information(day_name))

# # This will enerate the table
# headers = ['Name of the Day', 'Occurrences', 'Short Form', 'Name in Lower', 'Name in upper', 'Length']
# print(tabulate(days_table, headers=headers, tablefmt='grid'))



# import pandas as pd
# days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# day_info_dict = {}
# for i, day in enumerate(days_of_week, start=1):
#     day_info_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))

# df = pd.DataFrame.from_dict(day_info_dict, orient='index', columns=["Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
# df.to_excel("days_info.xlsx", index_label="Name of the Day")