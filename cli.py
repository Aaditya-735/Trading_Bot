from Bot.client import get_client
from Bot.orders import place_market_order, place_limit_order
from Bot.logging_config import setup_logger
from Bot.menu import (
    print_banner,
    print_menu,
    collect_order_inputs,
    print_order_summary,
    print_order_response,
    print_error
)

logger = setup_logger()


def run():
    print_banner()

    while True:
        print_menu()
        choice = input("\033[96m  Enter choice (1/2): \033[0m").strip()

        if choice == "2":
            print("\n\033[93m  👋 Exiting. Goodbye!\033[0m\n")
            break

        elif choice == "1":
            try:
                # Collect inputs interactively
                symbol, side, order_type, quantity, price = collect_order_inputs()

                # Show summary before placing
                print_order_summary(symbol, side, order_type, quantity, price)

                # Confirm before placing
                confirm = input("\033[93m  Confirm order? (yes/no): \033[0m").strip().lower()
                if confirm not in ("yes", "y"):
                    print("\n\033[91m  ✗ Order cancelled.\033[0m\n")
                    continue

                # Place order
                client = get_client()
                logger.info(f"Order confirmed by user: {symbol} {side} {order_type} qty={quantity} price={price}")

                if order_type == "MARKET":
                    response = place_market_order(client, symbol, side, quantity)
                else:
                    response = place_limit_order(client, symbol, side, quantity, price)

                print_order_response(response)

            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                print_error(str(e))

        else:
            print("\n\033[91m  ✗ Invalid choice. Please enter 1 or 2.\033[0m\n")


if __name__ == "__main__":
    run()