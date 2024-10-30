

# # Existing imports
# from flask import Flask, request, jsonify, render_template
# from werkzeug.utils import secure_filename
# from keras.preprocessing import image
# from keras.models import load_model
# import numpy as np
# import os

# app = Flask(__name__)

# # Define a directory to save uploaded images
# UPLOAD_FOLDER = 'uploads_for_prediction'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Load the model globally to avoid reloading it for each request
# model = load_model('cnn_model.h5')  # Replace with your actual model path

# # Prediction function
# def predict(image_path):
#     target_size = (150, 150)
#     img = image.load_img(image_path, target_size=target_size, color_mode="grayscale")
#     img_array = np.array(img) / 255.0
#     img_array = img_array.reshape(-1, 150, 150, 1)

#     predictions = model.predict(img_array)
#     confidence = predictions[0][0]

#     predicted_class = 0 if confidence >= 0.5 else 1
#     label = "Pneumonia" if predicted_class == 0 else "Normal"
#     return {"predicted_class": predicted_class, "confidence": float(confidence), "label": label}

# # Route to upload image and call prediction
# @app.route('/', methods=['GET', 'POST'])
# def upload_and_predict():
#     if request.method == 'POST':
#         if 'image' not in request.files:
#             return jsonify({"error": "No image part in the request"}), 400
#         file = request.files['image']
#         if file.filename == '':
#             return jsonify({"error": "No selected file"}), 400

#         if file:
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)

#             # Call the predict function
#             prediction = predict(file_path)

#             # Return the prediction result as JSON
#             return jsonify(prediction)

#     return '''
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Lung Cancer Detection</title>
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }
#         body {
#             font-family: Arial, sans-serif;
#             background: url('logo.jpeg') no-repeat center center fixed;
#             background-size: cover;
#             width: 100%;
#             height: 100vh;
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             color: #333;
#         }
#         .hidden { display: none; }
#         .centered-container {
#             text-align: center;
#             background-color: rgba(255, 255, 255, 0.8);
#             padding: 30px;
#             border-radius: 12px;
#             box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
#             width: 80%;
#             max-width: 500px;
#         }
#         input[type="text"], input[type="password"], input[type="file"], button {
#             width: 100%;
#             padding: 12px;
#             margin: 10px 0;
#             border-radius: 5px;
#             border: 1px solid #ccc;
#         }
#         button {
#             background-color: #0066cc;
#             color: white;
#             cursor: pointer;
#         }
#         button:hover { background-color: #005bb5; }
#         .result { margin-top: 20px; font-weight: bold; }
#     </style>
# </head>
# <body>
#     <!-- Welcome Section -->
#     <div id="welcome-section" class="centered-container">
#         <h1>Welcome</h1>
#         <h2>SwasaRakshaka</h2>
#         <form id="login-form" onsubmit="showDetectionInterface(event)">
#             <input type="text" id="username" name="username" placeholder="Username" required>
#             <input type="password" id="password" name="password" placeholder="Password" required>
#             <button type="submit">Login</button>
#         </form>
#     </div>

#     <!-- Detection Interface Section -->
#     <div id="detection-section" class="centered-container hidden">
#         <h2>Lung Cancer Detection using CNN</h2>
#         <p>Upload X-ray image.</p>
#         <form class="upload-form" method="post" enctype="multipart/form-data" onsubmit="uploadImage(event)">
#             <input type="file" name="image" accept="image/*" required>
#             <button type="submit">Upload & Detect</button>
#         </form>
#         <div id="result" class="result"></div>
#     </div>

#     <script>
#         // Function to handle login and display the detection interface
#         function showDetectionInterface(event) {
#             event.preventDefault();
#             const username = document.getElementById('username').value;
#             const password = document.getElementById('password').value;

#             // Here you can add authentication logic if needed
#             if (username && password) {
#                 document.getElementById('welcome-section').classList.add('hidden');
#                 document.getElementById('detection-section').classList.remove('hidden');
#             } else {
#                 alert('Please enter valid credentials.');
#             }
#         }

#         // Function to upload image and get prediction
#         async function uploadImage(event) {
#             event.preventDefault(); // Prevent form submission
#             const form = event.target;
#             const formData = new FormData(form);
#             const resultDiv = document.getElementById("result");

#             // Call your Flask prediction endpoint
#             const response = await fetch(form.action, {
#                 method: 'POST',
#                 body: formData,
#             });
#             const prediction = await response.json();

