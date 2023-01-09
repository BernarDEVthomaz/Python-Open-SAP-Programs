with open("numbers.txt", "r") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        lines[i] = int(line.strip())
        i = i + 1
    lines = sorted(lines)
    print(lines[-1])
    print(lines[-2])
    print(lines[-3])
    
