# Linear search
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

a_list = [1,8,32,91,5,15,9,100,3]
print(linear_search(a_list,91))


# Binary search
def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return False

a_list = [10,13,13,14,15,18,19]
print(binary_search(a_list,19))






