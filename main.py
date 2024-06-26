from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running on port 8000!"

@app.route('/age', methods=['GET'])
def age():
    param_age = request.args.get('age')
    if param_age:
        return f"Your age is: {param_age}"
    else:
        return "Please provide an age parameter."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)