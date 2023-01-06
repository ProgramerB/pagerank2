from flask import Flask
from flask import request
from flask import render_template
import os
import spider,sprank,spjson
import sqlite3
#import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    temp = 'empty'
    try:
        conn = sqlite3.connect('spider.sqlite')
        cur = conn.cursor()
        cur.execute('''Select url from Webs''')
        for row in cur:
            temp = row[0]
        cur.close()
    except:
        pass
    return render_template("my-form.html",site=temp) # this should be the name of your html file

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
    elif 'spremove' in request.form:
        try:
            conn = sqlite3.connect('spider.sqlite')
            cur = conn.cursor()
            cur.execute('''DROP TABLE Pages''')
            cur.execute('''DROP TABLE Links''')
            cur.execute('''DROP TABLE Webs''')
            conn.commit()
            cur.close()
        except:
            pass
        fhand = open('static/javascript/spider.js', 'w')
        fhand.close()
        print("All tables droped")
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