a = int(input("รับค่าตัวเลข :"))
for i in range(1,25,1):
    b = a*i
    if a /2%2 !=0:
        print(f"{a} x {i} = {b}")