# 1. Countdown
def countDownTimer(num):
    output = []
    for i in range(0, num + 1):
        output.append(i)
    output.reverse()
    return output

x = countDownTimer(5)
print(x)


# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

x = print_and_return([1,2])
print(x)


# 3. First Plus Length
def first_plus_length (arr):
    sum = arr[0] + len(arr)
    return sum

x = first_plus_length([1,2,3,4,5])
print(x)


# Values Greater than Second
def values_greater_than_second (arr):
    if len(arr) < 2:
        return False
    else:
        new_list = []
        second_value = arr[2]
        print(second_value)
        for i in arr:
            if i >= second_value:
                new_list.append(i)
        return new_list

x = values_greater_than_second([5,2,3,2,1,4])
y = values_greater_than_second([3])
print(x, y)


# This Lenght, That Value
def length_and_value(l,v):
    val = []
    for i in range(1,l+1):
        val.append(v)
    return val

x = length_and_value(4,7)
y = length_and_value(6,2)
print(x, y)