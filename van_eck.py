"""
Program to produce van eck sequence
"""
import matplotlib.pyplot as plt


def van_eck(start, iterations):
    van_list = [start]
    highest = [0]
    for i in range(iterations):
        for j in range(i-1, -1, -1):
            if van_list[i] == van_list[j]:
                van_list.append(i-j)
                if (i-j) > highest[-1]:
                    highest.append(i-j)
                else:
                    highest.append(highest[-1])
                break
        else:
            van_list.append(0)
            highest.append(highest[-1])

    return van_list, highest


def derivative(van_eck_list):
    van_der = []
    for i in range(1, len(van_eck_list)):
        van_der.append(van_eck_list[i] - van_eck_list[i-1])
    return van_der


van1, highest1 = van_eck(1, 100000)
vander = derivative(van1)

plt.figure(1)
plt.subplot(int(211))
plt.plot(van1)
plt.subplot(212)
plt.plot(vander)

plt.figure(1)
plt.subplot(211)
plt.plot(highest1)

plt.show()
