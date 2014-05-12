import os
from modules.install_module import InstallModule

class InstallPython(InstallModule):
    
    def __init__(self, _cfg):
        InstallModule.__init__(self, _cfg)
        
        self.psu_bash = 'export PYTHONSTARTUP=$HOME/.pythonstartup'
    
    def run(self):
        self.pr('# ----------')
        self.pr('Installing python')
        self.pr('# ----------')
        self.set_pythonstartup()
        self.install_lib()
    
    def set_pythonstartup(self):
        self.pr('Creating pythonstartup file')
        os.system('cat {} > ~/.pythonstartup'.format(self.cfg.python_startup_file))
                  
    def install_lib(self):
        for lib in self.cfg.python_lib:
            os.system('sudo aptitude install {}'.format(lib))
            
            