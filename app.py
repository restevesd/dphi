from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from pycaret.classification import * 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example(): 
    css = "static/css/style.css"
    
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
        output = predict_model(model,input_df)
        print(output)
        score = output.Score * 100
        if str(output.Label[0]) == "1":
            a = ("Loan Granted - Score: " + str(score[0])) +"%"
        else:
            a = ("Loan NOT Granted - Score: " + str(score[0])) +"%"
        
        return '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Documento sin título</title>
<link rel="stylesheet" href="{}">
</head>

<body>
 	
<div class="container"> 
<form id="contact" name="form1" method="post">
  <h1 align="center"><strong>Loan Application</strong> Result</h1>
  <p><br>
				<fieldset>
               <h2  align="center">{}<h2>
			</fieldset>
</form>
	
</div>

</body>
</html>
'''.format(css,a) 

    return '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Documento sin título</title>
<link rel="stylesheet" href="{}">
</head>

<body>
 	
<div class="container"> 
<form id="contact" name="form1" method="post">
  <h2 align="center"><strong>Loan Application</strong></h2>
				<fieldset>
				Gender:
				<select name="gender" id="gender">
					<option value="Male">Male</option>
					<option value="Female">Female</option>
				</select>
			</fieldset>
	
				<fieldset>
				Married:
				<select name="married" id="married">
					<option value="Yes">Yes</option>
					<option value="No">No</option>
        </select>
				</fieldset>
	
				<fieldset>
				Dependents:
				<select name="dependents" id="dependents">
					<option value="0">0</option>
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="+3">+3</option>
				</select>
				</fieldset>
				<fieldset>
				Education:
				<select name="education" id="education">
					<option value="Graduated">Graduated</option>
					<option value="Not Graduated">Not Graduated</option>
				</select>
			</fieldset>
	<fieldset>
			Self Emplyed:
			<select name="selfe" id="selfe">
				<option value="Yes">Yes</option>
				<option value="No">No</option>
			</select>
			</fieldset>
	<hr>
	<br>
	<fieldset>	
			<input placeholder="Income" type="text" name="income" id="income">
			</fieldset>
	<fieldset>	<input placeholder="CoApplication Income:" type="text" name="coincome" id="coincome">
			</fieldset>
				<fieldset>
				<input type="text" name="loan" id="loan" placeholder="Loan Amount:">
			</fieldset>
	<br>
	<hr>
				<fieldset>	Loan Amount Term:
				<select name="term" id="term">
          <option value="30" selected="selected">30</option>
          <option value="60">60</option>
          <option value="90">90</option>
          <option value="120">120</option>
          <option value="180">180</option>
          <option value="360">360</option>
          <option value="720">720</option>
        </select>
				</fieldset>
	
				<fieldset>Credit History:<br>
				<label>
					<input type="radio" name="history" value="1" id="history_0">Yes
				</label><br>
				<label>
					<input type="radio" name="history" value="0" id="history">No
				</label>
			</fieldset>
	
				<fieldset>
				Property Area:
				<select name="property" id="property">
				<option value="Rural">Rural</option>
				<option value="Semiurban">Semiurban</option>
				<option value="Urban">Urban</option>
       			</select>
			</fieldset>
	
	<button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Submit</button>
</form>
	
</div>

</body>
</html>
'''.format(css)

if __name__ == '__main__':
  app.run(host ='0.0.0.0', debug=False)