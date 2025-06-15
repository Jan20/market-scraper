from dataclasses import dataclass


@dataclass
class Constituent:
    symbol: str
    name: str
    sector: str
    subIndustry: str = ""
