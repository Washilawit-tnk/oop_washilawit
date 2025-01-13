class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} สี {self.color}"

class dog(Animal):
    def __init__(self,name,age,color,rang):
        super().__init__(name,age,color)
        self.nama = rang
    def showdog(self):
        return f"หมาพันนี้ {self.nama} มี {super().showinfo()}"

dog1 = dog("ประจวบ",10,"ขาว","ขี้เรื้อน")
print(dog1.showdog())