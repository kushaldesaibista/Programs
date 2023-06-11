# Search in list

list = ['a', 'b', 'c']


def search_element(list, elementSearch):
    for i in range(0, len(list)):
        if elementSearch == list[i]:
            return "element exist in lists"


print(search_element(list, 'b'))
