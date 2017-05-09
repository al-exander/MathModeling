from matplotlib import colors,pyplot
import numpy as np
import random

# -------------------------------------------------------------
# Adds at most 2500 drops of random size at random locations
# in the cloud. The drop sizes are taken from a normal
# distribution with an average drop size of 10 micrometers.
def makeDrops(cloud):
    initialDrops = np.random.normal(10, 1, 200)
    for i in range(0, 2500):
        m = random.randrange(0, 100)
        n = random.randrange(0, 100)
        if cloud[m][n] == 0:
            cloud[m][n] = random.choice(initialDrops)
    return cloud

# -------------------------------------------------------------
# Goes through each location in the cloud and moves a drop
# randomly in one of four directions. At the new location the
# drops join.
def motion(cloud):
    directions = ['up', 'down', 'left', 'right']
    for m in range(0, 100):
        for n in range(0, 100):
            if cloud[m][n] > 0:
                move = random.choice(directions)
                if move == 'up':
                    try:
                        cloud[m + 1][n] += cloud[m][n]
                        cloud[m][n] = 0
                    except IndexError, e:
                        pass
                elif move == 'down':
                    try:
                        cloud[m - 1][n] += cloud[m][n]
                        cloud[m][n] = 0
                    except IndexError, e:
                        pass
                elif move == 'left':
                    try:
                        cloud[m][n - 1] += cloud[m][n]
                        cloud[m][n] = 0
                    except IndexError, e:
                        pass
                elif move == 'right':
                    try:
                        cloud[m][n + 1] += cloud[m][n]
                        cloud[m][n] = 0
                    except IndexError, e:
                        pass
            else:
                pass
    return cloud
# -------------------------------------------------------------
# If drops are greater than 500 micrometers they "fall" out of
# the cloud. The simulation runs 500 times, at 250 random
# time steps more drops are added to the cloud.
def main():
    cloud = np.zeros((100, 100))
    cloud = makeDrops(cloud)
    image = 'image'
    simLength = range(0, 501)
    addDrops = sorted(random.sample(simLength, 251))
    c = 0

    for i in simLength:
        for m in range(0, 100):
            for n in range(0, 100):
                if cloud[m][n] > 500:
                    cloud[m][n] = 0

        if (i % 100) == 0:
            fig = pyplot.figure(c)
            cmap1 = colors.LinearSegmentedColormap.from_list('cloud', ['w', 'b'], 256)
            img1 = pyplot.imshow(cloud, interpolation = 'nearest', cmap = cmap1, origin = 'lower')
            pyplot.colorbar(img1, cmap = cmap1)
            fig.savefig(image + str(c) + '.png')
            #pyplot.show()
            c += 1
        if i in addDrops:
            cloud = makeDrops(cloud)
        cloud = motion(cloud)

main()
