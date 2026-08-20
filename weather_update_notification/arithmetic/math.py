from collections import Counter
# x = int(input("Please enter a number to print table: "))
# for i in range(1, 11):
#     result = x * i
#     print(result)

# name = "Alice"
# result = ""
# # print (name[index])
# for i in range(len(name)):
#     if i % 2 != 0:
#         result += name[i]
# print(result)

# name = "welcome"
# print(name[::-1])

# n = 4
# numbers = ""
# for i in range( 1, n+1 ):
#   numbers += str(i) + " "
#   print(numbers)


# numbers = [1, 2, 3, 7, 5]
# target = 12 
# index_string = ""
# index = 0
# while index < len(numbers):
#     if numbers[index] + numbers[index +1] == target:
#         print(f"Pair found: {numbers[index]} + {numbers[index + 1]} = {target}")
#         index_string += f"({index}, {index + 1}) "
#         print(f"Indices of the pair: {index_string}")
#         break
#     else:
#         index_string = "-1"
#         break
#     index += 1
# print(f"Indices of the pair: {index_string}")

# numbers = [1, 2, 3, 4, 5]
# result = ""
# for num in numbers:
#     result += str(num) + " "
#     print(result)

# name = "Devops"
# reversed_name = ""
# # for i in range(len(name)-1, -1, -1):
# #     reversed_name += name[i]
# for char in name:
#     reversed_name = char + reversed_name
# print(reversed_name)

# name = "Devops"
# reversed_name = ""
# index = len(name) - 1
# while index >= 0:
#     reversed_name += name[index]
#     index -= 1
# print(reversed_name)

# words = sentence.split()
# reveresed_sentence = ""
# index = 0
# for word in range(len(words)-1, -1 ,-1):
#     reveresed_sentence = words[index] + " " + reveresed_sentence
#     index += 1
# print(reveresed_sentence)

# print occurence of each vowel in a sentence

    # if char in "aeiouAEIOU":
    #     if char in "aA":
    #         count_a += 1
    #     elif char in "eE":
    #         count_e += 1
    #     elif char in "iI":
    #         count_i += 1
    #     elif char in "oO":
    #         count_o += 1
    #     elif char in "uU":
    #         count_u += 1


# remove duplicates from an array withoiy using set
# numbers = [1, 2, 3, 2, 5, 6, 1, 7]
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print(unique_numbers)

def largest_number( numbers ):
    for num in numbers:
        if num == max(numbers):
            return num


def second_largest( numbers ):
    largest = second_largest = 0
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    print(second_largest)

# count frequency in the word
def count_frequency(name = "banana"):
    print(Counter(name.lower()))

            



# count_frequency()
#print(second_largest([4,7,8,5,6]))
#print(largest_number([1, 2, 5, 5, 3]))  # Output: 5
