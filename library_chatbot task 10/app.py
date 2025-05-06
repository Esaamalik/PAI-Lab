from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample fixed responses
responses = {
    "what are the library timings": "The library is open from 9 AM to 5 PM, Monday to Saturday.",
    "how to get a library card": "You can get a library card by filling out a form at the reception with a valid ID.",
    "what is the fine for late return": "The fine is Rs. 5 per day after the due date.",
    "do you have books on python": "Yes, we have a variety of Python programming books in the technology section.",
    "where is the fiction section": "The fiction section is on the first floor, to the right of the staircase."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def chatbot_response():
    user_input = request.args.get("msg").lower()
    reply = responses.get(user_input, "Sorry, I don't have an answer to that. Please ask something else.")
    return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)
