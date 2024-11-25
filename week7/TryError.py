try:
    Pice  = int(input("ใส่ราคา : "))
    HAN2  = 0.2
    HAN1  = 0.1
    if Pice == 0 :
        raise ZeroDivisionError
    elif Pice < 0 :
        raise Exception
    elif Pice >= 5000:
        print(f"ราคาทั้งหมด{Pice}จะได้รับส่วนลด{Pice*HAN}")
    elif Pice >= 2000 and a <= 4999:
        print(f"ราคาทั้งหมด{Pice}จะได้รับส่วนลด{Pice*HAN1}")
    else:
        print(f"หากยอดซื้อต่ำกว่า 2000 จะไม่ได้ส่วนสด {Pice}")

except ValueError:
    print('ใส่เฉพาะตัวเลข')
except ZeroDivisionError:
    print('ห้ามใส่ 0')
except:
    print('ห้ามใส่ค่าติดลบ')