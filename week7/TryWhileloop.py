
inpud = 0 
while True:
    try:
        Pice = input("ใส่ราคาทีต้องจ่ายทั้งหมด : ")
        if Pice == "exit":
            print(f"ผมรวมคือ {inpud}")
            break 
        Pice = int(Pice)
        if Pice < 0:
            raise ZeroDivisionError
        elif Pice == 0:
            raise Exception
        else :
            inpud += Pice
            print(inpud)
    except ZeroDivisionError:
        print("ห้ามใส่ค่าเป็น 0")
    except ValueError:
        print("ห้ามใส่ข้อมูลที่ไม่ใช่ตัวเลข")
    except:
        print("ห้ามใส่ค่าติดลบ")




