#12-m
class Employee:
    def __init__(self, fullname, expericeni):
        self.fullname = fullname
        self.__experience = expericeni
        
    def get_fullname(self):
        return self.fullname
    
    def set_experience(self, new_experience):
        if 0 <= new_experience <= 40:
            self.__experience = new_experience
        else:
            print("Noto'g'ri tajriba")
            
e1 = Employee("John", "Smith")

print(e1.fullname)
print(e1.get_fullname())

e1.set_experience("Son")
print(e1.get_fullname())

e1.set_experience("sini")
print(e1.get_fullname())
