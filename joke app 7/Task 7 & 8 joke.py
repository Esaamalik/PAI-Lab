from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(joke_url)
    
    if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data.get("setup")
        punchline = joke_data.get("punchline")
    else:
        setup = "Oops! Couldn't fetch a joke."
        punchline = ""

    return render_template('index.html', setup=setup, punchline=punchline)

if __name__ == '__main__':
    app.run(debug=True)
