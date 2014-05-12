import urllib
from lxml import html
import os
import cfg
from modules.install_module import InstallModule

class InstallTor(InstallModule):

    def __init__(self, _cfg):
        InstallModule.__init__(self, _cfg)
        
    def run(self):
        url = self.get_tor_url()
    
    def get_tor_url(self):
        tor_site = 'https://www.torproject.org/download/download-easy.html.en'
        page = html.fromstring(urllib.urlopen(tor_site).read())
        
        tor_file = 'https://www.torproject.org'
        for link in page.xpath("//a"):
            if link.get("class") == "button lin-tbb32":
                tor_file += link.get("href")[2:]
                return tor_file
            
        return None


if __name__ == '__main__':
    
    ins_t = InstallTor(cfg)
    ins_t.run()