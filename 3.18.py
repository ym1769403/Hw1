import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width

print('Wall area:', wall_area, 'square feet')

wall_paint = wall_area / 350
print('Paint needed:', '{:.2f}'.format(wall_paint), 'gallons')

paint_can = math.ceil(wall_paint)

print('Cans needed:', paint_can, 'can(s)')

paint_used = input('\nChoose a color to paint the wall:\n')
price = paint_colors[paint_used]
print('Cost of purchasing', paint_used, 'paint: $', price)
