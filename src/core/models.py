from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class ActivityRow(BaseModel):
    date: date
    business_unit: str

    electricity_kwh: float = 0
    natural_gas_kwh: float = 0

    diesel_l: float = 0
    petrol_l: float = 0
    flight_km: float = 0
    vehicle_km_wfo: float = 0  # work-from-office travel by km

    landfill_kg: float = 0
    recycle_kg: float = 0
    compost_kg: float = 0

class EmissionFactors(BaseModel):
    # Default placeholders (update for your grid/country!)
    electricity_kg_per_kwh: float = 0.7      # scope 2
    natural_gas_kg_per_kwh: float = 0.184    # scope 1

    diesel_kg_per_l: float = 2.68            # scope 1
    petrol_kg_per_l: float = 2.31            # scope 1
    vehicle_kg_per_km: float = 0.175         # average fleet (fallback)

    flight_kg_per_km: float = 0.15           # conservative avg

    landfill_kg_per_kg: float = 1.9          # methane rich
    recycle_kg_per_kg: float = 0.05          # processing footprint
    compost_kg_per_kg: float = 0.02

    year: Optional[int] = None
    region: Optional[str] = None
