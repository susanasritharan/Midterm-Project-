import csv

# Step 1: Reading CSV File
with open('data.csv', 'r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    for line in fCSV:
        print(line)

# Step 2: Total Sale

with open('data.csv', 'r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    next(fCSV)
    totalsale = {}
    for line in fCSV:
        year = line[0]
        if year =="2022":
         continue
        values = line[1:]
        total = sum(int(v) for v in values if v)
        totalsale[year] = total
    with open('stats.txt', 'w') as file:
        for year, total in totalsale.items():
            file.write(f"{year}: {total}\n")

# Step 3: Bar Plot
import matplotlib.pyplot as plt

x = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
y = [1665063, 1728140, 1851645, 1867498, 1948375, 2029668, 1987373, 1921449, 1661560, 1638349]

plt.figure(1)
plt.bar(x,y)

plt.title ("Total Sales")
plt.xlabel("Year")
plt.ylabel("Total Amount")

plt.show()


