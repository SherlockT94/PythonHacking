# This script is used to find possible subdomains and directories and files in a website via guessing using a list of possible options
import requests

def request(url):
    try:
        return requests.get("http://" + url)#get method to get a web page
    except Exception:
        pass

target_url = "10.0.2.6/mutillidae"

# Discover subdomains
# with open("/root/PythonHacking/WebApplicationHacking/subdomains.list", "r") as wordlist_file:
    # for line in wordlist_file:
        # word = line.strip()
        # test_url = word + "." + target_url
        # response = request(test_url)
        # if response:
            # print("[+] Discovered subdomain --> " + test_url)

# Discover directories/fils
with open("/root/PythonHacking/WebApplicationHacking/files-and-dirs-wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)
