import pandas as pd

def txt_to_csv(file, csv_file):
    read_file = pd.read_csv(file)
    read_file.to_csv(csv_file, index=None)