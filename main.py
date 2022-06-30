import matplotlib.pyplot as plt
import csv
from text_to_csv import txt_to_csv


def plot(p, b_p):
    plt.xlabel("Window Start")
    plt.ylabel("Binary Correlation Coefficient")
    plt.title("Runs of Positive and Negative Correlations")
    plt.yticks([-0.25, 0, 0.25])

    plt.axhline(y=0, color="r", linestyle='dashed')
    plt.plot(p[1], label="cor coef")
    plt.plot(b_p[1], label="window")
    plt.plot(0.35)

    plt.legend(loc="upper left")
    plt.savefig('plot1.png')


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


data = []
with open('combined_cor_analysis_results.csv', newline='') as csvfile:
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
            b_points[1].append(0.25)
        else:
            b_points[1].append(-0.25)

plot(points, b_points)
