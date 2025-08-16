import pandas as pd

# Mapping CFPB product names to your target categories
PRODUCT_MAPPING = {
    # Credit card
    "Credit card": "Credit card",
    "Credit card or prepaid card": "Credit card",

    # Personal loan
    "Payday loan, title loan, or personal loan": "Personal loan",
    "Payday loan, title loan, personal loan, or advance loan": "Personal loan",
    "Consumer Loan": "Personal loan",

    # Savings account
    "Checking or savings account": "Saving account",
    "Bank account or service": "Saving account",

    # Money transfers
    "Money transfer, virtual currency, or money service": "Money transfers",
    "Money transfers": "Money transfers",

    # Potential BNPL (Buy Now, Pay Later) mappings
    # Note: not explicit in CFPB dataset, but may appear grouped here
    "Credit card or prepaid card": "Buy now, pay later",
    "Consumer Loan": "Buy now, pay later",
}

# Target product categories (after mapping)
TARGET_PRODUCTS = [
    "Credit card",
    "Personal loan",
    "Buy now, pay later",
    "Saving account",
    "Money transfers",
]

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """Map product names, filter to target products, and drop empty narratives"""
    df = df.copy()

    # Map products to standardized categories
    df["MappedProduct"] = df["Product"].map(PRODUCT_MAPPING)

    # Keep only target categories + valid narratives
    filtered = df[
        (df["MappedProduct"].isin(TARGET_PRODUCTS)) &
        (df["Consumer complaint narrative"].notna())
    ].copy()

    return filtered
