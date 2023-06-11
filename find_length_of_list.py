# lenth list

def list_Length(list):
    if list:
        type1 = len(list)
        # type 2
        type2 = 0
        for i in list:
            type2 += 1

        return type2
    else:
        return None


list = []
print(list_Length(list))
