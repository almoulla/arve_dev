import numpy as np


class inverted_gaussian:
    def inverted_gaussian(self, x: np.ndarray, *params: tuple) -> list:
        """Inverted Gaussian.

        :param x: RV array
        :type x: list
        :param params: tuple with continuum, contrast, RV and FWHM
        :type params: tuple of floats
        :return: inverted Gaussian evaluated at x
        :rtype: list
        """
        # unpack parameters
        continuum, contrast, RV, FWHM = params

        # rename parameters
        C = continuum
        a = contrast
        b = RV
        c = FWHM

        # scale FWHM into sigma
        c /= 2 * np.sqrt(2 * np.log(2))

        return C - a * np.exp(-(((x - b) / c) ** 2) / 2)
