from typing import List, Dict, Any, Optional

def calculate_average_order_value(orders: Optional[List[Dict[str, Any]]]) -> float:
    """
    Calculate the average order value from a list of orders, excluding cancelled orders.
    
    Args:
        orders: A list of dictionaries, each containing "status" and "amount" keys.
               
    Returns:
        float: The average order value of non-cancelled orders. Returns 0.0 if there are no valid orders.
    
    Notes:
        - Excludes orders with status "cancelled" (case-insensitive)
        - Skips orders with missing/invalid amounts or negative amounts
        - Handles edge cases: empty list, all cancelled, missing keys, invalid types
    """
    if orders is None:
        return 0.0
    
    try:
        iter(orders)
    except TypeError:
        return 0.0
    
    total = 0
    count = 0

    for order in orders:
        status = order.get("status")
        if status is None or str(status).lower() != "cancelled":
            amount = order.get("amount")
            if amount is not None and isinstance(amount, (int, float)) and amount >= 0:
                total += amount
                count += 1

    if count == 0:
        return 0.0
    
    return total / count
