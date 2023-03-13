from control.matlab import *
S1 = tf([0,1], [1,1])
S2 = tf([1,1], [1,1,1])
S = S2 * S1
print('S=', S)
S = series(S1, S2)
print('S=', S)

S = S1 + S2
print('S=', S)
S = parallel(S1, S2)
print('S=', S)

S = S1*S2 / (1 + S1 * S2)
print('S=', S)
S = feedback(S1*S2, 1)
print('S=', S)
print('S=', S.minreal())

S1 = tf(1, [1, 1])
S2 = tf(1, [1, 2])
S3 = tf([3,1], [1, 0])
S4 = tf([2,0], [0, 1])
S12 = feedback(S1, S2)
S123 = series(S12, S3)
S = feedback(S123, S4)
print('S=',S)