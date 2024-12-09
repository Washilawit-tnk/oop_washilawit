a = 0
while True:
    try:
        b = input("ใส่ค่า :")
        if b == 0:
            raise ZeroDivisionError
        elif b * a



    except ZeroDivisionError:
        print("ห้ามกรอก 0")
    except:
        print("จบการทำงาน")