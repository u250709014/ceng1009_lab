# def is_odd(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_odd(5))
# # from unittest import result
# #
# #
# def is_leapyear(year):
#     if year % 4 == 400:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print (is_leapyear(1900))
# #
# def print_triangular_numbers(n):
#     total=0
#     for i in range(1,n+1):
#         total=total+i
#         print(total)
#
# print_triangular_numbers(5)
# #
# def is_prime(n):
#     if n < 2:
#         return False
#     # for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(4875))
# #
#
# def reserve(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result
# print(reserve("abcd"))
#
# def reverse_slice(s):
#     return s[::-1]
# # print(reverse_slice("hello"))
#
#
# #
# def remove_all_occurrences(string, substring):
#     # return string.replace(substring, "")
# print(remove_all_occurrences("hello world", "hello"))
#
# def substitution_cipher(message, mapping):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     encrypted_message = ""
#
#     for char in message:
#         index = alphabet.find(char.lower())
#         if index == -1:
#             encrypted_message += char
#         # elif char.isupper():
#             encrypted_message = encrypted_message + mapping[index].upper()
#         else:
#             encrypted_message = encrypted_message + mapping[index].lower()
#     return encrypted_message
#
# mapping = "QTGABCDEFHIJKLMNOPRSUVWXYZ"
# message = "Hdlksjdccs"
#
# encrypted = substitution_cipher(message, mapping)
#
# print(encrypted)
#
#
# def remove_dups(string):
#     new_string = ""
#
#     for char in string:
#         if char not in new_string:
#             new_string += char
#
#     return new_string
#
# text = "hello world"
# print(remove_dups(text))