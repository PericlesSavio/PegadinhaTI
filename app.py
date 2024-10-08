from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

pegadinhas = {
    'item1': False,
    'item2': False,
    'item3': False,
    'item4': False
}

@app.route('/pegadinha', methods=['GET'])
def get_pegadinhas():
    return jsonify(pegadinhas)

@app.route('/pegadinha', methods=['POST'])
def set_pegadinha():
    global pegadinhas
    data = request.get_json()
    
    if all(key in pegadinhas for key in data):
        pegadinhas.update(data)
        return jsonify(pegadinhas), 200
    else:
        return jsonify({'error': 'Chaves não permitidas no payload'}), 400

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
