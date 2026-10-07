from langsmith import traceable

PRODUCT_PRICE = {"laptop": 1200.00, "mouse": 10.00, "keyboard": 20.00}
DISCOUNT_TIER = {"silver": 10.00, "gold": 15.00, "platinum": 20.00}


@traceable(run_type="tool")
def get_product_price(product_name: str) -> float:
    """
    Lookup the price for a given product from the product price catalog
        Args:
            product_name: A string containing the name of the product for which the price to be identified
        Returns:
            The price of the product in a float number format

    """
    print(f"Finding the price for the product {product_name}")
    return PRODUCT_PRICE.get(product_name, 0.0)


@traceable(run_type="tool")
def apply_discount(price: str, discount_tier: str) -> float:
    """
    Apply the discount on the price based on the discout tier. Available tiers are silver, gold, and platinum
        Args:
            price: Original price of the product
            discount_tier: The total % of the doscount to be applied
        Returns:
            Discounted price of the product
    """
    price = float(price)
    return round(price - (price * (DISCOUNT_TIER.get(discount_tier, 0) / 100)), 2)
