with open("numbers.txt", "r") as file:
    with open("even_numbers.txt","w") as file2:
        for line in file:
            file2.write(line)
print("List of even numbers created!")
