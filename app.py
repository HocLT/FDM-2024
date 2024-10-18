from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title='FDM Final Test', name='FPT Cooking 2024')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)