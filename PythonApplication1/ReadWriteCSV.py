max = 0.0
with open("sample.csv", "w") as f2:
    with open("aapl.csv", "r") as f:
        firstLine = f.readline()
        for line in f:
            f2.write(line+"\n")
            splitline = line.split(",")
            if float(splitline[4]) > max:
                max = float(splitline[4])
            #print(line)
    f.close()
f2.close()
print(max)