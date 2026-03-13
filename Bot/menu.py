from Bot.logging_config import setup_logger

logger = setup_logger()

# ── ANSI color codes ──────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

VALID_SYMBOLS    = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
VALID_SIDES      = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def print_banner():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════╗
║   🤖  Binance Futures Trading Bot        ║
║        Testnet (USDT-M)                  ║
╚══════════════════════════════════════════╝{RESET}
""")


def print_menu():
    print(f"{BOLD}{'─'*44}{RESET}")
    print(f"  {CYAN}1.{RESET} Place an Order")
    print(f"  {CYAN}2.{RESET} Exit")
    print(f"{BOLD}{'─'*44}{RESET}")


def get_validated_input(prompt, valid_options=None, input_type=float, allow_none=False):
    """
    Generic input helper with inline validation messages.
    - valid_options: list of allowed string values (case-insensitive)
    - input_type: float or str
    - allow_none: if True, empty input returns None (used for optional price)
    """
    while True:
        raw = input(f"{YELLOW}  ➤ {prompt}{RESET}").strip()

        # Handle optional fields
        if allow_none and raw == "":
            return None

        # Validate against allowed options
        if valid_options:
            if raw.upper() in valid_options:
                return raw.upper()
            else:
                print(f"{RED}  ✗ Invalid input. Choose from: {', '.join(valid_options)}{RESET}")
                continue

        # Validate numeric input
        if input_type == float:
            try:
                value = float(raw)
                if value <= 0:
                    print(f"{RED}  ✗ Value must be greater than 0.{RESET}")
                    continue
                return value
            except ValueError:
                print(f"{RED}  ✗ Please enter a valid number.{RESET}")
                continue

        return raw


def collect_order_inputs():
    """Interactively collect and validate all order fields."""
    print(f"\n{BOLD}  📋 Enter Order Details{RESET}")
    print(f"{'─'*44}")

    symbol     = get_validated_input("Symbol      (e.g. BTCUSDT): ", valid_options=VALID_SYMBOLS, input_type=str)
    side       = get_validated_input("Side        (BUY / SELL)  : ", valid_options=VALID_SIDES,   input_type=str)
    order_type = get_validated_input("Order Type  (MARKET/LIMIT): ", valid_options=VALID_ORDER_TYPES, input_type=str)
    quantity   = get_validated_input("Quantity    (e.g. 0.01)   : ", input_type=float)

    price = None
    if order_type == "LIMIT":
        price = get_validated_input("Price       (e.g. 50000)  : ", input_type=float)

    return symbol, side, order_type, quantity, price


def print_order_summary(symbol, side, order_type, quantity, price):
    print(f"\n{BOLD}{'─'*44}")
    print(f"  📤 Order Request Summary")
    print(f"{'─'*44}{RESET}")
    print(f"  Symbol     : {CYAN}{symbol}{RESET}")
    print(f"  Side       : {GREEN if side == 'BUY' else RED}{side}{RESET}")
    print(f"  Type       : {order_type}")
    print(f"  Quantity   : {quantity}")
    print(f"  Price      : {price if price else 'N/A (MARKET)'}")
    print(f"{BOLD}{'─'*44}{RESET}\n")


def print_order_response(response):
    print(f"\n{GREEN}{BOLD}  ✅ Order Placed Successfully!{RESET}")
    print(f"{BOLD}{'─'*44}{RESET}")
    print(f"  Order ID   : {response.get('orderId')}")
    print(f"  Status     : {response.get('status')}")
    print(f"  Executed   : {response.get('executedQty')}")
    print(f"  Avg Price  : {response.get('avgPrice', 'N/A')}")
    print(f"{BOLD}{'─'*44}{RESET}\n")


def print_error(message):
    print(f"\n{RED}{BOLD}  ✗ Error: {message}{RESET}\n")