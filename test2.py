from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your actual name
    full_name = "Your Full Name"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get 'top' command output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error fetching top output: {e}"

    # HTML Response
    response = f"""
    <html>
    <head><title>System Monitor</title></head>
    <body>
        <h2>Name: {full_name}</h2>
        <h3>Username: {username}</h3>
        <h3>Server Time (IST): {server_time}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
