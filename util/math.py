import numpy as np


def earth_radius():
    return 6371


def degree_to_radian(degree):
    return 2 * degree * np.pi / 360


def harversine(first_coord, last_coord):
    r = earth_radius()
    first_coord, last_coord = list(first_coord), list(last_coord)
    first_rads = list(map(degree_to_radian, first_coord))
    final_rads = list(map(degree_to_radian, last_coord))
    delta_phi = final_rads[0] - first_rads[0]
    delta_lambda = first_rads[1] - final_rads[1]
    h = np.power(np.sin(delta_phi/2), 2) + np.cos(first_rads[0]) * np.cos(final_rads[0]) * \
        np.power(np.sin(delta_lambda/2), 2)
    return 2*r*np.arcsin(np.sqrt(h))
