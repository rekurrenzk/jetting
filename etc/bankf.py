csv_path = "csv2.csv"
encoding = 'ISO-8859-1'  # Or any other encoding that works

with open(csv_path, 'r', encoding=encoding, errors='replace') as file:
    for line in file:
        print(line)
