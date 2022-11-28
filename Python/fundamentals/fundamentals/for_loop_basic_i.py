# Basics
for i in range(0,151):
    print(i)

# Multiples of Five
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)

# Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge
for i in range(0, 500000):
    sum = 0
    if i % 2 != 0:
        sum += i
print(sum)

# Countdown by Fours
i = 2018
while i > 0:
    print(i)
    i -= 4

# Flexible Counter
low_num = 2
high_num = 21
mult = 3
for i in range(low_num, high_num+1):
    if i % mult == 0:
        print(i)
