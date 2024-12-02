line = [8,7,9,2,5,3,56,43,32,59,1,9]

status = True
last = len(line) - 1
while last > 0 and status:
    status = False
    for i in range(last):
        if line[i] > line[i+1]:
            line[i], line[i+1] = line[i+1], line[i]
            status = True
    last = last - 1
print(line)
