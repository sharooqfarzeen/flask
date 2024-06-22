from flask import Flask, render_template, request, redirect, url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def home():
    return "Homepage"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods = ['GET', 'POST'])
def form():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science)/4
    else:
        return render_template('form.html')
    
    return redirect(url_for('result',score=total_score))

## Variable Rule
@app.route('/result/<int:score>')
def result(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score': score,
           "res":res}

    return render_template('result.html', results = exp)

if __name__ == "__main__":
    app.run(debug = True)