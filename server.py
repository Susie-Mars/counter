from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dont tell no one!'



@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    else: 
        session['count']+=1
    return render_template("index.html", count=session['count'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/plus', methods=['POST'])
def add_2():
    session['count']+= 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():   
    del session['count']
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)

