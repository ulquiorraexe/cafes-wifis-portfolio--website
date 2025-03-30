from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean
import sqlite3

app = Flask(__name__)
# Veritabanı dosyasına bağlan
conn = sqlite3.connect('instance/cafes.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM cafe')
rows = cursor.fetchall()
conn.close()

@app.route("/")
def home():
    return render_template("index.html", table=rows)

@app.route("/generic")
def generic():
    return render_template("generic.html", table=rows)

@app.route("/elements")
def element():
    return render_template("elements.html")

@app.route("/one")
def one():
    return render_template("1.html", table=rows)

@app.route("/two")
def two():
    return render_template("2.html", table=rows)

@app.route("/three")
def three():
    return render_template("3.html", table=rows)

@app.route("/four")
def four():
    return render_template("4.html", table=rows)

@app.route("/five")
def five():
    return render_template("5.html", table=rows)

@app.route("/six")
def six():
    return render_template("6.html", table=rows)

@app.route("/seven")
def seven():
    return render_template("7.html", table=rows)

@app.route("/eight")
def eight():
    return render_template("8.html", table=rows)

@app.route("/nine")
def nine():
    return render_template("9.html", table=rows)

@app.route("/ten")
def ten():
    return render_template("10.html", table=rows)

@app.route("/eleven")
def eleven():
    return render_template("11.html", table=rows)

@app.route("/twelve")
def twelve():
    return render_template("12.html", table=rows)

@app.route("/thirteen")
def thirteen():
    return render_template("13.html", table=rows)

@app.route("/fourteen")
def fourteen():
    return render_template("14.html", table=rows)

@app.route("/fifteen")
def fifteen():
    return render_template("15.html", table=rows)

@app.route("/sixteen")
def sixteen():
    return render_template("16.html", table=rows)

@app.route("/seventeen")
def seventeen():
    return render_template("17.html", table=rows)

@app.route("/eighteen")
def eighteen():
    return render_template("18.html", table=rows)

@app.route("/nineteen")
def nineteen():
    return render_template("19.html", table=rows)

@app.route("/twenty")
def twenty():
    return render_template("20.html", table=rows)

@app.route("/twenty-one")
def twenty_one():
    return render_template("21.html", table=rows)
if __name__ == "__main__":
    app.run(debug=True, port=5002)