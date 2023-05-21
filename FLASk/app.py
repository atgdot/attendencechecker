from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'html element to be returned'

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>the result is passed</h1></body></html"

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and the marks is"+ str(score)

##result checker
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result= 'fail'
    else:
        result= 'success'
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app.run(debug=True)  