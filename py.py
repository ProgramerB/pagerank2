from flask import Flask
from flask import request
from flask import render_template
import os
import spider,sprank,spjson
#import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    if text2 =="" or int(text2) < 1:
        text2='5'  
        
    if 'spider' in request.form:
        spider.spider(text1,int(text2))
        sprank.sprank(text2)
        spjson.spjson(int(text2))
        return render_template("table.html")
    elif 'sprank' in request.form:
        sprank.sprank(text2)
        return render_template("table.html")
    elif 'spjson' in request.form:
        spjson.spjson(int(text2))
        return render_template("table.html")

@app.route('/chart')
def chart():
    return render_template("force.html")

@app.route('/rank')
def rank():
    return render_template("rank.html")

@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/weight')
def weight():
    return render_template("weight.html")

    


if __name__ == '__main__':
    app.run()