import urllib
from lxml import html
import os
import cfg

def get_tor_url():
    tor_site = 'https://www.torproject.org/download/download-easy.html.en'
    page = html.fromstring(urllib.urlopen(tor_site).read())
    
    tor_file = 'https://www.torproject.org'
    for link in page.xpath("//a"):
        if link.get("class") == "button lin-tbb32":
            tor_file += link.get("href")[2:]
            return tor_file
        
    return None


if __name__ == '__main__':
    
    url = get_tor_url()
    print url