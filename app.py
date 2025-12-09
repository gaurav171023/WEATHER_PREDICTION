import os
from flask import Flask, render_template, request, jsonify
import sys
sys.path.insert(0, './tkinter-app')
from calculation import process_inputs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        inputs = [
            data['date'],
            float(data['precipitation']),
            float(data['temp_max']),
            float(data['temp_min']),
            float(data['wind'])
        ]
        result = process_inputs(inputs)
        return jsonify({'weather': str(result)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
