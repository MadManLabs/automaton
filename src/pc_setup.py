__author__ = "Martin Penicka"
__copyright__ = "Copyright 2014, Martin Penicka"

__licence__ = "GPL_v3"
__version__ = "0.1"
__email__ = "martin-penicka@seznam.cz"

import os

# =================

# -----------------
# Config
# -----------------

silent = False

install_software = False
install_games = False
install_python_lib = False
init_nano = True
init_alias = True

# -----------------
# Lists
# -----------------

ppa = []

software = ['vlc', 'calibre', 'gimp', 'blender', 'unrar']
python_lib = ['numpy', 'matplotlib', 'scipy', 'pip', 'nmap', 'xlrd', 'biopython']
games = ['openttd', 'openarena']

eclipse = 'http://www.auto_eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/kepler/SR2/auto_eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar.gz&mirror_id=580'
minecraft = 'https://www.dropbox.com/s/683xlul3mgmj5lg/Minecraft.jar'
tor = 'https://www.torproject.org/dist/torbrowser/3.5.3/tor-browser-linux64-3.5.3_en-US.tar.xz'


alias = ['minecraft=\'java -jar /home/martin/Hry/Minecraft.jar\'', 
         'sicstus=\'/usr/local/sicstus4.2.0/bin/sicstus\'', 
         'tor=\'/opt/tor-browser_en-US/start-tor-browser\'', 
         'auto_eclipse=\'/opt/auto_eclipse/auto_eclipse\'', 
         'alias unrar=\'unrar x\'']
nano = []

# =================

def pr(note):
    if not silent:
        print note
        
def get_python_lib():
    for lib in python_lib:
        yield 'python-' + lib

def install_list(sw_list):
    for item in list:
        pr('installing : ' + str(item))
        os.system('sudo aptitude install ' + item)
        
def get_file(path):
    splited = path.split('/')
    return splited[-1]

pr('Installing aptitude')
#os.system('sudo apt-get install aptitude')

if install_software:
    pr('# ----------')
    pr('Installing software')
    pr('# ----------')
    install_list(software)
    
if install_games:
    pr('# ----------')
    pr('Installing games')
    pr('# ----------')
    install_list(games)
    
if install_python_lib:
    pr('# ----------')
    pr('Installing python libraries')
    pr('# ----------')
    install_list(python_lib)
    
# setup Minecraft

    
# ==========

# Testing

if __name__ == '__main__':
    
    print get_file(tor)

