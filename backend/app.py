from flask import Flask, send_from_directory, request
from pythainlp.tokenize import syllable_tokenize
from pythainlp.spell import correct

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return send_from_directory("static", "index.html")

# API endpoint to tokenize a word into syllables
@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.json
    word = correct(data.get('word'))
    tokenized_syllables = syllable_tokenize(word, engine="dict")
    return {"syllables": tokenized_syllables}

if __name__ == "__main__":
    app.run(debug=True)
