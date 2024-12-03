import re

PATH = "03/"

regex = r"(don't|do)|(mul\(\d{1,},\d{1,}\))"

def test():
    prepared = prepare_input()
    assert prepared == ['mul(2,4)', "don't", 'mul(5,5)', 'mul(11,8)', 'do', 'mul(8,5)']

    counted = count(prepared)
    assert counted == 48

    print("All tests passed")

def main():
    print(count(prepare_input()))

def prepare_input():
    data = open(PATH + file).read().split("\n")

    return [elt for elt in re.split(regex, data[0]) if not elt == None and re.match(regex, elt)]

def count(data):
    count = 0
    activated = True
    for line in data:
        if line == "don't":
            activated = False
            continue
        elif line == "do":
            activated = True
            continue
        if not activated:
            continue
        part01, part02 = line.split("(")[1].split(")")[0].split(",")
        count += int(part01) * int(part02)
    
    return count



should_test = input("Test ? (y/N) ")
if should_test.lower() == "y":
    file = "example02.txt"
    test()
else:
    file = "input.txt"
    main()
