import csv

def csv_slow_count_lines(filepath):
    """
    Counts lines by parsing the csv file line-by-line
    """
    with open(filepath, 'r') as file_ptr:
        csv_reader = csv.reader(file_ptr, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
    return line_count    