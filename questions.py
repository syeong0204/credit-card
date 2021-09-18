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
""")
if inc == '1':
    final[15] = 1
if inc == '2':
    final[16] = 1
if inc == '3':
    final[17] = 1
if inc == '4':
    final[18] = 1
if inc == '5':
    final[19] = 1

edu = input("""1. Academic degree
2. Higher education
3. Incomplete higher
4. Lower secondary
5. Secondary / secondary special: """)

if edu == '1':
    final[20] = 1
if edu == '2':
    final[21] = 1
if edu == '3':
    final[22] = 1
if edu == '4':
    final[23] = 1
if edu == '5':
    final[24] = 1
    
fam = input("""1. Civil marriage 
2. Married
3. Separated
4. Single / not married
5. Widow
""")

if fam == '1':
    final[25] = 1
if fam == '2':
    final[26] = 1
if fam == '3':
    final[27] = 1
if fam == '4':
    final[28] = 1
if fam == '5':
    final[29] = 1
    
home = input("""1. Co-op apartment
2. House / apartment
3. Municipal apartment
4. Office apartment
5. Rented apartment
6. With parents: """)

if home == '1':
    final[30] = 1
if home == '2':
    final[31] = 1
if home == '3':
    final[32] = 1
if home == '4':
    final[33] = 1
if home == '5':
    final[34] = 1
if home == '6':
    final[35] = 1

occ = input("""1. Accountants 
2. Cleaning staff
3. Cooking staff 
4. Core staff
5. Drivers 
6. HR staff
7. High skill tech staff 
8. IT staff
9. Laborers
10. Low-skill Laborers
11. Managers
12. Medicine staff
13. Private service staff
14. Realty agents 
15. Sales staff
16. Secretaries 
17. Security staff
18. Waiters/barmen staff """)

if occ == '1':
    final[36] = 1
if occ == '2':
    final[37] = 1
if occ == '3':
    final[38] = 1
if occ == '4':
    final[39] = 1
if occ == '5':
    final[40] = 1
if occ == '6':
    final[41] = 1
if occ == '7':
    final[42] = 1
if occ == '8':
    final[43] = 1
if occ == '9':
    final[44] = 1
if occ == '10':
    final[45] = 1
if occ == '11':
    final[46] = 1
if occ == '12':
    final[47] = 1
if occ == '13':
    final[48] = 1
if occ == '14':
    final[49] = 1
if occ == '15':
    final[50] = 1
if occ == '16':
    final[51] = 1
if occ == '17':
    final[52] = 1
if occ == '18':
    final[53] = 1