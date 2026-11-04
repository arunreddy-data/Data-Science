## Building URL Dynamically.
## Variable Rule
## Jinja2 Template Engine

## Jinja2 Template Engine
"""
{{  }} Expressions to print output in html
{%.....%} conditions, for loops
{#....#} this is for comments
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def welcome():
    return "Get Method..."


# Variable Rule.
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template("result.html", results=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {"score": score, "res": res}
    return render_template("result1.html", results=exp)


if __name__ == "__main__":
    app.run(debug=True)
