import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("name") or not  request.form.get("option") or not  request.form.get("position"):
       return render_template("error.html", message="TODO")

    with open("survey.csv","a") as file:
      write = csv.writer(file)
      write.writerow((request.form.get("name"),request.form.get("option"),request.form.get("position")))
      return redirect("/sheet")

@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv","r") as file:
      if not file:
            return render_template("error.html", message="TODO")

      csvfile=csv.reader(file)

      return render_template("table.html",students = csvfile)
