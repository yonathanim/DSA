def occurrences(arr, num):
    count = 0
    for element in arr:
        if element == num:
            count += 1
    return count

def main():
    
    seq = input("Enter a sequence of numbers separated by spaces: ")
    seq = list(map(int, sequence.split()))
    search_num = int(input("Enter a number to be searched: "))
    occurrences = occurrences(seq, search_num)
    if occurrences > 0:
        print(f"The number {search_num} appears {occurrences} time(s) in the sequence.")
    else:
        print(f"The number {search_num} is not present in the sequence.")

if __name__ == "__main__":
    main()
()
