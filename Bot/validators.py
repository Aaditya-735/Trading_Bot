VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")
    
    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Side must be BUY or SELL, got: {side}")
    
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError(f"Order type must be MARKET or LIMIT, got: {order_type}")
    
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0.")
    
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if float(price) <= 0:
            raise ValueError("Price must be greater than 0.")