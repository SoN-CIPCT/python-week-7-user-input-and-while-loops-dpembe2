pizza_orders = [
    "Pepperoni",
    "Supreme",
    "Taco",
    "Veggie",
    "Buffalo Chicken",
]
finished_pizzas = []
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print(f"{current_pizza}: Your pizza pie is finished!")
finished_pizzas.append(current_pizza)
