def getLastValue (array):
    if(len(array) > 0):
        return array[len(array)-1]
    else:
        return None

def isSorted(array):
    index = 0
    for x in array:
        if index + 1 != len(array):
            if x > array[index+1]:
                return False
        index += 1
    return True

def sorter(array,reverse=False,distinct=False):
    sorted_array = []

    recurse = 1
    while(recurse > 0):
        temp_array = []
        index = 0
        if len(array) >= 1:
            if len(sorted_array) == 0:
                for element in array:
                    if len(temp_array) > 0:
                        if getLastValue(temp_array) > element:
                            num = temp_array.pop()
                            temp_array.append(element)
                            temp_array.append(num)
                        elif getLastValue(temp_array) < element:
                            temp_array.append(element)
                    else:
                        temp_array.append(element)
                    index += 1
                
                if isSorted(temp_array) == False:
                    recurse = 2
                sorted_array = temp_array
            else:
                temp_array.append(sorted_array[0])
                for element in sorted_array:
                    if getLastValue(temp_array) > element:
                        num = temp_array.pop()
                        temp_array.append(element)
                        temp_array.append(num)
                    elif getLastValue(temp_array) < element:
                        temp_array.append(element)
                    index += 1
            
        if isSorted(temp_array) == False:
            recurse = 2
        sorted_array = temp_array

        recurse -= 1

    distinct_array = []
    if distinct:
        for element in sorted_array:
            if distinct_array.__contains__(element) == False:
                distinct_array.append(element)
        sorted_array = distinct_array

    reverse_array = []
    if reverse:
        index = 1
        for element in sorted_array:
            reverse_array.append(sorted_array[len(sorted_array)-index])
            index += 1
        sorted_array = reverse_array
    return sorted_array