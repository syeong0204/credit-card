import pandas as pd
import flask
from flask import request, jsonify
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data_file = "/Users/julianapuskar/Desktop/credit_card/credit-card/cleaned_credit_card.csv"
data_df = pd.read_csv(data_file)
data_df

cc = pd.read_csv('/Users/julianapuskar/Desktop/credit_card/credit-card/cleaned_credit_card.csv')
app = pd.read_csv('/Users/julianapuskar/Desktop/credit_card/app_record_ml.csv')

df = pd.merge(cc, app, on='ID')
del df['Unnamed: 0']
del df['ID']

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


from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=50,
                               min_samples_split=2,
                               random_state=10)
tree.fit(X_train, y_train)
print(f"Training Data Score: {tree.score(X_train, y_train)}")
print(f"Testing Data Score: {tree.score(X_test, y_test)}")


tree2 = DecisionTreeClassifier(max_depth=50,
                               min_samples_split=2,
                               random_state=10)
tree2.fit(X2_train, y2_train)
print(f"Training Data Score: {tree.score(X2_train, y2_train)}")
print(f"Testing Data Score: {tree.score(X2_test, y2_test)}")

tree3 = DecisionTreeClassifier(max_depth=50,
                               min_samples_split=2,
                               random_state=10)
tree3.fit(X3_train, y3_train)
print(f"Training Data Score: {tree.score(X3_train, y3_train)}")
print(f"Testing Data Score: {tree.score(X3_test, y3_test)}")


tree4 = DecisionTreeClassifier(max_depth=50,
                               min_samples_split=2,
                               random_state=10)
tree4.fit(X4_train, y4_train)
print(f"Training Data Score: {tree.score(X4_train, y4_train)}")
print(f"Testing Data Score: {tree.score(X4_test, y4_test)}")


tree5 = DecisionTreeClassifier(max_depth=50,
                               min_samples_split=2,
                               random_state=10)
tree5.fit(X5_train, y5_train)
print(f"Training Data Score: {tree.score(X5_train, y5_train)}")
print(f"Testing Data Score: {tree.score(X5_test, y5_test)}")

@app.route('/')
def home():
    return '''<h1>app_record</h1>
<p>A prototype API for displaying data</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/credit_card/credit-card/cleaned_credit_card.csv/all', )
def api_all():
    return jsonify(results)

app.run()