num = int(input("จำนวนคนที่จะป้อน: "))
rem = {}
for i in range(1,rem+1):
    print(f"กรอกข้อมูลคนที่ {i}")
    rem["Nickname"] = str(input("ชื่อเล่น: "))
    rem["Number"] = str(input("เลขที่: "))
    rem["age"] = str(input("อายุ: "))
    rem["IDSTUDENT"] = str(input("เลขนักศึกษา: "))