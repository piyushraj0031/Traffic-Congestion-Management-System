from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/run_simulation')
def run_simulation():
    try:
        subprocess.run(['python','simulation.py'], check=True)
        return render_template('Success.html')
    except subprocess.CalledProcessError as e:
        return f'Error running simulation: {e}', 500

if __name__ == '__main__':
    app.run(debug=True)
