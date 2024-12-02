PATH = "02/"

def test():
    prepared = prepare_input()
    print(prepared)
    assert prepared == [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

    counted = count(prepared)
    assert counted == 4

    print("All tests passed")

def main():
    print(count(prepare_input()))

def prepare_input():
    data = open(PATH + file).read().split("\n")

    for i in range(len(data)):
        data[i] = [int(elt) for elt in data[i].split(" ")]

    return data

def count(data):
    count = 0
    for line in data:
        if is_safe(line):
            count += 1
        elif is_safe_removing(line):
            count += 1
    
    return count

def is_safe(line):
    is_increasing = line[0] < line[1]
    for i in range(len(line) - 1):
        actual = line[i]
        next_ = line[i + 1]

        if abs(actual - next_) > 3:
            return False
        if (is_increasing and actual > next_) or (not is_increasing and actual < next_):
            return False
        if actual == next_:
            return False
        
    return True
        
def is_safe_removing(line):
    for i in range(len(line)):
        copy = line.copy()
        copy.pop(i)
        if is_safe(copy):
            return True
    return False



should_test = input("Test ? (y/N) ")
if should_test.lower() == "y":
    file = "example.txt"
    test()
else:
    file = "input.txt"
    main()
