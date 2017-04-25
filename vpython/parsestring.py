def findLargestNumber(text):
    ls = list()
    for w in text.split():
        try:
            ls.append(int(w))
        except:
            pass
    try:
        return max(ls)
    except:
        return None

print (findLargestNumber('I saw 3 dogs, 17 cats, and 14 cows!'))
print (findLargestNumber('0;-1'))

v="3.5;0;-1"
v_split = v.split(";")
v = max(v_split)
print(str(v))