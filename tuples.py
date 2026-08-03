
info = ("Pradyumna", 12, 158.5, True)


print(info)
print()
tuple1 = (10, 20, 30, 40, 50, 50)


print("new tuple:", tuple1)
print()

# Step 3: Add a single new item (9)
tuple1 = tuple1 + (9,)


print(tuple1)
print()


print("50 appears", tuple1.count(50), "times.")
print()




print(tuple1[3:5])
print()



print(tuple1[:6])
print()

def palind(r):
    s = 0
    e = len(r) - 1

    while s < e:
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1

    return True

r = (1, 2, 3, 3, 2, 1)

if palind(r):
    print("It is Flip-Flop.")
else:
    print("It is not Flip-Flop.")

weather = (1, 0, 1, 1, 0, 1, 0)

sunny = 0
rainy = 0

for i in range(len(weather)):
    if weather[i] == 0:
        rainy += 1
    else:
        sunny += 1

print("Sunny days:", sunny)
print("Rainy days:", rainy)

if sunny > rainy:
    print("Good weather")
else:
    print("Bad weather")