def number_times(num):
    flag = True
    times = 0
    while flag:
        if num >= 2:
            num = num // 2
            times+=1
        else:
            flag = False
    return times


# Testing
print(number_times(120)) #  6