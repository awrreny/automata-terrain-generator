def printgrid(grid, binary=False):
    maxlen = 0

    #get longest item
    for row in grid:
        for tile in row:
            maxlen = max(maxlen, len(str(tile)))

    for row in grid:
        if binary:
            print(*[("██" if tile == 1 else " ") for tile in row],sep="")  #easier viewing of binary grids
        else:
            print(*[str(tile).ljust(maxlen) for tile in row])


# grid = [[1, 2], [3, 4]]
# printgrid(grid)

# grid = [["short", "longer"], ["tiny", "sizeable"]]
# printgrid(grid)

# grid = [[1, 2, 3], [4, 5]]
# printgrid(grid)

# grid = [["@", "#$%"], ["&", "*()"]]
# printgrid(grid)

# grid = [[1, "longstring"], [3.1415, None]]
# printgrid(grid)