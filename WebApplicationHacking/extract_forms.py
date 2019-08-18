# Using beautifulsoup4 to parse html and extract forms and its attributes
import requests
from bs4 import BeautifulSoup
import urllib

def request(url):
    try:
        return requests.get("http://" + url)
    except Exception:
        pass

target_url = "10.0.2.6/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content, features="lxml")# set lxml as the HTML parser, if not set, there will be a warning
forms_list = parsed_html.find_all("form")# find all form tag in current page

for form in forms_list:
    action = form.get("action")#get html attribute
    post_url = urllib.parse.urljoin(target_url, action)
    method = form.get("method")

    inputs_list = form.find_all("input")
    post_data = {}
    for input_tag in inputs_list:
        input_name = input_tag.get("name")
        input_type = input_tag.get("type")
        input_value = input_tag.get("value")
        if input_type == "text":
            input_value = "test"

        post_data[input_name] = input_value
    result = requests.post("http://" + post_url, data=post_data)
    print(result.content.decode())

