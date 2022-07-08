import csv
from Bio import AlignIO
from difflib import SequenceMatcher


# QUESTIONS FOR DR. QUI
# In csv file, not every index is represented. Ex: first index is 4.

def win_read(fn, remove_first=False):
    f = open(fn)

    csvreader = csv.reader(f)
    w = []
    for row in csvreader:
        w.append(row)

    f.close()
    if remove_first:
        del w[0]

    return w


windows = win_read("windows.csv")

filename = "sequence_data.aln"
alignment = AlignIO.read(filename, "clustal")

combos = []
for i in alignment:
    for j in alignment:
        if i.id != j.id:
            combos.append((i, j))

ODs_raw = win_read("OD_data.csv", True)
ODs = {}

x = 0
for i in ODs_raw:
    if (i[0], i[3].replace("anti-", "")) in ODs:
        ODs[(i[0], i[3].replace("anti-", ""))].append(i[7])
    else:
        ODs[(i[0], i[3].replace("anti-", ""))] = [i[7]]


def tall_data():
    data = []
    for combo in combos:
        for od in ODs[(combo[0].id, combo[1].id)]:
            for win in windows:
                seq_1 = combo[0].seq[int(win[1]):int(win[2]) + 6 + 1]
                seq_2 = combo[1].seq[int(win[1]):int(win[2]) + 6 + 1]
                data.append([combo[0].id, combo[1].id, od, win[1], int(win[2]) + 6, str(seq_1), str(seq_2),
                             round(1.0 - SequenceMatcher(None, seq_1, seq_2).ratio(), 5)])

    with open('diff_output_tall.tsv', 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in data:
            tsv_output.writerow(row)


def wide_data():
    data = []
    for combo in combos:
        for od in ODs[(combo[0].id, combo[1].id)]:
            combo_data = [combo[0].id, combo[1].id, od]
            for win in windows:
                seq_1 = combo[0].seq[int(win[1]):int(win[2]) + 6 + 1]
                seq_2 = combo[1].seq[int(win[1]):int(win[2]) + 6 + 1]
                combo_data.append(round(1.0 - SequenceMatcher(None, seq_1, seq_2).ratio(), 5))
            data.append(combo_data)

    with open('diff_output_wide.tsv', 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in data:
            tsv_output.writerow(row)


tall_data()
wide_data()
