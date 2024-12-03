day = input("Which day ? ")
step = input("Which step ? ")

if len(day) == 1:
    day = "0" + day
if len(step) == 1:
    step = "0" + step

exec(open(f"{day}/part{step}/index.py").read())