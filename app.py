# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')  # Shows a welcome page

# Route for handling form submission
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greet.html', name=name)  # Show greeting page
    return render_template('form.html')  # Show form page

if __name__ == '__main__':
    app.run(debug=True)
