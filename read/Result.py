from datetime import datetime
from xml.etree.ElementTree import Element
from .TypeTransformations import to_float


class Result:
    drug: str = ''
    istd: str = ''
    sample: str = ''
    time: datetime = datetime.fromisoformat('2000-01-01T05:00:00.0000000-05:00')
    type: str = ''
    drug_type: str = ''
    r2: float = 0
    rrt: float = 0
    rt: float = 0
    exp: float = 0
    min: float = 0
    max: float = 0
    conc: float = 0
    sn1: float = 0
    sn2: float = 0
    ir: float = 0
    target_area: float = 0
    qual_area: float = 0
    istd_area: float = 0

    def from_element(self, sample: Element, drug: Element):
        self.sample = sample.get('name')
        self.type = sample.get('type')
        self.drug = drug.get('name')
        self.drug_type = drug.get('type')
        self.exp = to_float(drug.attrib['stdconc'])

        data = drug.find('./PEAK')

        self.conc = to_float(data.attrib['analconc'])
        self.sn1 = to_float(data.attrib['signoise'])
        self.rt = to_float(data.attrib['foundrt'])
        self.target_area = to_float(data.attrib['area'])

        qual = data.find('./CONFIRMATIONIONPEAK1')
        if qual is not None:
            self.qual_area = to_float(qual.attrib['area'])
            self.sn2 = to_float(qual.attrib['signoise'])
            self.ir = to_float(qual.attrib['ionratio'])

        istd = data.find('./ISPEAK')
        self.istd_area = to_float(istd.attrib['area'])
        istd_rt = to_float(istd.attrib['foundrt'])
        self.rrt = self.rt / istd_rt if istd_rt > 0 else 0
