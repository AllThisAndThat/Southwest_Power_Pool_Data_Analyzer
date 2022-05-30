"""
Author: Lucas Hudson
Date: 5/29/22
Goal: Data object to store SPP data
"""
from dataclasses import dataclass, field

@dataclass
class SPP_Data_Time:
    year: int
    month: int
    day: int
    hour: int

    load: float = 0

    coal_market: float = 0
    coal_self: float = 0
    diesel_fuel_oil: float = 0
    hydro: float = 0
    natural_gas: float = 0
    nuclear: float= 0
    solar: float= 0
    waste_disposal: float = 0
    wind: float = 0
    waste_heat: float = 0
    other: float = 0

    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.month}/{self.day}/{self.year}"


        