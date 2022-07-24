# Enumeración implícita
# max Z = 3X1 - 2X2 + 5X3
# X1 + 2X2 - X3 <= 2
# X1 + 4X2 + X3 <= 4
# X1 + X2 <= 3
# 4X1 + X3 <= 6
# X1, X2, X3 = 0 o 1

objetivo = []
restricciones = []


import random as rd

def generateSequence(n):
    x = []
    x.append([0 for i in range(n)])
    xTran = []
    m = 0
    while len(x) != 2 ** n:
        for i in range(len(x)):
            for j in range(n):
                xTran.append(x[i][j])
            xTran[n - m - 1] = 1
            x.append(xTran)
            xTran = []
        m += 1
    return x

def judge(x):
    judge = None
    if x[0] + 2 * x[1] - x[2] <= 2 and x[0] + 4 * x[1] + x[2] <= 4 and x[0] + x[1] <= 3 and 4 * x[0] + x[2] <= 6:
        judge = True
    else:
        judge = False
    return judge

n = 3
solution = generateSequence(n)
zmax = -float("inf")
best = []
for x in solution:
    if judge(x):
        z = 3 * x[0] - 2 * x[1] + 5 * x[2]
        zmax = z
        break
for x in solution:
    z = 3 * x[0] - 2 * x[1] + 5 * x[2]
    if z > zmax:
        if judge(x):
            zmax = z
            best.append(x)
        else:
            continue
    else:
        continue
print("Solución óptima: x =",best[-1],"max z = ",zmax)