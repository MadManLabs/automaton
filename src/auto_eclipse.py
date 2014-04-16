import urllib
from lxml import html
import os
import cfg

def get_eclipse_url():
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

def download_eclipse(url):
    
    if not os.path.exists(cfg.use_tmp_dir):
        try:
            os.mkdir(cfg.use_tmp_dir)
        except:
            print os.path.basename(__file__) + " : Cannot create directory cfg.use_tmp_dir."
            exit(0)
    
    # Download to tmp dir
    wget_command = 'wget ' + url + ' ' + cfg.use_tmp_dir
    os.system(wget_command)
    
    # Extract from tar file
    file_name = url.split('&')[0]
    os.system('tar -xzvf ' + cfg.use_tmp_dir + file_name)
    os.system('rm ' + cfg.use_tmp_dir + file_name)
    
    return cfg.use_tmp_dir + 'eclipse/'

def install_plugins(plugin_set):
    pass

if __name__ == '__main__':
    
    url = get_eclipse_url()
    print url
    download_eclipse(url)