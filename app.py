from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/<name>')
def greet(name):
    return f"<h1 style='text-align:center;margin-top:100px;'>Hello, {name}! Akwaaba! <br><a href='/'>Back Home</a></h1>"
if __name__ == '__main__':
    app.run(debug=True)
