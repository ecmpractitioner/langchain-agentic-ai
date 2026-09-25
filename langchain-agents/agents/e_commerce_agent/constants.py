from types import MappingProxyType
from typing import Final

PRODUCT_CATALOG: Final = MappingProxyType(
    {"laptop": 1200.00, "mouse": 25.00, "keyboard": 30.00}
)
DISCOUNT_TIER_PERCENTAGE: Final = MappingProxyType(
    {
        "silver": 10,
        "gold": 15,
        "platinum": 20,
    }
)
DEFAULT_MODEL: Final = "qwen3.5:4b"  # hardcoded here because I want to use ollama.
MAX_ITERATIONS: Final = 10
TEMPERATURE: Final[float] = 0.8
MODEL_PROVIDER: Final[str] = "OLLAMA"
