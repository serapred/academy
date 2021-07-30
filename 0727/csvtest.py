import csv

with open('../files/elderlyweights.csv') as csvf:
    reader = csv.reader(csvf, delimiter=' ')

    heights = ['Heights']
    weights = ['Weights']

    for row in reader:
        heights.append(row[2])
        weights.append(row[3])

print(heights)
print(weights)
