from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import datetime
from datetime import date



app = Flask(__name__)

@app.route("/form")
def form():
    return render_template("form.html")


cc = pd.read_csv('cleaned_credit_card.csv')
app = pd.read_csv('app_record_ml.csv')

df = pd.merge(cc, app, on='ID')
del df['Unnamed: 0']
del df['ID']

df = df.dropna()

X = df.drop(['0', '1', '2', '3', '4', '5', 'X', 'C'], axis=1)
y = df[['0', '1', '2', '3', '4', '5', 'X', 'C']]

twos = y['2']
threes = y['3']
fours = y['4']
fives = y['5']
zeroes = y['0']
y['score'] = y['1']
y = y['score']

X_train, X_test, y_train, y_test = train_test_split(X, y)
X2_train, X2_test, y2_train, y2_test = train_test_split(X, twos)
X3_train, X3_test, y3_train, y3_test = train_test_split(X, threes)
X4_train, X4_test, y4_train, y4_test = train_test_split(X, fours)
X5_train, X5_test, y5_train, y5_test = train_test_split(X, fives)
X0_train, X0_test, y0_train, y0_test = train_test_split(X, zeroes)

tree = DecisionTreeClassifier(max_depth=50, min_samples_split=2,random_state=10)
tree.fit(X_train, y_train)


tree2 = DecisionTreeClassifier(max_depth=50, min_samples_split=2, random_state=10)
tree2.fit(X2_train, y2_train)


tree3 = DecisionTreeClassifier(max_depth=50, min_samples_split=2, random_state=10)
tree3.fit(X3_train, y3_train)


tree4 = DecisionTreeClassifier(max_depth=50, min_samples_split=2, random_state=10)
tree4.fit(X4_train, y4_train)


tree5 = DecisionTreeClassifier(max_depth=50, min_samples_split=2, random_state=10)
tree5.fit(X5_train, y5_train)


tree0 = DecisionTreeClassifier(max_depth=50, min_samples_split=2, random_state=10)
tree0.fit(X0_train, y0_train)

@app.route("/test/<noc>/<inc>/<dofb>/<dofw>/<tech>/<famsize>/<info>/<jobtype>")
def modelrun(noc, inc, dofb, dofw, tech, famsize, info, jobtype):
    final = []
    for r in range(0,54):
        final.append(0)

    children = noc
    final[0] = int(children)

    income = inc
    final[1] = int(income)

    dob = dofb
    year = dob[0:4]
    month = dob[5:7]
    day = dob[8:10]
    print(year)
    print(month)
    print(day)

    b_date = date(int(year), int(month), int(day))
    f_date = date(2021, 9, 21)

    delta = b_date - f_date
    print(delta.days)
    final[2] = int(delta.days)

    wor = dofw
    yearw = wor[0:4]
    monthw = wor[5:7]
    dayw = wor[8:10]
    print(yearw)
    print(monthw)
    print(dayw)

    w_date = date(int(yearw), int(monthw), int(dayw))
    f_date = date(2021, 9, 21)

    deltaw = w_date - f_date
    print(deltaw.days)
    final[3] = int(deltaw.days)

    mobile = tech[0]
    work_phone = tech[1]
    home_phone = tech[2]
    email = tech[3]

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

    family_size = famsize
    final[8] = int(family_size)

    gender = info[0]
    if gender == 'M':
        final[9] = 0
        final[10] = 1

    if gender == 'F':
        final[9] = 1
        final[10] = 0

    car = info[1]
    if car == 'Y':
        final[11] = 0
        final[12] = 1

    if car == 'N':
        final[11] = 1
        final[12] = 0


    realty = info[2]
    if realty == 'Y':
        final[13] = 0
        final[14] = 1

    if realty == 'N':
        final[13] = 1
        final[14] = 0

    inc = info[3]
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

    edu = info[4]

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

    fam = info[5]

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

    home = info[6]

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

    occ = jobtype

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

    one = tree.predict([final])[0]
    zero = tree0.predict([final])[0]
    two = tree2.predict([final])[0]
    three = tree3.predict([final])[0]
    four = tree4.predict([final])[0]
    five = tree5.predict([final])[0]

    return(f"{zero} zeroes, {one} ones, {two} twos, {three} threes, {four} fours, {five} fives")



if __name__ == "__main__":
    app.run(debug=True)
