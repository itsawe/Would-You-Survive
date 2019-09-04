import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request
import preprocessing

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/titanic/api/v1.0/predict', methods=['GET'])
def get_predict():
    passenger = {}
    
    passenger['Name'] = request.args.get('n')
    passenger['Pclass'] = int(float(request.args.get('c')))
    passenger['Sex'] = request.args.get('s')
    passenger['Age'] = int(float(request.args.get('a')))
    passenger['Fare'] = float(request.args.get('f'))
    passenger['IsAlone'] = int(float(request.args.get('fam')))
    passenger['Embarked'] = request.args.get('e')
    passenger['HasCabin'] = int(request.args.get('ca'))
    
    data = pd.DataFrame(passenger, index=[0])
    
    data_mod = preprocessing.process_data(data)
    predict = model.predict(data_mod)
#    predict=1
    
    survived = 'yes' if predict else 'no'
    return jsonify({'survived': survived})

if __name__ == "__main__":
    app.run(debug=True)