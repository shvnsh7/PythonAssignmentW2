from collections import Counter
###### a 
daysofWeek=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturay","Sunday")
def consDay1(daysofWeek):
    consecutiveDays=[(daysofWeek[i],daysofWeek[i+1]) for i in range(0,len(daysofWeek)-1)]
    print(consecutiveDays)
# consDay1(daysofWeek)


def ConsDays(daysofWeek):
    res=[] #emptylist
    for i in range(0,len(daysofWeek)-1):
        tuple_elements=(daysofWeek[i],daysofWeek[i+1])
        res.append(tuple_elements)
    print(res)

# ConsDays(daysofWeek)



###### b  i.e {"Monday":(1,"Mon",monday,MONDAY,6)} 
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

char_occurences=tuple((day,Counter(day)) for day in daysofWeek)

# print(char_occurences)

occurences=[]
for day in daysofWeek:  #first iterating through days of week
    element_occurence={}
    for char in day:  #Then iterating through particular day characters
        element_occurence[char]=day.count(char)
    occurences.append(element_occurence)
print(occurences)

