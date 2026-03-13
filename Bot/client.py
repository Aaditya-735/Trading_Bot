import time
import requests
from binance.client import Client
from Bot.logging_config import setup_logger
from dotenv import dotenv_values

logger = setup_logger()

env_vars = dotenv_values(".env")
API_KEY = env_vars.get("Binance_API_KEY")
API_SECRET = env_vars.get("Binance_API_SECRET")

def get_server_time_offset():
    """Fetch Binance testnet server time and calculate offset."""
    try:
        response = requests.get("https://testnet.binancefuture.com/fapi/v1/time")
        server_time = response.json()["serverTime"]
        local_time = int(time.time() * 1000)
        offset = server_time - local_time
        logger.info(f"Time offset calculated: {offset}ms")
        return offset
    except Exception as e:
        logger.warning(f"Could not fetch server time, using 0 offset: {e}")
        return 0

def get_client():
    try:
        client = Client(
            api_key=API_KEY,
            api_secret=API_SECRET,
            testnet=True
        )
        # Auto-sync with Binance server time
        client.timestamp_offset = get_server_time_offset()
        logger.info("Binance Futures Testnet client initialized.")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize client: {e}")
        raise