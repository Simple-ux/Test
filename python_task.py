sorted_list = [1, 6, 8, 12, 13]

# O(n)
def twoSum(sorted_list, num):

    for i in range(len(sorted_list)):
        diff = num - sorted_list[i]
        if diff in sorted_list:
            return sorted_list[i], diff

print(twoSum(sorted_list, 20))



# O(n^2)
def twoSum_2(sorted_list, num):

    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == num:
                return sorted_list[i], sorted_list[j]

print(twoSum_2(sorted_list, 20))
