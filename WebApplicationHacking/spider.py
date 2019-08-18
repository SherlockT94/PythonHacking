# This script will discover all possible parts of a website
import requests
import re
import urllib

# target_url = "http://zsecurity.org"
# target_url = "https://zsecurity.org/"
# domain = "zsecurity.org"
target_url = "http://10.0.2.6/mutillidae/"
target_links = []

def extract_link_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())

# When discover a link, it will go into the link utill there is no more to go
def crawl(url):
    href_links = extract_link_from(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)#join relative url and target url
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_links:
            target_links.append(link)# append() will searching the global namespace, so no need to using global keyword
            print(link)
            crawl(link)# call it self

crawl(target_url)
