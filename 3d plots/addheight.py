from copy import deepcopy

vtx = [
[550, 450],#0
[455, 519],#1
[491, 631],#2
[609, 631],#3
[645, 519],#4
]
n = len(vtx)
h = 350

vtx2 = [
[550, 450],#0
[455, 519],#1
[491, 631],#2
[609, 631],#3
[645, 519],#4
]
n = len(vtx2)
h = 350

def addvtx0():
    vtx = deepcopy(vtx2)
    vtxh = deepcopy(vtx2)
    for i in range(len(vtx)):
        a = vtx[i]
        a.append(0)
        b = vtxh[i]
        b.append(h)
        vtx.append(b)
    return vtx

vtx = addvtx0();
print(vtx)