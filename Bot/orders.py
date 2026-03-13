from Bot.logging_config import setup_logger

logger = setup_logger()

def place_market_order(client, symbol, side, quantity):
    logger.info(f"Placing MARKET {side} order | Symbol: {symbol} | Qty: {quantity}")
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Order response: {response}")
        return response
    except Exception as e:
        logger.error(f"MARKET order failed: {e}")
        raise

def place_limit_order(client, symbol, side, quantity, price):
    logger.info(f"Placing LIMIT {side} order | Symbol: {symbol} | Qty: {quantity} | Price: {price}")
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"  # Good Till Cancelled
        )
        logger.info(f"Order response: {response}")
        return response
    except Exception as e:
        logger.error(f"LIMIT order failed: {e}")
        raise