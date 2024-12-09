# orders = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13"""
# 
# pages = """75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""


def parse_data():
    data = open('input.txt').read().splitlines()
    
    orders = []
    pages = []
    a = True
    for line in data:
        if line == "":
            a = False
            continue
        if a:
            orders.append(line)
        else:
            pages.append(line)
                
    return [[int(char) for char in order.split('|')] for order in orders], [[int(char) for char in page.split(',')] for page in pages]

            
orders, pages = parse_data()
            
# orders = [[int(char) for char in order.split('|')] for order in orders.splitlines()]
# pages = [[int(char) for char in page.split(',')] for page in pages.splitlines()]

            

def has_order(nb):
    return len(get_befores(nb)) > 0

def get_befores(nb):
    befores = []
    for order in orders:
        if order[0] == nb:
            befores.append(order[1])
    return befores

def validate(page):
    already_inserted = []
    for char in page:
        befores = get_befores(char)
        for before in befores:
            if before in already_inserted:
                return False
            
        already_inserted.append(char)
        
    return True

def get_middle(page):
    return page[int(len(page) / 2)]
    
def count():
    somme = 0
    for page in pages:
        if validate(page):
            somme += get_middle(page)
            
    return somme
        

