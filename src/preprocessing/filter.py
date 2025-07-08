TARGET_PRODUCTS = [
    'Credit card', 
    'Personal loan', 
    'Payday loan',
    'Savings account', 
    'Money transfer'
]

def filter_data(df):
    """Filter to target products and valid narratives"""
    filtered = df[
        (df['Product'].isin(TARGET_PRODUCTS)) &
        (df['Consumer complaint narrative'].notna())
    ].copy()
    return filtered