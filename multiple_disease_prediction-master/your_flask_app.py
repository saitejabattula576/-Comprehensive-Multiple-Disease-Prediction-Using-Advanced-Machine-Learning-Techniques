from flask import Flask, render_template, request
import os
import pickle

#
app = Flask(__name__)

working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))
liver_disease_model = pickle.load(open(f'{working_dir}/liver_disease_model.sav', 'rb'))

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the diabetes prediction page
@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = [request.form['Pregnancies'], request.form['Glucose'], request.form['BloodPressure'],
                      request.form['SkinThickness'], request.form['Insulin'], request.form['BMI'],
                      request.form['DiabetesPedigreeFunction'], request.form['Age']]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        return render_template('diabetes.html', diagnosis=diab_diagnosis)
    return render_template('diabetes.html', diagnosis='')

# Route for the heart disease prediction page
@app.route('/heart', methods=['GET', 'POST'])
def heart():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = [request.form['age'], request.form['sex'], request.form['cp'], request.form['trestbps'],
                      request.form['chol'], request.form['fbs'], request.form['restecg'], request.form['thalach'],
                      request.form['exang'], request.form['oldpeak'], request.form['slope'], request.form['ca'], request.form['thal']]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        return render_template('heart.html', diagnosis=heart_diagnosis)
    return render_template('heart.html', diagnosis='')

# Route for the Parkinson's prediction page
@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = [request.form['fo'], request.form['fhi'], request.form['flo'], request.form['Jitter_percent'],
                      request.form['Jitter_Abs'], request.form['RAP'], request.form['PPQ'], request.form['DDP'],
                      request.form['Shimmer'], request.form['Shimmer_dB'], request.form['APQ3'], request.form['APQ5'],
                      request.form['APQ'], request.form['DDA'], request.form['NHR'], request.form['HNR'],
                      request.form['RPDE'], request.form['DFA'], request.form['spread1'], request.form['spread2'],
                      request.form['D2'], request.form['PPE']]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        return render_template('parkinsons.html', diagnosis=parkinsons_diagnosis)
    return render_template('parkinsons.html', diagnosis='')

# Route for the liver disease prediction page
@app.route('/liver', methods=['GET', 'POST'])
def liver():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = [request.form['Age'], request.form['Gender'], request.form['Total_Bilirubin'], request.form['Direct_Bilirubin'],
                      request.form['Alkaline_Phosphotase'], request.form['Alamine_Aminotransferase'], request.form['Aspartate_Aminotransferase'],
                      request.form['Total_Proteins'], request.form['Albumin'], request.form['Albumin_and_Globulin_Ratio']]
        user_input = [float(x) for x in user_input]
        liver_prediction = liver_disease_model.predict([user_input])
        if liver_prediction[0] == 1:
            liver_diagnosis = "The person has liver disease"
        else:
            liver_diagnosis = "The person does not have liver disease"
        return render_template('liver.html', diagnosis=liver_diagnosis)
    return render_template('liver.html', diagnosis='')

if __name__ == "__main__":
    app.run(debug=True)
