class Nam:

    name = "I dont know "

    #def changename(self, name):
    #    self.__class__.name = name

    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Nam()
p1.changename("Tejas Pawar")
print(p1.name)
print(Nam.name)