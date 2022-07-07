import csv


def file_write(intervals, v, fn):
    writer = csv.writer(open(fn, 'w'), lineterminator='\n')
    for i in range(len(intervals)):
        if v[1][intervals[i][0]] < 0:
            writer.writerow([f"{int(i-i/2)}", f"{v[0][intervals[i][0]]}", f"{v[0][intervals[i][1]]}"])
