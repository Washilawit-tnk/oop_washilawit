Number = int(input("ใส่เลข : "))
for Tail in range(1,25,1):
    ans = Number*Tail
    if Number /2 % 2 != 0 :
            print(f"{Number}x{Tail}={ans}")