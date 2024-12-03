import re

PATH = "03/"

regex = r"(mul\(\d{1,},\d{1,}\))"

def test():
    prepared = prepare_input()
    assert prepared == ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']

    counted = count(prepared)
    assert counted == 161

    print("All tests passed")

def main():
    print(count(prepare_input()))

def prepare_input():
    data = open(PATH + file).read().split("\n")

    return [elt for elt in re.split(regex, data[0]) if re.match(regex, elt)]

def count(data):
    count = 0
    for line in data:
        part01, part02 = line.split("(")[1].split(")")[0].split(",")
        count += int(part01) * int(part02)
    
    return count



should_test = input("Test ? (y/N) ")
if should_test.lower() == "y":
    file = "example01.txt"
    test()
else:
    file = "input.txt"
    main()
