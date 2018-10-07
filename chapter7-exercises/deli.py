sandwhich_orders = ['pastrami', 'tuna', 'pastrami','turkey', 'ham', 'pastrami', 'pepperoni', 'salami']
finished_sandwhiches = []

print("The shop has run out of pastrami\n")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    sando = sandwhich_orders.pop()
    print("Your " + sando + " sandwhich is being prepared")
    finished_sandwhiches.append(sando)

for fs in finished_sandwhiches:
    print("Your " + fs + " has been prepared")