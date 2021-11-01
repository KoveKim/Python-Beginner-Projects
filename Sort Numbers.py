# Sorting a numerical list!

def sort_numbers(sort):
    numbers_list = open("numberslist.txt", "r+").read().splitlines()
    # Open the file, read the data, remove whitespace, convert to list

    length = len(numbers_list)  # How many items are in the list (12 in this case)

    # Ascending order, bubble sort. Comments to understand wtf is going on
    if sort == "asc":
        for i in range(length):  # Stop when there's nothing left to sort
            been_sorted = True

            # Looks at each item, compares to adjacent
            for j in range(length - i - 1):  # Range is 0-12

                if numbers_list[j] > numbers_list[j + 1]:  # Mind the operator
                    # If current item is greater than adjacent, swap them

                    numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                    # This is the swap

                    been_sorted = False
                    # Since we swapped, set bool to False so it doesn't stop prematurely

            if been_sorted:
                break
                # If there were no swaps and the array is sorted, terminate


    # Descending order, bubble sort, no comments
    if sort == "desc":
        for i in range(length):
            been_sorted = True
            for j in range(length - i - 1):
                if numbers_list[j] < numbers_list[j + 1]:
                    numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                    been_sorted = False
            if been_sorted:
                break


    # The "asc" bubble sort in its most simplified form
    if sort == "none":
        for i in range(length):
            for j in range(length - i - 1):
                if numbers_list[j] > numbers_list[j + 1]:
                    numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

    print(numbers_list)


sort_numbers("asc")
sort_numbers("desc")
sort_numbers("none")
