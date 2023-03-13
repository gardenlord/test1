from control.matlab import *
Np = [0, 1]
Dp = [1, 2, 3]
P = tf(Np, Dp)
print(P)

P = tf([1,3], [1,5,8,4])
print(P)

P1 = tf([1,3], [0,1])
P2 = tf([0,1], [1,1])
P3 = tf([0,1], [1,2])
P = P1 * P2 * P3 ** 2
print(P)
print(P.num)
print(P.den)

[[numP]], [[denP]] = tfdata(P)
print(numP)
print(denP)