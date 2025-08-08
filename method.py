from csv import writer
from read import results
from pathlib import Path

def to_csv(path: Path):
    _results = results(path)
    _results = list(set((i.drug, i.istd, i.min, i.max) for i in _results))
    _results.sort()
    output = 'C:/Coding Projects/Waters/output/output_method.csv'
    with open(output, 'w', newline='') as file:
        csv = writer(file)
        csv.writerow(['Drug', 'ISTD', 'Min', 'Max'])
        for result in _results:
            csv.writerow(result)
