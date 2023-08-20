try:
    import requests
    import webbrowser
except:
    import os
    os.system("pip install requests")
    import requests
    import webbrowser

webbrowser.open("https://github.com/AlexPhamNgoQuoc/appbasicbuoi1/tree/main")


exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/main.py").text)
