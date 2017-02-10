v = open('C:/test/test.csv')
r = csv.reader(v)
row0 = r.next()
row0.append('berry')
print row0

for item in r:
    item.append(item[0])
    print item