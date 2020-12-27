from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from pycaret.classification import * 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():    
    if request.method == 'POST':  #this block is only entered when the form is submitted
        gender = request.form.get('gender')
        married = request.form['married']
        depen = request.form["dependents"]
        education = request.form["education"]
        selfe = request.form["selfe"]
        income = request.form["income"]
        cincome = request.form["coincome"]
        loan = request.form["loan"]
        term = request.form["term"]
        history = request.form["history"]
        area = request.form["property"]
 
        
        input_dict = {'Gender' : gender, 'Married' : married, 'Dependents' : depen,
                      'Education' : education, 'Self_Employed' : selfe,'ApplicantIncome':income,
                      'CoapplicantIncome' : cincome,'LoanAmount':loan,'Loan_Amount_Term':term,
                      'Credit_History':history,'Property_Area':area}
        input_df = pd.DataFrame([input_dict])
        
        model = load_model('best-model') 
        output = predict_model(model,input_df,round = 0)
        if str(output.Label[0]) == "1":
            a = ("Loan Granted {}".format(output.Label[0]))
        else:
            a = ("Loan NOT Granted {}".format(output.Label[0]))
        
        return '''<H1>{}</H1> '''.format(a) 

    return '''<form id="form1" name="form1" method="post">
  <h2 align="center"><strong>Loan Application</strong></h2>
  <table width="80%" border="0" align="center" cellpadding="5">
    <tbody>
      <tr>
        <td align="right"><label for="gender">Gender:</label></td>
        <td><select name="gender" id="gender">
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select></td>
      </tr>
      <tr>
        <td align="right"><label for="married3">Married:</label></td>
        <td><select name="married" id="married">
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select></td>
      </tr>
      <tr>
        <td align="right"><label for="dependents3">Dependents:</label></td>
        <td><select name="dependents" id="dependents">
          <option value="0">0</option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="+3">+3</option>
        </select></td>
      </tr>
      <tr>
        <td align="right"><label for="education3">Education:</label></td>
        <td><select name="education" id="education">
          <option value="Graduated">Graduated</option>
          <option value="Not Graduated">Not Graduated</option>
        </select></td>
      </tr>
      <tr>
        <td align="right"><label for="selfe3">Self Emplyed:</label></td>
        <td><select name="selfe" id="selfe">
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select></td>
      </tr>
      <tr>
        <td align="right"><label for="income3">Income:</label></td>
        <td><input type="text" name="income" id="income"></td>
      </tr>
      <tr>
        <td align="right"><label for="coincome3">CoApplication Income:</label></td>
        <td><input type="text" name="coincome" id="coincome"></td>
      </tr>
      <tr>
        <td align="right"><label for="loan3">Loan Amount:</label></td>
        <td><input type="text" name="loan" id="loan"></td>
      </tr>
      <tr>
        <td align="right"><label for="term3">Loan Amount Term:</label></td>
        <td><select name="term" id="term">
          <option value="30" selected="selected">30</option>
          <option value="60">60</option>
          <option value="90">90</option>
          <option value="120">120</option>
          <option value="180">180</option>
          <option value="360">360</option>
          <option value="720">720</option>
        </select></td>
      </tr>
      <tr>
        <td align="right">Credit History:</td>
        <td><label>
          <input type="radio" name="history" value="1" id="history_0">
          Yes</label>
          <br>
          <label>
            <input type="radio" name="history" value="0" id="history_1">
            No</label></td>
      </tr>
      <tr>
        <td align="right"><label for="property3">Property Area:</label></td>
        <td><select name="property" id="property">
          <option value="Rural">Rural</option>
          <option value="Semiurban">Semiurban</option>
          <option value="Urban">Urban</option>
        </select></td>
      </tr>
      <tr>
        <td colspan="2" align="center"><input type="submit" name="submit" id="submit" value="Submit"></td>
      </tr>
    </tbody>
  </table>
</form>'''

if __name__ == '__main__':
  app.run(host ='0.0.0.0', debug=False)