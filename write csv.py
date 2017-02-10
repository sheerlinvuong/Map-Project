import csv

with open('C:\Users\soapz_000\Documents\map project\square.csv','r') as csvinput:
    with open('C:\Users\soapz_000\Documents\map project\output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('Berry')
        all.append(row)

        for row in reader:
            row.append(row[0])
            all.append(row)

        writer.writerows(all)

all = []
row = node_id
row.append(str(node_lat) + "\n")
all.append(row)

# row in writer:
row.append(row[0])
# all.append[row]

writer.writerows(all)
# file.write(str(node_id) + "\n")
# row = next(writer)
# row.append(file.write(str(node_lat) + "\n"))