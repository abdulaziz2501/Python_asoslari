num=12
a=False
for i in range(2, num):
    if num % i == 0:
        a = True
        break
    else:
        break
if a:
    print("Tub son emas")
else:
    print("Tub son")