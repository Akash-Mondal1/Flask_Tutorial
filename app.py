from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello this is home'

@app.route('/home')
def home():
    return "Hello welcome Home..!!"

# Dynamic url

@app.route('/success/<int:marks>')
def pas(marks):
    return 'The guy is pass at '+ str(marks)

@app.route('/fail/<int:marks>')
def fail(marks):
    return 'The guy is failed at marks '+ str(marks)

@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks>50:
        result= 'pas'
    else:
        result= 'fail'
    return redirect(url_for(result,marks=marks))

if __name__=='__main__':
    app.run(debug=True)