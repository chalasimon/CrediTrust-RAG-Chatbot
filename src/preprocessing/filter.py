TARGET_PRODUCTS = [
    'Credit card', 
    'Personal loan', 
    'Buy now, pay later',
    'Saving account', 
    'Money transfers'
]

def filter_data(df):
    """Filter to target products and valid narratives"""
    filtered = df[
        (df['Product'].isin(TARGET_PRODUCTS)) &
        (df['Consumer complaint narrative'].notna())
    ].copy()
    return filtered