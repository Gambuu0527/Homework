for i in range(101):
    f"Энэ тоо бол {i}"
    print(i)

for i in range(101):
    if i % 5 == 0:
        print(i)
        
Diveded_by_five = [i for i in range(0, 101) if i % 5 == 0]
print(Diveded_by_five)