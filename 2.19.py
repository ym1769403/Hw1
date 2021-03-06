lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
amount_servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', ('{:.2f}'.format(amount_servings)), 'servings')
print(('{:.2f}'.format(lemon_juice_cups)), 'cup(s) lemon juice')
print(('{:.2f}'.format(water_cups)), 'cup(s) water')
print(('{:.2f}'.format(nectar_cups)), 'cup(s) agave nectar')

customer_servings = int(input('\nHow many servings would you like to make?\n'))
calc_servings = customer_servings / amount_servings
calc_lemon_juice_cups = calc_servings * lemon_juice_cups
calc_water_cups = calc_servings * water_cups
calc_nectar_cups = calc_servings * nectar_cups

print('\nLemonade ingredients - yields', ('{:.2f}'.format(customer_servings)), 'servings')
print(('{:.2f}'.format(calc_lemon_juice_cups)), 'cup(s) lemon juice')
print(('{:.2f}'.format(calc_water_cups)), 'cup(s) water')
print(('{:.2f}'.format(calc_nectar_cups)), 'cup(s) agave nectar')

gal_lemonjuice = calc_lemon_juice_cups / 16
gal_water = calc_water_cups / 16
gal_nectar = calc_nectar_cups / 16

print('\nLemonade ingredients - yields', '{:.2f}'.format(customer_servings), 'servings')
print(('{:.2f}'.format(gal_lemonjuice)), 'gallon(s) lemon juice')
print(('{:.2f}'.format(gal_water)), 'gallon(s) water')
print(('{:.2f}'.format(gal_nectar)), 'gallon(s) agave nectar')
