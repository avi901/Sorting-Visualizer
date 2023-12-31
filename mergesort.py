import matplotlib.pyplot as plt
import random

random.seed('ABC')

amount = 10
numbers = [random.randint(0, 1000) for _ in range(amount)]


def merge_sort(number_list, left, right):
    if left >= right:
        return

    mid = (left+right) // 2

    # plt.bar(list(range(amount)), number_list)
    # plt.pause(0.001)
    # plt.clf()

    merge_sort(number_list, left, mid)
    merge_sort(number_list, mid+1, right)

    plt.bar(list(range(amount)), number_list)
    plt.pause(0.001)
    plt.clf()

    merge(number_list, left, right, mid)

    plt.bar(list(range(amount)), number_list)
    plt.pause(0.001)
    plt.clf()


def merge(number_list, left, right, mid):
    left_cpy = number_list[left:mid+1]
    right_cpy = number_list[mid+1:right+1]

    l_counter, r_counter = 0, 0

    sorted_counter = left

    while l_counter < len(left_cpy) and r_counter < len(right_cpy):
        if left_cpy[l_counter] <= right_cpy[r_counter]:
            number_list[sorted_counter] = left_cpy[l_counter]
            l_counter += 1
        else:
            number_list[sorted_counter] = right_cpy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_cpy):
        number_list[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1


merge_sort(numbers, 0, len(numbers)-1)
print(numbers)

plt.bar(list(range(amount)), numbers)
plt.show()
