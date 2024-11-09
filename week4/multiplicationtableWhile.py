Number = int(input("ใส่เลข : "))
Tail = 1

while Tail < 25:
    ans = Number * Tail
    if Number / 2 % 2 != 0:
        print(f"{Number} x {Tail} = {ans}")
    Tail += 1
