#!python3

from flask import Flask, render_template, request, session, redirect, url_for, escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():	
    if request.method == 'POST' and 'wage' in request.form:
        session['wage'] = float(request.form.get('wage'))
        return redirect(url_for('pay_calc'))
    return render_template("index.html")

@app.route('/pay', methods=['GET', 'POST'])
def pay_calc():
    pay = ''
    if request.method == 'POST' and 'hours' in request.form and 'wage' in session:
        hours = float(request.form.get('hours'))
        pay = calc_wage(session['wage'], hours)
        #pay = (session['wage'] * hours)
    return render_template("pay_calc.html",
                            pay=pay)
						   

def calc_wage(wage, hours):
    return (wage * hours)

app.secret_key = "Test_Secret_Key"
app.run()