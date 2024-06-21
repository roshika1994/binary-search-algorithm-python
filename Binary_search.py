#You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.
def binary_search(sorted_list, target_variable):
    left, right = 0, len(sorted_list)-1
    numbers_present = False

    for x in sorted_list:
        if all(isinstance(num, int) for num in sorted_list):
            numbers_present = True
        else:
            numbers_present = False


    while left <= right:
        mid_index = (left + right) // 2

        if numbers_present == True:
            if sorted_list[mid_index] == int(target_variable):
                return mid_index
            elif sorted_list[mid_index] < int(target_variable):
                left = mid_index + 1
            else:
                right = mid_index - 1
        else:
            if sorted_list[mid_index] == target_variable:
                return mid_index
            elif sorted_list[mid_index] < target_variable:
                left = mid_index + 1
            else:
                right = mid_index - 1
    return -1

print('Please enter the sorted list : ')
input_string = input()
input_string = input_string.replace('[', '').replace(']', '')

numbers_present = False

for x in input_string:
    if x.isdigit():
        numbers_present = True
    else:
        numbers_present = False

if numbers_present == True:
    sorted_list = [int(num) for num in input_string.split(',')]
    sorted_list.sort()
else:
    sorted_list = input_string.split(',')
    sorted_list.sort()

print("Sorted list:", sorted_list)

print('Please enter the target varible : ')
target_variable = input() 

target_variable_index = binary_search(sorted_list, target_variable)
print(target_variable_index)

if target_variable_index != -1:
    print(target_variable,' taget variable index is ', target_variable_index)
else:
    print(target_variable, ' does not exist on the sorted list')