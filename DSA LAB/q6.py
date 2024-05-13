def delete(array, index):
    if index < 0 or index >= len(array):
        print("Invalid index.")
        return array
    
    del array[index]
    return array
array = [3, 7, 1, 9, 4]
index = 2
print("Original array:", array)
array = delete(array, index)
print("Modified array:", array)
