class Circle():
    def __init__(self,rad):
        self._rad=rad
    @property
    def rad(self):
        return self._rad
    @rad.setter
    def rad(self,new_rad):
        self._rad=new_rad
    def get_radius(self):
        print(self._rad)
kryg=Circle(25)
kryg.get_radius()
kryg.rad=767
kryg.get_radius()