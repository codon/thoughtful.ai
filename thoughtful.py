from enum import Enum

class Stack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

MAX_LENGTH = 150  # cm
MAX_VOLUME = 1_000_000  # cm^3
MAX_WEIGHT = 20.0  # kg

def sort(width: int, height: int, length: int, mass: float) -> str:
    bulk_mass, bulk_dimensions = False, False

    assert width > 0 and height > 0 and length > 0 and mass > 0.0

    bulk_dims = [cm for cm in [width, height, length] if cm >= MAX_LENGTH]

    if len(bulk_dims) > 0:
        bulk_dimensions = True
    elif length * width * height >= MAX_VOLUME:
        bulk_dimensions = True

    if mass >= MAX_WEIGHT:
        bulk_mass = True

    if bulk_mass and bulk_dimensions:
        return Stack.REJECTED
    if bulk_mass or bulk_dimensions:
        return Stack.SPECIAL

    return Stack.STANDARD

