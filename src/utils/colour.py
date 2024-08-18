# each colour is a 3-tuple (R, G, B)

def brighten(colour, factor=0.1):
    return tuple(
        int(colourVal + (256-colourVal)*factor)
        for colourVal in colour
    )


def darken(colour, factor=0.1):
    return tuple(
        int(colourVal*(1-factor))
        for colourVal in colour
    )


# done by moving each R, G, B value closer to each other
# factor of 1 makes it grey
def desaturate(colour, factor=0.2):
    meanValue = sum(colour)/3
    return tuple(
        int(
            colourVal * (1-factor) + meanValue * factor
        )
        for colourVal in colour
    )


# idea: blending colours for borders?
# maybe make colour class