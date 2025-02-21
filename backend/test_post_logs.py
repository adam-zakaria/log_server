import requests

def main():
    url = "http://localhost:3000/logs"
    payload = {
        "logs": "This is a test log line from Python script."
    }
    
    try:
        # Send POST with JSON payload
        response = requests.post(url, json=payload)
        
        # Check the response status
        if response.status_code == 200:
            print("Successfully posted logs!")
            print("Response JSON:", response.json())
        else:
            print(f"Failed to post logs. Status code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print("Error posting to /logs:", e)

if __name__ == "__main__":
    main()
