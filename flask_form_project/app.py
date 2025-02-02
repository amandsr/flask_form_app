import os
import subprocess
import json
import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ensure the directory for the log file exists
log_directory = os.path.dirname('flask_app.log')
if log_directory and not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up logging for the Flask app
logging.basicConfig(filename='flask_app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Get form data from the POST request
        form_data = request.get_json()

        # Log the received form data in the Flask app
        app.logger.info(f"Received form data: {json.dumps(form_data)}")

        # Optionally, save the form data to a file (like JSON)
        with open("form_data.json", "w") as file:
            json.dump(form_data, file, indent=4)

        # Prepare the form data as JSON to send to the Python script
        form_data_json = json.dumps(form_data)

        # Trigger the Python script and pass the form data to it
        result = subprocess.run(
            ["python3", "api_script.py", form_data_json],  # Pass data as a command-line argument
            check=True, capture_output=True, text=True
        )

        # Log the output of the script
        app.logger.info(f"Python script executed successfully: {result.stdout}")

        # Return a success response
        return jsonify({"message": "Form submitted successfully and API triggered."})

    except subprocess.CalledProcessError as e:
        # Log the error if the Python script fails
        app.logger.error(f"Error executing Python script: {e.stderr}")
        return jsonify({"message": "Error executing API call"}), 500

    except Exception as e:
        # Log any other errors
        app.logger.error(f"An error occurred while processing the form: {str(e)}")
        return jsonify({"message": "There was an error processing your form."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

