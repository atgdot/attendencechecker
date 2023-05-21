from flask import Flask, render_template, request, jsonify
import base64
import requests

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('FLASk\templates\index.html')

# API endpoint for capturing the reference photo
@app.route('/capture-reference', methods=['POST'])
def capture_reference():
    data_url = request.form['imageData']
    image_data = base64.b64decode(data_url.split(',')[1])

    # Store the reference photo or send it to your ML server for further processing
    # Replace this code with your logic for storing or processing the reference photo

    return jsonify({'message': 'Reference photo captured.'})

# API endpoint for face verification
@app.route('/verify-face', methods=['POST'])
def verify_face():
    data = request.json
    reference_photo_data = base64.b64decode(data['referencePhoto'].split(',')[1])
    current_photo_data = base64.b64decode(data['currentPhoto'].split(',')[1])

    # Perform face verification using your ML server
    # Replace the URL with the appropriate endpoint of your ML server
    ml_server_url = 'http://your-ml-server/face-verification'
    response = requests.post(ml_server_url, json={'referencePhoto': reference_photo_data, 'currentPhoto': current_photo_data})

    if response.status_code == 200:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({'error': 'Face verification failed.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
