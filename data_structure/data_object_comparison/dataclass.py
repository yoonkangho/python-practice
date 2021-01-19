"""
Reference: https://docs.python.org/ko/3.8/library/dataclasses.html
"""
from dataclasses import dataclass
from timeit import default_timer


# object definition
@dataclass
class InventoryItem:

    id: int
    name: str
    size: str
    color: str
    unit_price: float
    quantity: int

obj_list = []


# average create time
count = 1000000
sum = 0

for i in range(count):
    start = default_timer()
    # notes: To be precise, we must eliminate object assignment as well.
    obj = InventoryItem(
        id=i,
        name='name',
        size='size',
        color='color',
        unit_price=0.12,
        quantity=123,
    )
    end = default_timer()
    sum += (end - start)
    obj_list.append(obj)

avg = sum / count * (10 ** 9)
print(f'dataclass create avg = {avg:.0f}ns')


# average access time
sum = 0
for i in range(count):
    obj = obj_list[i]

    start = default_timer()
    obj.id
    obj.name
    obj.size
    obj.color
    obj.unit_price
    obj.quantity
    end = default_timer()
    sum += (end - start)

avg = sum / count * (10 ** 9)
print(f'dataclass access time avg = {avg:.0f}ns')