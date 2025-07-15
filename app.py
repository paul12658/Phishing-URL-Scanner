# import necessary libraries
from flask import Flask, render_template, request
from scanner import scan_url

# used for creating the Flask web application
app = Flask(__name__)

# used for rendering HTML templates and handling HTTP requests
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    heuristics = {}
    flagged_by_google = False

    if request.method == "POST":
        url = request.form["url"]
        heuristics, flagged_by_google = scan_url(url)
        result = {
            "url": url,
            "heuristics": heuristics,
            "flagged_by_google": flagged_by_google
        }

    return render_template("index.html", result=result)
# renders the index.html template with the scan results
if __name__ == "__main__":
    app.run(debug=True)
