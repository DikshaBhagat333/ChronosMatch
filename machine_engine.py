import heapq
from typing import NamedTuple, List

from order_manager import OrderManager, BUY, SELL



class Trade(NamedTuple):
    trade_id: int
    buy_id: object
    sell_id: object
    price: float
    quantity: int