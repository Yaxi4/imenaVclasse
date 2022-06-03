class Departament:
    Pyhton = 3
    Go = 4
    Java = 7

    def info(self):
        print(self.Pyhton, self.Go, self.Java)

    def info2(self):
        print(Departament.Pyhton, Departament.Go, Departament.Java)

    @property
    def info_property(self):
        print(self.Pyhton, self.Go, self.Java)

    @classmethod
    def info_class(cls):
        print(cls.Pyhton, cls.Go, cls.Java)

    @staticmethod
    def info_static():
        print(Departament.Pyhton, Departament.Go, Departament.Java)

a=Departament()
a.info()
a.info2()
a.info_property
a.info_class()
a.info_static()
print('----')
