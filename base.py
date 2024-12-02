PATH = "01/"

def test():
    ...

    print("All tests passed")

def main():
    print(...)


should_test = input("Test ? (y/N) ")
if should_test.lower() == "y":
    file = "example.txt"
    test()
else:
    file = "input.txt"
    main()
