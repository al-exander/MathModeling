import math
import matplotlib.pyplot as plt

def main():
    simLength = 120
    dt = 0.001
    time = [0]
    mass = 119
    accelGrav = 9.81
    springConstant = 40
    unWeightLength = 30
    weight = mass * accelGrav
    radius = .76

    velocity = [0]
    length = [0]

    weightDisplace = weight / springConstant
    projectedArea = math.pi * radius * radius
    airFriction = -0.65 * projectedArea * velocity[0] * math.fabs(velocity[0])

    if length[-1] > unWeightLength:
        restoringSpringForce = -springConstant * (length[-1] - unWeightLength)
    else:
        restoringSpringForce = 0
    force = weight + restoringSpringForce + airFriction
    acceleration = force / mass

    for i in range(1, int(simLength / dt) + 1):
        time.append(i * dt)
        velocity.append(velocity[i -1] + acceleration * dt)
        length.append(length[i - 1] + velocity[-1] * dt)

        if length[-1] > unWeightLength:
            restoringSpringForce = -springConstant * (length[-1] - unWeightLength)
        else:
            restoringSpringForce = 0

        airFriction = -0.65 * projectedArea * velocity[-1] * abs(velocity[-1])
        force = weight + restoringSpringForce + airFriction
        acceleration = force / mass

    plt.plot(time, length, 'k-', label = 'Length')
    plt.plot(time, velocity, 'g--', label = 'Velocity (per second)')
    plt.xlabel('Seconds')
    plt.ylabel('Meters')
    plt.title('A Model of a Bungee Jumper')
    plt.axis([0, simLength, min(velocity) - 10, max(length) + 10])
    legend = plt.legend(loc = 'upper right', shadow = True)
    frame =  legend.get_frame()
    frame.set_facecolor('0.90')
    for label in legend.get_texts():
        label.set_fontsize('large')
    for label in legend.get_lines():
        label.set_linewidth(1.5)
    plt.show()

main()
