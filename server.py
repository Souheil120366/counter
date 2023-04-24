from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' 

count=0
@app.route('/')         
def index():
    if "counter" not in session:
        session['counter']=0
    else:
        session['counter']=str(int(session['counter'])+1)    
    
    return render_template("index.html")

@app.route('/destroy_session')         
def dest_session():
    session.clear()
    return redirect("/")

@app.route('/<int:times>')         
def counter_2(times):
    if "counter" not in session:
        session['counter']=0
    else:
        session['counter']=str(int(session['counter'])+times-1)    
    
    return redirect("/")

@app.route('/counterstep', methods=['POST'])         
def counter_step():
    session['counterstep']=request.form['counterstep']
    if "counter" not in session:
        session['counter']=0
    else:
        session['counter']=str(int(session['counter'])+int(session['counterstep'])-1)    
    
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)    