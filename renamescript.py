import os

for i in range(2015, 2024):
    i = str(i)
    for folder in os.listdir(os.path.join(os.getcwd(), i)):
        for folder1 in os.listdir(os.path.join(os.getcwd(), i, folder)):
            os.delete(os.path.join(os.getcwd(), i, folder, folder1, "input.txt"))
