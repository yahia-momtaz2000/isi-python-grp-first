# calc discounts for order
item_cost = 200.0
item_qty = 3
special_client = 0  # 1:special     |0:not special
total_order_cost = item_cost * item_qty
discount_pct = 0
if total_order_cost >= 1000: # order will have discount 10% - 20%
    if special_client == 1:
        discount_pct = 20
    else:
        discount_pct = 10
discount_value = total_order_cost * discount_pct / 100
total_order_cost = total_order_cost - discount_value
print(discount_pct)
print(discount_value)
print(total_order_cost)

