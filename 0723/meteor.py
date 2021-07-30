"""
Meteor

In a video game, a meteor will fall toward the main character's home planet. Given the meteor's
trajectory as a string in the form y = mx + b and the character's position as a tuple of (x, y), return True
if the meteor will hit the character and False if it will not.
Examples
will_hit("y = 2x - 5", (0, 0)) ➞ False
will_hit("y = -4x + 6", (1, 2)) ➞ True
will_hit("y = 2x + 6", (3, 2)) ➞ False
Notes
The b value will never be zero or blank.
The m value will always be an integer.
If the m value is 1, the "1" will be shown.
For example, "y = x + 5" will be shown as "y = 1x + 5".
If the m value is -1, the "-1" will be shown.
For example, "y = -x + 2" will be shown as "y = -1x + 2".

"""


def collision(traj, planet):
    # naive
    traj = traj.replace('x', f'*{planet[0]}')
    traj = traj.replace('y', f'{planet[1]}')
    traj = traj.replace('=', '==')

    return eval(traj)


def parse_eq(e):

    mi = e.index('=') + 1
    mj = e.index('x')
    qi = e.rindex(' ')
    return int(e[mi:mj]), int(e[qi - 1] + e[qi + 1:])


def linear(m, q, planet):
    return planet[1] == (planet[0] * m) + q


def collision(traj, planet):
    # marginally less naive
    return linear(*parse_eq(traj), planet)


if __name__ == '__main__':

    # a regex should be used for string validation...
    from sys import argv
    planet = (4, 2)
    ans = 'not' if collision(argv[1], planet) else ''
    print(f"the planet is {ans} safe")
