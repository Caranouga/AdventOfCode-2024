import re

data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split('\n')

def prepare_h(line):
    return line

def prepare_d(data, idx1, idx2):
    prepared = []
    i = idx1
    j = idx2
    while max(i, j) < len(data):
        print(i, j, data[i][j])
        i += 1
        j += 1
    return prepared
        
def prepare_v(data, idx):
    prepared = []
    for i in range(len(data)):
        prepared.append(data[i][idx])
    return prepared

def exec_regex(string):
    return re.findall(r"XMAS", string) + re.findall(r"SAMX", string)

def count(data):
    somme = 0
    for i in range(len(data)):
        if len(exec_regex(prepare_h(data[i]))) > 0:
                somme += 1
        if len(exec_regex(prepare_v(data, i))) > 0:
            somme += 1
        for j in range(len(data[i])):
            if len(exec_regex(prepare_d(data[i][j]))) > 0:
                somme += 1
                
    return somme
        
print(prepare_d(data, 9, 0))
print(count(data))
