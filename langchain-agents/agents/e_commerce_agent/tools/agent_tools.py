from langchain.tools import tool

PRODUCT_CATALOG = {"laptop": 1200.00, "mouse": 25.00, "keyboard": 30.00}
DISCOUNT_TIER_PERCENTAGE = {"silver": 10, "gold": 15, "platinum": 20}


@tool
def get_product_price(product: str) -> float:
    """
    Look up the price of product in the catalog
    Args:
        product: A string containing the name of the product for which price to be found
    Returns:
        Return the price of the product
    """
    print(f"Finding the price for the product {product}")
    return PRODUCT_CATALOG.get(product, 0)


@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """
    Apply the discount on the price based on the discout tier. Available tiers are silver, gold, and platinum
    Args:
        price: Original price of the product
        discount_tier: The total % of the doscount to be applied
    Returns:
        Discounted price of the product
    """
    return round(
        price - (price * (DISCOUNT_TIER_PERCENTAGE.get(discount_tier, 0) / 100)), 2
    )
