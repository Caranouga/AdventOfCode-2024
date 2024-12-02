PATH = "01/"

def test():
    prepared = prepare_input()
    assert prepared == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])

    counted = count(prepared)
    assert counted == 31

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
    lst1, lst2 = data
    
    total_sum = 0
    for elt1 in lst1:
        sum_ = 0
        for elt2 in lst2:
            if elt1 == elt2:
                sum_ += 1
        total_sum += sum_ * elt1

    return total_sum

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
