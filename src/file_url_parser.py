import urllib
from lxml import html


def get_tor_url():
    tor_site = 'https://www.torproject.org/download/download-easy.html.en'
    page = html.fromstring(urllib.urlopen(tor_site).read())
    
    tor_file = 'https://www.torproject.org'
    for link in page.xpath("//a"):
        if link.get("class") == "button lin-tbb32":
            tor_file += link.get("href")[2:]
            break
        
    return tor_file

def get_eclipse_url():
    eclipse_download_site = "http://www.eclipse.org/downloads/?osType=linux"
    d_page = html.fromstring(urllib.urlopen(eclipse_download_site).read())
    
    for link in d_page.xpath("//a"):
        if link.get("class") == "downloadLink" and "Linux 64 Bit" in link.get("title") and "Standard" in link.get("title"):
            print link.get("href")


if __name__ == '__main__':
    
    #print get_tor_url()
    print get_eclipse_url()