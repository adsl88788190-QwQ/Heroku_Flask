from flask import Flask
from flask import request, jsonify
import json

if __name__ == '__main__':
    print('Start ^^')
    app.run()

@app.route('/')
def index():
    return 'Hello, World!'