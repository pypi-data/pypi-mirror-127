import numpy as np
import scipy.interpolate as si


def bspline(cv, n=10000, degree=3, periodic=False):
    """ Calculate n samples on a bspline

        Parameters
        ----------
        cv: array_like
            Array ov control vertices
        n: int
            Number of samples to return
        degree: int
            Curve degree
        periodic: bool
            True - Curve is closed, False - Curve is open
        Returns
        -------
        np.ndarray

        """

    # If periodic, extend the point array by count+degree+1
    cv = np.asarray(cv)
    count = len(cv)

    if periodic:
        factor, fraction = divmod(count + degree + 1, count)
        cv = np.concatenate((cv,) * factor + (cv[:fraction],))
        count = len(cv)
        degree = np.clip(degree, 1, degree)

    # If opened, prevent degree from exceeding count-1
    else:
        degree = np.clip(degree, 1, count - 1)

    # Calculate knot vector
    kv = None
    if periodic:
        kv = np.arange(0 - degree, count + degree + degree - 1, dtype='int')
    else:
        kv = np.concatenate(([0] * degree, np.arange(count - degree + 1), [count - degree] * degree))

    # Calculate query range
    u = np.linspace(periodic, (count - degree), n)

    # Calculate result
    return np.array(si.splev(u, (kv, cv.T, degree))).T
