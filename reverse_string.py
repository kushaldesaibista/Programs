# Reverse string


class ReverseStringClass():

    def reverse_words(self, original_string):
            string_list = original_string.split(" ")
            reversed_string_list = string_list[-1::-1]
            # i = len(string_list) -1
            # reversed_string_list = ' '
            # while(i!=-1):
            #     reversed_string_list = reversed_string_list + string_list[i]
            #     i = i-1
            reversed_string = " ".join(reversed_string_list)
            return reversed_string


original_string = input("Enter a string:")
print(ReverseStringClass().reverse_words(original_string))



