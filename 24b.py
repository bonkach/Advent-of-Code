import copy
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
koo = dict()
for red in sve:
    x = y = z = 0
    i = 0
    red = red.strip()
    while i < len(red):
        if red[i] == 's':
            if red[i + 1] == 'e':
                z += 1
                y -= 1
                i += 2
            else:
                x -= 1
                z += 1
                i += 2
        elif red[i] == 'n':
            if  red[i + 1] == 'e':
                x += 1
                z -= 1
                i += 2
            else:
                y += 1
                z -= 1
                i += 2
        elif red[i] == 'w':
            x -= 1
            y += 1
            i += 1
        else:
            x += 1
            y -= 1
            i += 1
    if (x, y, z) not in koo:
        koo[(x, y, z)] = 1
    else:
        koo[(x, y, z)] = 0
b = 0
for vr in koo.values():
    if vr:
        b += 1
susjedi = [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]
for i in range(100):
    koo2 = copy.deepcopy(koo)
    for k in koo:
        for s in susjedi:
            if not koo.get((k[0] + s[0], k[1] + s[1], k[2] + s[2]), 0):
                koo2[k[0] + s[0], k[1] + s[1], k[2] + s[2]] = 0
    koo = copy.deepcopy(koo2)
    for k in koo:
        bb = 0
        for s in susjedi:
            if koo.get((k[0] + s[0], k[1] + s[1], k[2] + s[2]), 0):
                bb += 1
        if koo[k] and (bb == 0 or bb > 2):
            koo2[k] = 0
        if (not koo[k]) and bb == 2:
            koo2[k] = 1
    koo = copy.deepcopy(koo2)
b = 0
for vr in koo.values():
    if vr:
        b += 1
print(b)

