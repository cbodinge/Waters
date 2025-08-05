from pathlib import Path
from xml.etree import ElementTree as ET
from . import Result

def _read(path: Path):
    xml = ET.parse(path)
    root = xml.getroot()
    results = []

    for sample in root.findall(f"./GROUPDATA/GROUP/SAMPLELISTDATA/SAMPLE"):
        for drug in sample.findall('./COMPOUND'):
            result = Result()
            result.from_element(sample, drug)
            results.append(result)

    set_istds(results)
    set_limits(results)
    results = [result for result in results if result.drug_type=='']
    return results

def set_istds(results):
    drugs = {result.istd_area: result.drug for result in results if result.drug_type==''}
    istds = {result.target_area: result.drug for result in results if result.drug_type=='ISTD'}

    for istd_area, drug in drugs.items():
        istd = istds.get(istd_area)
        for result in [i for i in results if i.drug==drug]:
            result.istd = istd


def set_limits(results):
    for drug in {result.drug for result in results if result.drug_type == ''}:
        samples = [result for result in results if result.drug==drug]
        cals = [result.exp for result in samples if result.type=='Standard' and result.exp>0]
        _min = min(cals)
        _max = max(cals)
        for result in samples:
            result.min = _min
            result.max = _max



