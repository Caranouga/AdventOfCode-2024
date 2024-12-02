PATH = "01/"

def test():
    prepared = prepare_input()
    assert prepared == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])

    counted = count(prepared)
    assert counted == 11

    print("All tests passed")

def main():
    print(count(prepare_input()))

def prepare_input():
    data = open(PATH + file).read().split("\n")

    lst1 = []
    lst2 = []

    for i in data:
        lst1.append(int(i.split("  ")[0]))
        lst2.append(int(i.split("  ")[1]))

    return lst1, lst2

def count(data):
    """Sum the differences between the two smallest numbers in each list"""

    lst1, lst2 = data
    count = 0

    while len(lst1) > 0:
        index1 = find_smallest(lst1)
        index2 = find_smallest(lst2)

        count += abs(lst1.pop(index1) - lst2.pop(index2))

    return count

def find_smallest(lst):
    """Find the smallest number in a list and return it's index"""
    smallest = lst[0]
    index = 0

    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            index = i

    return index



should_test = input("Test ? (y/N) ")
if should_test.lower() == "y":
    file = "example.txt"
    test()
else:
    file = "input.txt"
    main()
