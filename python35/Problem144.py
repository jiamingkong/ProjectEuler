from math import sqrt


result = 0

xA = 0.
yA = 10.1

x0 = 1.4
y0 = -9.6

while x0 > 0.01 or x0 < -0.01 or y0 < 0:
    slopeA = (y0 - yA) / (x0 - xA)
    slope0 = -4 * x0 / y0

    tanA = (slopeA - slope0) / (1 + slopeA * slope0)
    slopeB = (slope0 - tanA) / (1 + tanA * slope0)

    interceptB = y0 - slopeB * x0

    a = 4 + slopeB * slopeB
    b = 2 * slopeB * interceptB
    c = interceptB * interceptB - 100

    ans1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    ans2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)

    xA = x0
    yA = y0

    x0 = abs(ans1 - x0) > abs(ans2 - x0) and ans1 or ans2
    y0 = slopeB * x0 + interceptB

    result += 1

print(result)