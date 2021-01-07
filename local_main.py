from flask import Flask, render_template, request
import requests
import jsonify
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__, template_folder = 'templates')
model = pickle.load(open(r'C:\Users\Brajesh Mohapatra\Python\Mental Health Prediction\mental_health_prediction.pkl', 'rb'))
@app.route('/', methods = ['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        name = str(request.form['aa'])
        age = int(request.form['ab'])
        gender = request.form['ac']
        if gender == 'Male':
            gender_male = 1
            gender_female = 0
            gender_other = 0
        elif gender == 'Female':
            gender_male = 0
            gender_female = 1
            gender_other = 0
        else:
            gender_male = 0
            gender_female = 0
            gender_other = 1
        race = str(request.form['ad'])
        location = str(request.form['ae'])
        question_6 = request.form['af']
        if question_6 == 'Yes':
            question_6 = 1
        else:
            question_6 = 0
        question_7 = request.form['ag']
        if question_7 == '1-5':
            question_7_1_5 = 1
            question_7_6_25 = 0
            question_7_26_100 = 0
            question_7_100_500 = 0
            question_7_500_1000 = 0
            question_7_more_than_1000 = 0
        elif question_7 == '6-25':
            question_7_1_5 = 0
            question_7_6_25 = 1
            question_7_26_100 = 0
            question_7_100_500 = 0
            question_7_500_1000 = 0
            question_7_more_than_1000 = 0
        elif question_7 == '26-100':
            question_7_1_5 = 0
            question_7_6_25 = 0
            question_7_26_100 = 1
            question_7_100_500 = 0
            question_7_500_1000 = 0
            question_7_more_than_1000 = 0
        elif question_7 == '100-500':
            question_7_1_5 = 0
            question_7_6_25 = 0
            question_7_26_100 = 0
            question_7_100_500 = 1
            question_7_500_1000 = 0
            question_7_more_than_1000 = 0
        elif question_7 == '500-1000':
            question_7_1_5 = 0
            question_7_6_25 = 0
            question_7_26_100 = 0
            question_7_100_500 = 0
            question_7_500_1000 = 1
            question_7_more_than_1000 = 0
        else:
            question_7_1_5 = 0
            question_7_6_25 = 0
            question_7_26_100 = 0
            question_7_100_500 = 0
            question_7_500_1000 = 0
            question_7_more_than_1000 = 1
        question_8 = request.form['ah']
        if question_8 == 'Yes':
            question_8 = 1
        else:
            question_8 = 0
        question_9 = request.form['ai']
        if question_9 == 'Yes':
            question_9 = 1
        else:
            question_9 = 0
        question_10 = request.form['aj']
        if question_10 == 'Yes':
            question_10_yes = 1
            question_10_no = 0
            question_10_dk = 0
            question_10_na = 0
        elif question_10 == 'No':
            question_10_yes = 0
            question_10_no = 1
            question_10_dk = 0
            question_10_na = 0
        elif question_10 == 'Don\'t Know':
            question_10_yes = 0
            question_10_no = 0
            question_10_dk = 1
            question_10_na = 0
        else:
            question_10_yes = 0
            question_10_no = 0
            question_10_dk = 0
            question_10_na = 1
        question_11 = request.form['ak']
        if question_11 == 'Yes':
            question_11_yes = 1
            question_11_no = 0
            question_11_ns = 0
        elif question_11 == 'No':
            question_11_yes = 0
            question_11_no = 1
            question_11_ns = 0
        else:
            question_11_yes = 0
            question_11_no = 0
            question_11_ns = 1
        question_12 = request.form['al']
        if question_12 == 'Yes':
            question_12_yes = 1
            question_12_no = 0
            question_12_dk = 0
        elif question_12 == 'No':
            question_12_yes = 0
            question_12_no = 1
            question_12_dk = 0
        else:
            question_12_yes = 0
            question_12_no = 0
            question_12_dk = 1
        question_13 = request.form['am']
        if question_13 == 'Yes':
            question_13_yes = 1
            question_13_no = 0
            question_13_dk = 0
        elif question_13 == 'No':
            question_13_yes = 0
            question_13_no = 1
            question_13_dk = 0
        else:
            question_13_yes = 0
            question_13_no = 0
            question_13_dk = 1
        question_14 = request.form['an']
        if question_14 == 'Yes':
            question_14_yes = 1
            question_14_no = 0
            question_14_dk = 0
        elif question_14 == 'No':
            question_14_yes = 0
            question_14_no = 1
            question_14_dk = 0
        else:
            question_14_yes = 0
            question_14_no = 0
            question_14_dk = 1
        question_15 = request.form['ao']
        if question_15 == 'Very easy':
            question_15_ve = 1
            question_15_se = 0
            question_15_nend = 0
            question_15_sd = 0
            question_15_d = 0
            question_15_vd = 0
            question_15_dk = 0
        elif question_15 == 'Somewhat easy':
            question_15_ve = 0
            question_15_se = 1
            question_15_nend = 0
            question_15_sd = 0
            question_15_d = 0
            question_15_vd = 0
            question_15_dk = 0
        elif question_15 == 'Neither easy nor difficult':
            question_15_ve = 0
            question_15_se = 0
            question_15_nend = 1
            question_15_sd = 0
            question_15_d = 0
            question_15_vd = 0
            question_15_dk = 0
        elif question_15 == 'Somewhat difficult':
            question_15_ve = 0
            question_15_se = 0
            question_15_nend = 0
            question_15_sd = 1
            question_15_d = 0
            question_15_vd = 0
            question_15_dk = 0
        elif question_15 == 'Difficult':
            question_15_ve = 0
            question_15_se = 0
            question_15_nend = 0
            question_15_sd = 0
            question_15_d = 1
            question_15_vd = 0
            question_15_dk = 0
        elif question_15 == 'Very difficult':
            question_15_ve = 0
            question_15_se = 0
            question_15_nend = 0
            question_15_sd = 0
            question_15_d = 0
            question_15_vd = 1
            question_15_dk = 0
        else:
            question_15_ve = 0
            question_15_se = 0
            question_15_nend = 0
            question_15_sd = 0
            question_15_d = 0
            question_15_vd = 0
            question_15_dk = 1
        question_16 = request.form['ap']
        if question_16 == 'Physical health':
            question_16_ph = 1
            question_16_mh = 0
            question_16_slc = 0
        elif question_16 == 'Mental health':
            question_16_ph = 0
            question_16_mh = 1
            question_16_slc = 0
        else:
            question_16_ph = 0
            question_16_mh = 0
            question_16_slc = 1
        question_17 = request.form['aq']
        if question_17 == 'Yes':
            question_17_yes = 1
            question_17_no = 0
            question_17_mb = 0
        elif question_17 == 'No':
            question_17_yes = 0
            question_17_no = 1
            question_17_mb = 0
        else:
            question_17_yes = 0
            question_17_no = 0
            question_17_mb = 1
        question_18 = request.form['ar']
        if question_18 == 'Yes':
            question_18 = 1
        else:
            question_18 = 0
        question_19 = request.form['as']
        if question_19 == 'Yes':
            question_19_yes = 1
            question_19_no = 0
            question_19_mb = 0
        elif question_19 == 'No':
            question_19_yes = 0
            question_19_no = 1
            question_19_mb = 0
        else:
            question_19_yes = 0
            question_19_no = 0
            question_19_mb = 1
        question_20 = request.form['at']
        if question_20 == 'Yes':
            question_20 = 1
        else:
            question_20 = 0
        question_21 = request.form['au']
        if question_21 == 'Yes':
            question_21 = 1
        else:
            question_21 = 0
        question_22 = request.form['av']
        if question_22 == '1':
            question_22 = 1
        elif question_22 == '2':
            question_22 = 2
        elif question_22 == '3':
            question_22 = 3
        elif question_22 == '4':
            question_22 = 4
        elif question_22 == '5':
            question_22 = 5
        elif question_22 == '6':
            question_22 = 6
        elif question_22 == '7':
            question_22 = 7
        elif question_22 == '8':
            question_22 = 8
        elif question_22 == '9':
            question_22 = 9
        else:
            question_22 = 10
        question_23 = request.form['aw']
        if question_23 == '1':
            question_23 = 1
        elif question_23 == '2':
            question_23 = 2
        elif question_23 == '3':
            question_23 = 3
        elif question_23 == '4':
            question_23 = 4
        elif question_23 == '5':
            question_23 = 5
        elif question_23 == '6':
            question_23 = 6
        elif question_23 == '7':
            question_23 = 7
        elif question_23 == '8':
            question_23 = 8
        elif question_23 == '9':
            question_23 = 9
        else:
            question_23 = 10
        question_24 = request.form['ax']
        if question_24 == 'Yes':
            question_24 = 1
        else:
            question_24 = 0
        question_25 = request.form['ay']
        if question_25 == 'Yes':
            question_25_yes = 1
            question_25_no = 0
            question_25_mb = 0
            question_25_dk = 0
        elif question_25 == 'No':
            question_25_yes = 0
            question_25_no = 1
            question_25_mb = 0
            question_25_dk = 0
        elif question_25 == 'Maybe':
            question_25_yes = 0
            question_25_no = 0
            question_25_mb = 1
            question_25_dk = 0
        else:
            question_25_yes = 0
            question_25_no = 0
            question_25_mb = 0
            question_25_dk = 1
        question_26 = request.form['az']
        if question_26 == 'Yes':
            question_26_yes = 1
            question_26_no = 0
            question_26_mb = 0
            question_26_dk = 0
        elif question_26 == 'No':
            question_26_yes = 0
            question_26_no = 1
            question_26_mb = 0
            question_26_dk = 0
        elif question_26 == 'Maybe':
            question_26_yes = 0
            question_26_no = 0
            question_26_mb = 1
            question_26_dk = 0
        else:
            question_26_yes = 0
            question_26_no = 0
            question_26_mb = 0
            question_26_dk = 1
        question_27 = request.form['ba']
        if question_27 == 'Yes':
            question_27 = 1
        else:
            question_27 = 0
        question_28 = request.form['bb']
        if question_28 == 'Yes':
            question_28_yes = 1
            question_28_no = 0
            question_28_dk = 0
        elif question_28 == 'No':
            question_28_yes = 0
            question_28_no = 1
            question_28_dk = 0
        else:
            question_28_yes = 0
            question_28_no = 0
            question_28_dk = 1
        question_29 = request.form['bc']
        if question_29 == 'Often':
            question_29_o = 1
            question_29_s = 0
            question_29_r = 0
            question_29_n = 0
            question_29_na = 0
        elif question_29 == 'Sometimes':
            question_29_o = 0
            question_29_s = 1
            question_29_r = 0
            question_29_n = 0
            question_29_na = 0
        elif question_29 == 'Rarely':
            question_29_o = 0
            question_29_s = 0
            question_29_r = 1
            question_29_n = 0
            question_29_na = 0
        elif question_29 == 'Never':
            question_29_o = 0
            question_29_s = 0
            question_29_r = 0
            question_29_n = 1
            question_29_na = 0
        else:
            question_29_o = 0
            question_29_s = 0
            question_29_r = 0
            question_29_n = 0
            question_29_na = 1
        question_30 = request.form['bd']
        if question_30 == 'Often':
            question_30_o = 1
            question_30_s = 0
            question_30_r = 0
            question_30_n = 0
            question_30_na = 0
        elif question_30 == 'Sometimes':
            question_30_o = 0
            question_30_s = 1
            question_30_r = 0
            question_30_n = 0
            question_30_na = 0
        elif question_30 == 'Rarely':
            question_30_o = 0
            question_30_s = 0
            question_30_r = 1
            question_30_n = 0
            question_30_na = 0
        elif question_30 == 'Never':
            question_30_o = 0
            question_30_s = 0
            question_30_r = 0
            question_30_n = 1
            question_30_na = 0
        else:
            question_30_o = 0
            question_30_s = 0
            question_30_r = 0
            question_30_n = 0
            question_30_na = 1
        question_31 = request.form['be']
        if question_31 == 'Yes':
            question_31_yes = 1
            question_31_no = 0
            question_31_mb = 0
        elif question_31 == 'No':
            question_31_yes = 0
            question_31_no = 1
            question_31_mb = 0
        else:
            question_31_yes = 0
            question_31_no = 0
            question_31_mb = 1
        question_32 = request.form['bf']
        if question_32 == 'Yes':
            question_32_yes = 1
            question_32_no = 0
            question_32_mb = 0
        elif question_32 == 'No':
            question_32_yes = 0
            question_32_no = 1
            question_32_mb = 0
        else:
            question_32_yes = 0
            question_32_no = 0
            question_32_mb = 1
        question_33 = request.form['bg']
        if question_33 == 'Yes':
            question_33_yes = 1
            question_33_no = 0
            question_33_mb = 0
        elif question_33 == 'No':
            question_33_yes = 0
            question_33_no = 1
            question_33_mb = 0
        else:
            question_33_yes = 0
            question_33_no = 0
            question_33_mb = 1
        question_34 = request.form['bh']
        if question_34 == 'Yes':
            question_34 = 1
        else:
            question_34 = 0
        entries = np.array([question_29_na, question_25_yes, question_27, question_29_s, question_29_r, question_26_yes, 
                            question_25_mb, question_28_no, question_25_no, question_28_yes, question_30_o, question_29_o, 
                            age, question_30_na, question_30_s, question_26_no, question_10_yes, gender_male, question_26_mb, 
                            question_15_dk, question_15_nend])
        entries = entries.reshape(1, -1)
        prediction = model.predict_proba(entries)
        output = prediction[0][1] * 100
        output = output.round(decimals = 0)
        return render_template('index.html', prediction_text = "{}, you have {}% chance of suffering from Mental Health Disorder".format(name, output))
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug = True)