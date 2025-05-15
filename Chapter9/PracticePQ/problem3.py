#3. Write a program to generate multiplication tables from 2 to 20 and write it to different files. Place these files in a folder for a 13-year-old.

import os

folder = "MultiplicationTables"
os.makedirs(folder, exist_ok=True)

for i in range(2, 21):
    with open(f"{folder}/table_of_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
