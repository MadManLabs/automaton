

class InstallModule():
    
    def __init__(self):
        self.silent = True
    
    def __del__(self):
        pass
    
    def run(self):
        pass
    
    def pr(self, mssg):
        if not self.silent:
            print mssg