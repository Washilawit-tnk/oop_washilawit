class oopcat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
        self.name=ชื่อ
        self.age=อายุ
        self.gender=เพศ
        self.color=สี
    def old(self):
        self.age += 1
cat1 = oopcat(ชื่อ="ศรีทอง",อายุ=4,เพศ="ผู้",สี="ทอง")
cat2 = oopcat("ศรีทอง",4,"ผู้","ทอง")
cat2.old
print(cat2.age)