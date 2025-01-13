class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} สี {self.color}"

class dog(Animal):
    def speak(self):
        return "โฮ่ง"

dog1 = dog('ประจวบ',10,'ขาว')
print(f'หมาชื่อ {dog1.name} ร้อง {dog1.speak()}')
print(f'ข้อมูลหมาตัวที่1 คือ {dog1.showinfo()}')