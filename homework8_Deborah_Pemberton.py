pizza_orders = [
    {'name': "Pepperoni"},
   {'name': "Supreme"},
    {'name': "Taco"},
    {'name': "Veggie"},
    {'name': {"Buffalo Chicken"}
]
finished_pizzas = []
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print(f"{current_pizza}: Your pizza pie is finished!")
finished_pizzas.append(current_pizza)
index = 0
while index < len(finished_pizzas):
    print(f"The pizza {finished_pizzas['name']} was made.")
    index += 1
