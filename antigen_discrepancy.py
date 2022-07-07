import csv
from Bio import AlignIO
from difflib import SequenceMatcher


# QUESTIONS FOR DR. QUI
# In csv file, not every index is represented. Ex: first index is 4.

def win_read(fn):
    f = open(fn)

    csvreader = csv.reader(f)
    w = []
    for row in csvreader:
        w.append(row)

    f.close()
    return w


windows = win_read("windows.csv")
raw_window_data = win_read("combined_cor_analysis_results.csv")

filename = "sequence_data.aln"
alignment = AlignIO.read(filename, "clustal")

sequences = []
for i in alignment:
    sequences.append(i)

combos = [(a, b) for idx, a in enumerate(sequences) for b in sequences[idx + 1:]]


def tall_data():
    global combos, windows
    data = [["Start", "End", "#1", "#2", "Seq #1", "Seq #2", "Diff", "OD"]]
    for combo in combos:
        for win in windows:
            seq_1 = combo[0].seq[int(win[1]):int(win[2]) + 6 + 1]
            seq_2 = combo[1].seq[int(win[1]):int(win[2]) + 6 + 1]
            data.append([win[1], int(win[2]) + 6, combo[0].id, combo[1].id, str(seq_1), str(seq_2),
                         round(1.0 - SequenceMatcher(None, seq_1, seq_2).ratio(), 5)])

    with open('diff_output_tall.tsv', 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in data:
            tsv_output.writerow(row)


def wide_data():
    global combos, windows
    data = []
    for combo in combos:
        combo_data = [combo[0].id, combo[1].id]
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
