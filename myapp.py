from flask import *
import json
import os

app = Flask(__name__) 
getlist =[]


@app.route('/')
def index():   
    
    return render_template('index.html')

@app.route('/foo/<name>')
def foo(name):   
     return render_template('index.html', to=name)


@app.route('/whereami')
def whereami():
    return 'Ghana'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home/foo1/<name>')
def foo1(name):
    return render_template('home.html',fro=name)
@app.route('/register')
def reg():
    return render_template('register.html',getlist=getlist)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_todo')
def todo():
    user=request.args.get("user")
    item=request.args.get("item")
    dd=request.args.get("date")
    fin= user + " : added "  + item  + "  " + dd 
    getlist.append(fin)
    return  redirect("/register", code=302)



@app.route('/get_todos')
def getodos():

    resp= Response(json.dumps(getlist))
    resp.headers['Content-Type']= 'application/json'
    return resp

@app.route('/courses')
def course():

    return render_template('courses.html')


if __name__ =='__main__':
     port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0',port=port)