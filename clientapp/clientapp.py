import requests
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, required=True)
args = parser.parse_args()

# Prepare the file
with open(args.filename, 'rb') as f:
    files = {'file': f}

    # Send the POST request
    response = requests.post("http://localhost:8080/predictionB", files=files)

#can also just:
#curl -X POST -F "file=@file.txt" http://localhost:8080/predictionB


# Print the response
if response.text:
    # Print the response
    print(response.json())
else:
    print("Empty response received")