#             // Display result based on predicted_class
#             resultDiv.innerHTML = prediction.predicted_class === 0 
#                 ? "Result: Negative (Normal)" 
#                 : "Result: Positive (Pneumonia leading to Lung Cancer)";
#         }
#     </script>
# </body>
# </html>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True)


# Existing imports
# from flask import Flask, request, jsonify, render_template
# from werkzeug.utils import secure_filename
# from keras.preprocessing import image
# from keras.models import load_model
# import numpy as np
# import os

# app = Flask(__name__)

# # Define a directory to save uploaded images
# UPLOAD_FOLDER = 'uploads_for_prediction'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Load the model globally to avoid reloading it for each request
# model = load_model('cnn_model.h5')  # Replace with your actual model path

# # Prediction function
# def predict(image_path):
#     target_size = (150, 150)
#     img = image.load_img(image_path, target_size=target_size, color_mode="grayscale")
#     img_array = np.array(img) / 255.0
#     img_array = img_array.reshape(-1, 150, 150, 1)

#     predictions = model.predict(img_array)
#     confidence = predictions[0][0]

#     predicted_class = 0 if confidence >= 0.5 else 1
#     label = "Pneumonia" if predicted_class == 0 else "Normal"
#     return {"predicted_class": predicted_class, "confidence": float(confidence), "label": label}

# # Route to upload image and call prediction
# @app.route('/', methods=['GET', 'POST'])
# def upload_and_predict():
#     if request.method == 'POST':
#         if 'image' not in request.files:
#             return jsonify({"error": "No image part in the request"}), 400
#         file = request.files['image']
#         if file.filename == '':
#             return jsonify({"error": "No selected file"}), 400

#         if file:
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)

#             # Call the predict function
#             prediction = predict(file_path)

#             # Return the prediction result as JSON
#             return jsonify(prediction)

#     return '''
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Lung Cancer Detection</title>
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }
#         body {
#             font-family: Arial, sans-serif;
#             background: url('logo.jpeg') no-repeat center center fixed;
#             background-size: cover;
#             width: 100%;
#             height: 100vh;
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             color: #333;
#         }
#         .hidden { display: none; }
#         .centered-container {
#             text-align: center;
#             background-color: rgba(255, 255, 255, 0.8);
#             padding: 30px;
#             border-radius: 12px;
#             box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
#             width: 80%;
#             max-width: 500px;
#         }
#         input[type="text"], input[type="password"], input[type="file"], button {
#             width: 100%;
#             padding: 12px;
#             margin: 10px 0;
#             border-radius: 5px;
#             border: 1px solid #ccc;
#         }
#         button {
#             background-color: #0066cc;
#             color: white;
#             cursor: pointer;
#         }
#         button:hover { background-color: #005bb5; }
#         .result { margin-top: 20px; font-weight: bold; }
#     </style>
# </head>
# <body>
#     <!-- Welcome Section -->
#     <div id="welcome-section" class="centered-container">
#         <h1>Welcome</h1>
#         <h2>SwasaRakshaka</h2>
#         <form id="login-form" onsubmit="showDetectionInterface(event)">
#             <input type="text" id="username" name="username" placeholder="Username" required>
#             <input type="password" id="password" name="password" placeholder="Password" required>
#             <button type="submit">Login</button>
#         </form>
#     </div>

#     <!-- Detection Interface Section -->
#     <div id="detection-section" class="centered-container hidden">
#         <h2>Lung Cancer Detection using CNN</h2>
#         <p>Upload X-ray image.</p>
#         <form class="upload-form" method="post" enctype="multipart/form-data" onsubmit="uploadImage(event)">
#             <input type="file" name="image" accept="image/*" required>
#             <button type="submit">Upload & Detect</button>
#         </form>
#         <div id="result" class="result"></div>
#     </div>

#     <script>
#         // Function to handle login and display the detection interface
#         function showDetectionInterface(event) {
#             event.preventDefault();
#             const username = document.getElementById('username').value;
#             const password = document.getElementById('password').value;

#             // Here you can add authentication logic if needed
#             if (username && password) {
#                 document.getElementById('welcome-section').classList.add('hidden');
#                 document.getElementById('detection-section').classList.remove('hidden');
#             } else {
#                 alert('Please enter valid credentials.');
#             }
#         }

