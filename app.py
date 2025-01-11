from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Inisialisasi Flask app
app = Flask(__name__)

# Memuat model, encoder, dan scaler
with open('./model/stroke_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('./model/label_encoders.pkl', 'rb') as encoders_file:
    label_encoders = pickle.load(encoders_file)

with open('./model/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk melakukan prediksi
@app.route('/predict', methods=['POST'])
def predict():
    # Mengambil input dari form
    gender = request.form['gender']
    age = int(request.form['age'])
    hypertension = int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    ever_married = request.form['ever_married']
    work_type = request.form['work_type']
    residence_type = request.form['residence_type']
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    smoking_status = request.form['smoking_status']
    
    # Melakukan encoding pada variabel kategori menggunakan label encoder
    encoded_data = {
        'gender': label_encoders['gender'].transform([gender])[0],
        'ever_married': label_encoders['ever_married'].transform([ever_married])[0],
        'work_type': label_encoders['work_type'].transform([work_type])[0],
        'Residence_type': label_encoders['Residence_type'].transform([residence_type])[0],
        'smoking_status': label_encoders['smoking_status'].transform([smoking_status])[0]
    }
    
    # Menyusun data input sesuai dengan model
    input_data = [
        [
            encoded_data['gender'],
            age,
            hypertension,
            heart_disease,
            encoded_data['ever_married'],
            encoded_data['work_type'],
            encoded_data['Residence_type'],
            avg_glucose_level,
            bmi,
            encoded_data['smoking_status']
        ]
    ]
    
    # Menggunakan scaler untuk fitur numerik (age, avg_glucose_level, bmi)
    input_data_scaled = scaler.transform(input_data)

    # Prediksi menggunakan model
    prediction = model.predict(input_data_scaled)

    # Menentukan hasil prediksi
    result = "Pasien berisiko stroke." if prediction[0] == 1 else "Pasien tidak berisiko stroke."
    
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)