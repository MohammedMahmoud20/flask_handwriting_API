import requests

# URL of the Flask API
url = 'http://127.0.0.1:5000/predict'

# Path to the image you want to test
image_path = 'NonASD004.jpg'

# Prepare the image file to send
with open(image_path, 'rb') as img:
    files = {'image': img}  # Make sure the key is 'image'
    response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    try:
        print(f"Response JSON: {response.json()}")
    except ValueError:
        print("Response is not in JSON format")
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
