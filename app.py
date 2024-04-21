from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load label encoders and imputer
label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))
imputer = pickle.load(open('imputer.pkl', 'rb'))


@app.route('/')
def home():
    return "Hello World"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve data from the form
        S_NO = request.form.get('S_NO')
        CHK_ACCT = str(request.form.get('CHK_ACCT'))
        Duration = int(request.form.get('Duration')) if request.form.get('Duration') else None
        History = request.form.get('History')
        Purposeofcredit = request.form.get('Purposeofcredit')
        CreditAmount = float(request.form.get('CreditAmount')) if request.form.get('CreditAmount') else None
        BalanceinSavingsAC = request.form.get('BalanceinSavingsAC')
        Employment = request.form.get('Employment')
        Install_rate = float(request.form.get('Install_rate')) if request.form.get('Install_rate') else None
        Maritalstatus = request.form.get('Maritalstatus')
        S_No_ = request.form.get('S_NO_')
        Coapplicant = request.form.get('Coapplicant')
        PresentResident = request.form.get('PresentResident')
        RealEstate = request.form.get('RealEstate')
        Age = int(request.form.get('Age')) if request.form.get('Age') else None
        Otherinstallment = request.form.get('Otherinstallment')
        Residence = request.form.get('Residence')
        Num_Credits = int(request.form.get('Num_Credits')) if request.form.get('Num_Credits') else None
        Job = request.form.get('Job')
        Nodependents = int(request.form.get('Nodependents')) if request.form.get('Nodependents') else None
        Phone = request.form.get('Phone')
        Foreign = request.form.get('Foreign')
        Output = request.form.get('Output')

        # Create a DataFrame from the input data
        input_data = {'S_No': S_NO, 'CHK_ACCT': CHK_ACCT, 'Duration': Duration, 'History': History,
                      'Purposeofcredit': Purposeofcredit,
                      'CreditAmount': CreditAmount, 'BalanceinSavingsAC': BalanceinSavingsAC,
                      'Employment': Employment,
                      'Install_rate': Install_rate, 'Maritalstatus': Maritalstatus, 'S_No_': S_No_,
                      'Coapplicant': Coapplicant,
                      'PresentResident': PresentResident, 'RealEstate': RealEstate, 'Age': Age,
                      'Otherinstallment': Otherinstallment,
                      'Residence': Residence, 'Num_Credits': Num_Credits, 'Job': Job, 'Nodependents': Nodependents,
                      'Phone': Phone, 'Foreign': Foreign, 'Output': Output}

        # Create a DataFrame from the input data
        input_df = pd.DataFrame([input_data])

        for col, encoder in label_encoders.items():
            # Check if the column exists in the DataFrame
            if col in input_df.columns:
                encoder_classes = encoder.classes_.tolist()
                if 'unknown' not in encoder_classes:
                    encoder_classes.append('unknown')
                encoder.classes_ = np.array(encoder_classes)

                # Convert input_df[col] to a Series if it's not already one
                input_series = input_df[col].squeeze() if isinstance(input_df[col], pd.DataFrame) else input_df[col]

                # Manually encode values, considering 'unknown'
                input_series_encoded = input_series.apply(
                    lambda x: encoder.transform([x])[0] if x in encoder.classes_ else encoder.transform(['unknown'])[0])

                # Replace original column with encoded values
                input_df[col] = input_series_encoded
            else:
                print(f"Column {col} does not exist in the DataFrame.")

        # Handle missing values using the same Imputer
        input_df_filled = pd.DataFrame(imputer.transform(input_df), columns=input_df.columns)
        # Drop the 'Output' column if present (in case it's accidentally included)
        if 'Output' in input_df_filled.columns:
            input_df_filled.drop('Output', axis=1, inplace=True)

        # Make predictions
        predicted_class = model.predict(input_df_filled)

        return jsonify({'Output': str(predicted_class[0])})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
