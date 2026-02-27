import httpx
import time
import subprocess
import os

def test_api():
    print("Starting FastAPI server...")
    # Start the server as a subprocess
    server_process = subprocess.Popen(
        ["python", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.getcwd()
    )
    
    time.sleep(5)  # Wait for server to start
    
    try:
        # Test Root Endpoint
        print("Testing Root Endpoint...")
        response = httpx.get("http://127.0.0.1:8000/")
        print("Root Response:", response.json())
        
        # Test Add User
        print("\nTesting Add User...")
        user_data = {"username": "testuser", "password": "testpassword123"}
        response = httpx.post("http://127.0.0.1:8000/add-user", json=user_data)
        print("Add User Response:", response.json())
        
        # Test Get Users
        print("\nTesting Get Users...")
        response = httpx.get("http://127.0.0.1:8000/users")
        print("Get Users Response:", response.json())
        
    except Exception as e:
        print("API Test Failed:", str(e))
    finally:
        print("\nStopping server...")
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    test_api()
