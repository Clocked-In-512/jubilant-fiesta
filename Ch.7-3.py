##Robert Fernandez
##Complete
##This program will create a list of numbers to print maximum and minimun numbers in the list.

def total_list(numbers):
    return sum(numbers)

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    combined_list = sorted(list1 + list2)
    total = total_list(combined_list)
    print("Sorted List:", combined_list)
    print("Total:", total)
    print("Maximum Value:", max(combined_list))
    print("Minimum Value:", min(combined_list))
