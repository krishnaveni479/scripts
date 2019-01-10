file1 = set(line.strip() for line in open("file1.txt"))
file2 = set(line.strip() for line in open("file2.txt"))
for line in file1 & file2:
        if line:
             print line


