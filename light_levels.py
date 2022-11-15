from numpy import log2

ISO = 100
C = 350


def exposure_value(N: float, t: float):
    """
    Parameters
    ----------
    N: float
        Aperture, from f/2 the N is 2
    t: float
        Exposure time / shutter time, from 1/48s the t is 48

    Returns
    -------
    EV: float
        Exposure value
    """

    return log2(N**2*t)


print(exposure_value(2.8, 48))

