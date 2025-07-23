import time
from .utils import (
    get_large_transactions,
    analyze_transaction,
    notify_user,
    get_eth_price_usd,
)
import os

CHECK_INTERVAL = 30  # seconds

def start_monitoring():
    print("🐋 Запуск отслеживания китов на Ethereum...\n")
    while True:
        try:
            txs = get_large_transactions()
            for tx in txs:
                if tx["value_usd"] >= 1_000_000:
                    analysis = analyze_transaction(tx)
                    notify_user(tx, analysis)
        except Exception as e:
            print(f"Ошибка: {e}")
        time.sleep(CHECK_INTERVAL)
