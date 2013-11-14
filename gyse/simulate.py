
import numpy


def background_noise(mu, sigma, size):
    """
    Generates a matrix of `size`, filled with random noise. The random
    noise is generated with a gaussian distribution with the my and sigma
    parameters.

    :param mu: Mean ("centre") of the distribution.
    :param sigma: Standard deviation (spread or "width") of the distribution
    :param size: matrix size (square)
    :returns: a numpy matrix
    """
    return numpy.random.normal(loc=mu, scale=sigma, size=(size, size))


def generate_sources(count, flux_mu, flux_sigma, size):
    """
    generate a matrix containing random sources
    """
    fluxes = numpy.random.normal(loc=flux_mu, scale=flux_sigma, size=count)
    x = numpy.random.uniform(low=0, high=size, size=count)
    y = numpy.random.uniform(low=0, high=size, size=count)
    return numpy.vstack((fluxes, x, y))



if __name__ == '__main__':
    size = 1000
    print background_noise(1, 0.1, size)
    print generate_sources(100, 5, 0.2, size)
