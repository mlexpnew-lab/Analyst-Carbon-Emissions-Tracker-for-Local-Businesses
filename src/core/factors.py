import json
from pathlib import Path
from .models import EmissionFactors

DEFAULTS = EmissionFactors()

def load_factors(path: Path | None = None) -> EmissionFactors:
    if path and path.exists():
        data = json.loads(path.read_text())
        return EmissionFactors(**data)
    return DEFAULTS

def save_factors(factors: EmissionFactors, path: Path):
    path.write_text(factors.model_dump_json(indent=2))
