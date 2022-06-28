import matplotlib.pyplot as plt
import csv
import random


def rand_binary():
    binary_string = ""
    for _ in range(int(input("Length of binary string: "))):
        binary_string = binary_string + str(random.randint(0, 1))


def binary_plot(p):
    plt.plot(p[1])
    plt.yticks([-1, 0, 1])
    plt.xlabel("Window Start")
    plt.ylabel("Binary Correlation Coefficient")
    plt.title("Runs of Positive and Negative Correlations")


def intervals(s, min):
    inter = []

    for i in range(len(s)):
        start = i
        end = i
        if i == 0 or (float(s[i][1]) > 0) != (float(s[i - 1][1]) > 0):
            if i + 1 <= len(s) - 1:
                while (float(s[end][1]) > 0) == (float(s[end + 1][1]) > 0):
                    if end + 1 >= len(s) - 1:
                        end = len(s) - 1
                        break
                    else:
                        end += 1
            if end - start >= min - 1:
                inter.append((start, end))

    return inter


def float_plot(p):
    plt.plot(p[1])
    plt.yticks([-1, 0, 1])
    plt.xlabel("Window Start")
    plt.ylabel("Correlation Coefficient")
    plt.title("Runs of Positive and Negative Correlations")
    plt.savefig("plot.png")


data = []
with open('data.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in d:
        data.append(row)

ints = intervals(data, 0)

points = [[], []]
b_points = [[], []]
for i in ints:
    for j in range(i[0], i[1] + 1):
        points[0].append(data[j][0])
        points[1].append(round(float(data[j][1]), 2))
        b_points[0].append(data[j][0])
        if float(data[j][1]) > 0:
            b_points[1].append(1)
        else:
            b_points[1].append(-1)

print(points)
binary_plot(b_points)
float_plot(points)
