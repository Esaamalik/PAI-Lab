from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for mentors
mentors = [
    {"name": "Dr. Essa", "specialty": "Cardiologist", "email": "essa123@medi.com"},
    {"name": "Dr. Sami", "specialty": "Dermatologist", "email": "sami667@medi.com"},
    {"name": "Dr. John", "specialty": "Psychologist", "email": "johncena@medi.com"},
]

# Sickness to treatment mapping
health_advice = {
    "cold": "Rest, drink warm fluids, and take vitamin C.",
    "flu": "Stay hydrated, rest, and take antiviral medication if prescribed.",
    "diabetes": "Monitor blood sugar levels, avoid sugar, and exercise regularly.",
    "hypertension": "Reduce salt intake, avoid stress, and exercise.",
    "asthma": "Use inhalers, avoid allergens, and keep air clean.",
    "headache": "Rest in a dark room, drink water, and take pain relief if needed.",
    "stomach ache": "Avoid spicy food, eat light meals, and stay hydrated.",
}

@app.route('/', methods=["GET", "POST"])
def index():
    advice = None
    if request.method == "POST":
        sickness = request.form.get("sickness", "").lower().strip()
        advice = health_advice.get(sickness, "Sorry, we don't have advice for that sickness.")
    return render_template("index.html", advice=advice)

@app.route('/mentors')
def show_mentors():
    return render_template("mentors.html", mentors=mentors)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        print(f"Message received from {name}: {message}")
        return redirect(url_for('index'))
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
