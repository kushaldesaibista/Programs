# Reverse List





# def rev_fun(rev_list):
#     print("original:", rev_list)
#     if not rev_list:
#         return "list empty"
#     if rev_list:
#         front_pointer = 0
#         last_pointer = len(rev_list) - 1
#         while front_pointer < last_pointer:
#             rev_list[front_pointer], rev_list[last_pointer] = rev_list[last_pointer], rev_list[
#                 front_pointer]
#             front_pointer += 1
#             last_pointer -= 1
#         return rev_list


# print("reversed:", rev_fun(reverse_list))

class ReverseList:
    def reverse_list(self,original_list):
        reverse_list = original_list[-1::-1]
        return reverse_list


# outside class
original_list = []
n = int(input("Enter number of elements in list:"))
for i in range(0,n):
    ele = input()
    original_list.append(ele)

print(ReverseList().reverse_list(original_list))



