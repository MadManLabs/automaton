

class InstallModule():
    
    def __init__(self, _cfg):
        self.cfg = _cfg
        self.silent = self.cfg.silent_install
    
    def __del__(self):
        pass
    
    def run(self):
        pass
    
    def pr(self, mssg):
        if not self.silent:
            print mssg