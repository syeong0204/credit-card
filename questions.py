final = []
for r in range(0,54):
    final.append(0)
    
children = input("How many children do you have? ")
final[0] = int(children)

income = input("What is your total income? ")
final[1] = int(income)

import datetime
from datetime import date
dob = input("When were you born (yyyy-mm-dd)? ")
year = dob[0:4]
month = dob[5:7]
day = dob[8:10]
print(year)
print(month)
print(day)

b_date = date(int(year), int(month), int(day))
f_date = date(2021, 9, 15)

delta = b_date - f_date
print(delta.days)
final[2] = int(delta.days)

wor = input("When did you start working (yyyy-mm-dd)? ")
yearw = wor[0:4]
monthw = wor[5:7]
dayw = wor[8:10]
print(yearw)
print(monthw)
print(dayw)

w_date = date(int(yearw), int(monthw), int(dayw))
f_date = date(2021, 9, 15)

deltaw = w_date - f_date
print(deltaw.days)
final[3] = int(deltaw.days)

mobile = input("Do you have a mobile phone Y or N? ")
work_phone = input("Do you have a work phone Y or N? ")
home_phone = input("Do you have a landline phone Y or N? ")
email = input("Do you have an email Y or N? ")

if mobile == 'Y':
    final[4] = 1
if mobile == 'N':
    final[4] = 0
    
if work_phone == 'Y':
    final[5] = 1
if work_phone == 'N':
    final[5] = 0

if home_phone == 'Y':
    final[6] = 1
if home_phone == 'N':
    final[6] = 0
    
if email == 'Y':
    final[7] = 1
if email == 'N':
    final[7] = 0
    
family_size = input("How many people are in your immediate family? ")
final[8] = int(family_size)

gender = input("Male or Female? (M or F) ")
if gender == 'M':
    final[9] = 0
    final[10] = 1

if gender == 'F':
    final[9] = 1
    final[10] = 0
    
car = input("Do you own a car Y or N? ")
if car == 'Y':
    final[11] = 0
    final[12] = 1

if car == 'N':
    final[11] = 1
    final[12] = 0

    
realty = input("Do you own a home? (Y or N) ")
if realty == 'Y':
    final[13] = 0
    final[14] = 1

if realty == 'N':
    final[13] = 1
    final[14] = 0
    

inc = input("""Enter the number that best represents your income type
1. Commercial associate 
2. Pensioner
3. State servant
4. Student
5. Working 
6. Academic degree
""")
if inc == '1':
    final[15] = 1
    final[16] = 0
    final[17] = 0
    final[18] = 0
    final[19] = 0
    final[20] = 0
if inc == '2':
    final[15] = 0
    final[16] = 1
    final[17] = 0
    final[18] = 0
    final[19] = 0
    final[20] = 0
if inc == '3':
    final[15] = 0
    final[16] = 0
    final[17] = 1
    final[18] = 0
    final[19] = 0
    final[20] = 0
if inc == '4':
    final[15] = 0
    final[16] = 0
    final[17] = 0
    final[18] = 1
    final[19] = 0
    final[20] = 0
if inc == '5':
    final[15] = 0
    final[16] = 0
    final[17] = 0
    final[18] = 0
    final[19] = 1
    final[20] = 0
if inc == '6':
    final[15] = 0
    final[16] = 0
    final[17] = 0
    final[18] = 0
    final[19] = 0
    final[20] = 1