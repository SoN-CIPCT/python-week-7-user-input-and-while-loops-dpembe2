pizza_orders = [
    "Pepperoni",
    "Supreme",
    "Taco",
    "Veggie",
    "Buffalo Chicken",
]
finished_pizzas = []
index = 0
while index < len(pizza_orders):
    print(f"{pizza_orders[index]}: Your pizza pie is finished!")
    index += 1
finished_pizzas.append(current_pizza)
