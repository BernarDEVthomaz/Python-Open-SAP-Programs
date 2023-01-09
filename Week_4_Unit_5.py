with open("invoice_data.txt", "r") as file:
    for line in file:
        line = line.split()
        line[0] = str(line[0])
        line[1] = int(line[1])
        line[2] = float(line[2])
        print(
            f"{line[0]:15s}{line[1]:3d}{line[2]:7.2f}{line[1]*line[2]:8.2f}"
        )
