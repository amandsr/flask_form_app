import sys
import requests
import json
import logging
import os

# Ensure the directory for the log file exists
log_directory = os.path.dirname('api_script.log')
if log_directory and not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up logging to a file
logging.basicConfig(filename='api_script.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def trigger_api_call(data):
    try:
        # Dummy API URL - Replace with your actual API
        api_url = "https://jsonplaceholder.typicode.com/posts"

        # Log the data received from Flask (payload to be sent)
        logging.info(f"Received data: {json.dumps(data)}")

        # Send the form data as the payload to the API
        response = requests.post(api_url, json=data)

        # Check if the API call was successful
        if response.status_code == 201:
            logging.info(f"API call successful! Response: {response.json()}")
        else:
            logging.error(f"API call failed with status code {response.status_code}. Response: {response.text}")

    except requests.exceptions.RequestException as e:
        # Log any exception during the API call
        logging.error(f"Error making the API call: {str(e)}")

    except Exception as e:
        # Log any other general errors
        logging.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        # Get the form data passed as command-line argument
        form_data_json = sys.argv[1]  # The form data will be the first argument

        # Parse the form data from JSON
        form_data = json.loads(form_data_json)

        # Log the start of the script
        logging.info("Starting API script...")

        # Trigger the API call with the form data
        trigger_api_call(form_data)

        # Log completion of the script
        logging.info("API script completed successfully.")

    except IndexError:
        # Handle the case where no data is passed to the script
        logging.error("No form data received from Flask.")
    except Exception as e:
        # Log any errors that occur in the script
        logging.error(f"An error occurred while executing the script: {str(e)}")

