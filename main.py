import requests

print("[1]Exercise 1")
print("[2]Exercise 2")
method = input("Please choose a mode: ")
print()
print("[1]Text mode")
print("[2]Gui mode")
istext = input("Please choose a mode: ")

if int(method) == 1 and int(istext) == 1:
    print("\nTrying getting Exercise 1 in text mode...")
    exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/gitfile/gui-text.py").text)
    print("\nExecution was complete!")
elif int(method) == 1 and int(istext) == 2:
    print("\nTrying getting Exercise 1 in gui mode...")
    exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/gitfile/gui.py").text)
    print("\nExecution was complete!")
elif int(method) == 2 and int(istext) == 1:
    print("\nTrying getting Exercise 2 in text mode...")
    exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/gitfile/gui2-text.py").text)
    print("\nExecution was complete!")
elif int(method) == 2 and int(istext) == 2:
    print("\nTrying getting Exercise 2 in gui mode...")
    exec(requests.get("https://raw.githubusercontent.com/AlexPhamNgoQuoc/appbasicbuoi1/main/gitfile/gui2.py").text)
    print("\nExecution was complete!")
else:
    print("\n\nThere was an error: The mode was either incorrect or the python file was corrupted. 😥")

