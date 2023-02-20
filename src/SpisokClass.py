

class SpisokClass:
    def __init__(self,npp,name,nch,sum):
        self._npp = npp
        self._name = name
        self._nch = nch
        self._sum = sum
    def get_npp(self):
        return self._npp
    def get_name(self):
        return self._name
    def get_nch(self):
        return self._nch
    def get_sum(self):
        return self._sum
    def set_npp(self,npp):
        self._npp = npp
    def set_name(self,name):
        self._name = name
    def set_nch(self,nch):
        self._nch = nch
    def set_sum(self,sum):
        self._sum = sum