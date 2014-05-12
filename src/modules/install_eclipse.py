import urllib
from lxml import html
import os
import cfg
from modules.install_module import InstallModule

class InstallEclipse(InstallModule):
    
    def __init__(self, _cfg):
        InstallModule.__init__(self, _cfg)
        
    def run(self):
        url = self.get_eclipse_url()
        self.download_eclipse(url)

    def get_eclipse_url(self):
        eclipse_site = "http://www.eclipse.org/downloads/"
        eclipse_download_site = "http://www.eclipse.org/downloads/?osType=linux"
        try:
            d_page = html.fromstring(urllib.urlopen(eclipse_download_site).read())
        except:
            print os.path.basename(__file__) + " : Cannot load download site."
            return None
        
        for link in d_page.xpath("//a"):
            if link.get("class") == "downloadLink" and "Linux 64 Bit" in link.get("title") and "Standard" in link.get("title"):
                first_link = 'http:' + link.get("href")
                
        try:
            d_page = html.fromstring(urllib.urlopen(first_link).read())
        except:
            print os.path.basename(__file__) + " : Cannot load download site."
            return None
        
        for link in d_page.xpath("//a"):
            if 'mirror_id' in link.get("href"):
                return eclipse_site + link.get("href")
            
        return None

    def download_eclipse(self, url):
        
        if not os.path.exists(self.cfg.use_tmp_dir):
            try:
                os.mkdir(self.cfg.use_tmp_dir)
            except:
                print os.path.basename(__file__) + " : Cannot create directory cfg.use_tmp_dir."
                exit(0)
        
        # Download to tmp dir
        #wget_command = 'wget ' + url + ' -P' + cfg.use_tmp_dir
        wget_command = 'wget ' + 'http://www.novinky.cz/static/images/logo.gif' + ' -P' + self.cfg.use_tmp_dir
        print "===\nstart download \n",wget_command,"\n==="
        os.system(wget_command)
        exit()
        # Extract from tar file
        file_name = url.split('&')[0]
        os.system('tar -xzvf ' + self.cfg.use_tmp_dir + file_name)
        os.system('rm ' + self.cfg.use_tmp_dir + file_name)
        
        return self.cfg.use_tmp_dir + 'eclipse/'

    def install_plugins(self, plugin_set):
        pass

if __name__ == '__main__':
    
    inst_e = InstallEclipse(cfg)
    inst_e.run()