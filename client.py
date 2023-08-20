try:
    import requests
except:
    import os
    os.system("pip install requests")

exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/main.py").text)