#         // Function to upload image and get prediction
#         async function uploadImage(event) {
#             event.preventDefault(); // Prevent form submission
#             const form = event.target;
#             const formData = new FormData(form);
#             const resultDiv = document.getElementById("result");

#             // Call your Flask prediction endpoint
#             const response = await fetch(form.action, {
#                 method: 'POST',
#                 body: formData,
#             });
#             const prediction = await response.json();

#             // Display result based on predicted_class
#             if (prediction.predicted_class === 0) {
#                 resultDiv.innerHTML = "Result: Negative (Normal)<br>Status: Non-Alcoholic, Non-Smoker";
#             } else {
#                 resultDiv.innerHTML = "Result: Positive (Pneumonia leading to Lung Cancer)<br>Status: Potentially Alcoholic, Chain Smoker";
#             }
#         }
#     </script>
# </body>
# </html>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import os

app = Flask(__name__)

# Define a directory to save uploaded images
UPLOAD_FOLDER = 'uploads_for_prediction'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the model globally to avoid reloading it for each request
model = load_model('cnn_model.h5')  # Replace with your actual model path

# Prediction function
def predict(image_path):
    target_size = (150, 150)
    img = image.load_img(image_path, target_size=target_size, color_mode="grayscale")
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(-1, 150, 150, 1)

    predictions = model.predict(img_array)
    confidence = predictions[0][0]

    predicted_class = 0 if confidence >= 0.5 else 1
    label = "Pneumonia" if predicted_class == 0 else "Normal"
    return {"predicted_class": predicted_class, "confidence": float(confidence), "label": label}

# Route to upload image and call prediction
@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({"error": "No image part in the request"}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Call the predict function
            prediction = predict(file_path)

            # Return the prediction result as JSON
            return jsonify(prediction)

    return '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lung Cancer Detection</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background: url('https://thumbs.dreamstime.com/z/cute-human-lungs-organ-character-cute-human-lungs-organ-character-look-bacteria-magnifier-vector-flat-line-cartoon-kawaii-204837299.jpg') no-repeat center center fixed;
            background-size: cover;
            background-color: #f0f0f5; /* Standard light gray color */
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #333;
        }
        .hidden { display: none; }
        .centered-container {
            text-align: center;
            background-color: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
            width: 80%;
            max-width: 500px;
        }
        input[type="text"], input[type="password"], input[type="file"], button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background-color: #0066cc;
            color: white;
            cursor: pointer;
        }
        button:hover { background-color: #005bb5; }
        .result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <!-- Welcome Section -->
    <div id="welcome-section" class="centered-container">
        <h1>Welcome</h1>
        <h2>SwasaRakshaka</h2>
        <form id="login-form" onsubmit="showDetectionInterface(event)">
            <input type="text" id="username" name="username" placeholder="Username" required>
            <input type="password" id="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>

    <!-- Detection Interface Section -->
    <div id="detection-section" class="centered-container hidden">
        <h2>Lung Cancer Detection using CNN</h2>
        <p>Upload X-ray image.</p>
        <form class="upload-form" method="post" enctype="multipart/form-data" onsubmit="uploadImage(event)">
            <input type="file" name="image" accept="image/*" required>
            <button type="submit">Upload & Detect</button>
        </form>
        <div id="result" class="result"></div>
    </div>

    <script>
        // Function to handle login and display the detection interface
        function showDetectionInterface(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Here you can add authentication logic if needed
            if (username && password) {
                document.getElementById('welcome-section').classList.add('hidden');
                document.getElementById('detection-section').classList.remove('hidden');
            } else {
                alert('Please enter valid credentials.');
            }
        }

        // Function to upload image and get prediction
        async function uploadImage(event) {
            event.preventDefault(); // Prevent form submission
            const form = event.target;
            const formData = new FormData(form);
            const resultDiv = document.getElementById("result");

            // Call your Flask prediction endpoint
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
            });
            const prediction = await response.json();

            // Display result based on predicted_class
            if (prediction.predicted_class === 0) {
                resultDiv.innerHTML = "Result: Negative (Normal)<br>Status: Non-Alcoholic, Non-Smoker";
            } else {
                resultDiv.innerHTML = "Result: Positive (Pneumonia leading to Lung Cancer)<br>Status: Potentially Alcoholic, Chain Smoker";
            }
        }
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
