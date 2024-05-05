import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def create_truchet_tile(ax, tile_type, x_offset, y_offset):
    """ Create a Truchet tile at position (x_offset, y_offset) on the given axes based on the tile type. """
    """
    Rules to draw the tile:
    # sum of indexes (x,y) Even and the value = 0 -> background color: black, circle color: white, pos 0,1 1,0  === 0
    # sum of indexes (x,y) Odd and the value = 0  -> background color: white, circle color: black, pos 0,1 1,0  === 1
    # sum of indexes (x,y) Even and the value = 1 -> background color: white, circle color: black, pos 0,0 1,1  === 2
    # sum of indexes (x,y) Odd and the value = 1  -> background color: black, circle color: white, pos 0,0 1,1  === 3 
    """
    # Determine the background and circle colors
    background_color = 'black' if tile_type in [0, 3] else 'white'
    circle_color = 'black' if tile_type in [1, 2] else 'white'

    # Set background by adding a Rectangle that covers the tile
    ax.add_patch(Rectangle((x_offset, y_offset), 1, 1, color=background_color))

    # Define the positions for the disks based on the tile type
    positions = [(0, 0), (1, 1)] if tile_type in [2, 3] else [(0, 1), (1, 0)]
    
    # Add disks to the plot
    for pos in positions:
        circle_x = pos[0] + x_offset
        circle_y = pos[1] + y_offset
        circle = Circle((circle_x, circle_y), 0.5, color=circle_color)
        ax.add_patch(circle)

def binary_ascii_conversion(text):
    """ Convert text to a grid of binary values based on ASCII. """
    return [format(ord(char), '08b') for char in text]

def plot_truchet_from_string(text):
    binary_grid = binary_ascii_conversion(text)
    rows = len(binary_grid)
    cols = len(binary_grid[0])

    fig, ax = plt.subplots(figsize=(cols, rows))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw each tile directly onto the single Axes object
    for i, row in enumerate(binary_grid):
        for j, bit in enumerate(row):
            tile_type = (i + j) % 2 + 2 * int(bit)
            create_truchet_tile(ax, tile_type, j, rows - i - 1)  # flip y-axis to align the origin at the top-left corner

    plt.show()

plot_truchet_from_string("hello world!")
