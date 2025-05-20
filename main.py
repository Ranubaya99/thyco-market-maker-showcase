from market_maker.monitor import get_price
from market_maker.strategy import calculate_optimal_trade
from market_maker.execution import execute_trade
import time

def run():
    while True:
        price = get_price("ETH")
        print(f"Current ETH price: {price}")

        inventory = {"ETH": 10, "USDC": 10000}
        trade_plan = calculate_optimal_trade(price, inventory)

        if trade_plan:
            execute_trade(trade_plan)
        time.sleep(30)

if __name__ == "__main__":
    run()
