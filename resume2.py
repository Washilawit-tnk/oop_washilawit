name = str(input("ชื่อเล่น"))
centimeter = float(input("ส่วนสูง"))
kilogram = float(input("น้ำหนัก"))
Full = str(input("ชื่อจริง"))
age = int(input("อายุ"))
IDstudent = int(input("รหัสประจำตัวนักเรียน"))
Gradelevel = int(input("ระดับการศึกษา"))


print(f"ชื่อ:{Full}อายุ,{age}")
print(f"รหัสประจำตัวนักเรียน:{IDstudent}ระดับชั้น{Gradelevel}")
print(f"ชื่อเล่น:{name}")
print(f"ส่วนสูง:{centimeter}น้ำหนัก: {kilogram}")
plus = centimeter + kilogram
print(f"ส่วนสูง + น้ำหนัก ={plus}")

