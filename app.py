from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD World!"

@app.route('/version')
def version():
    return "Version 2.0"

@app.route('/info')
def info():
    return jsonify({
        "app": "CICD Demo",
        "version": "2.0",
        "author": "Your Name"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)