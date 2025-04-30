from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
scaler = pickle.load(open("models5/scaler.pkl", 'rb'))  
model_gbc = pickle.load(open("models5/model_gbc.pkl", 'rb'))

# Encoding function (manually matches notebook)
def encode_input(data):
    data['htn'] = 1 if data['htn'].lower() == 'yes' else 0
    data['dm'] = 1 if data['dm'].lower() == 'yes' else 0
    data['cad'] = 1 if data['cad'].lower() == 'yes' else 0
    data['appet'] = 1 if data['appet'].lower() == 'good' else 0
    data['pc'] = 1 if data['pc'].lower() == 'normal' else 0
    return data

@app.route('/')
def home():
    return render_template('index3.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract and prepare input data
            input_data = {
                'age': float(request.form['age']),
                'bp': float(request.form['bp']),
                'sg': float(request.form['sg']),
                'al': float(request.form['al']),
                'hemo': float(request.form['hemo']),
                'sc': float(request.form['sc']),
                'htn': request.form['htn'],
                'dm': request.form['dm'],
                'cad': request.form['cad'],
                'appet': request.form['appet'],
                'pc': request.form['pc']
            }

            # Apply manual encoding
            input_data = encode_input(input_data)

            # Convert to DataFrame
            df = pd.DataFrame([input_data])

            # Scale numerical columns
            numeric_cols = ['age', 'bp', 'sg', 'al', 'hemo', 'sc']
            df[numeric_cols] = scaler.transform(df[numeric_cols])

            # Make prediction
            prediction = model_gbc.predict(df)
            result = "The patient has CKD." if prediction[0] == 1 else "The patient does not have CKD."

            return render_template('index3.html', prediction_text=result)

        except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
