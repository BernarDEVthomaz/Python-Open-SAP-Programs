i = 0
with open("key.txt", "r") as key_file:
    for line in key_file:
        if i == 0:
            columns = int(line)
        else:
            lines = int(line)
        i = i + 1
with open("secret.txt", "r") as secret_file:
    secret_file_content = secret_file.readlines()
count = 1
i = 0
for line in secret_file_content:
    secret_file_content[i] = line.replace("\n", "")
    i = i + 1
i = 0
lengh = len(secret_file_content) - 1
with open("public.txt", "w") as public:    
    for line in range(lines):
        for column in range(columns):
            public.write(secret_file_content[i])
            i = i + 1
        if i != 0:
            public.write("\n")
