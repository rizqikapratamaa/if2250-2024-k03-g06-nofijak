import random

# Baca file input
inputfile = 'series.sql'
with open(inputfile, 'r') as f:
    lines = f.readlines()

# Acak urutan baris
random.shuffle(lines)

# Bagi menjadi dua bagian
third = len(lines) // 3
file1_lines = lines[:third]
file2_lines = lines[third:third*2]
file3_lines = lines[third*2:]

# Tulis ke file output
with open('file_output1.sql', 'w') as f:
    f.writelines(file1_lines)

with open('file_output2.sql', 'w') as f:
    f.writelines(file2_lines)

with open('file_output3.sql', 'w') as f:
    f.writelines(file3_lines)
