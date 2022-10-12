"""Second assignment of CMEPDA Course, 2022/2023"""

import logging
import math


conv_MeV_kg = 1.78*10**(-30)
c = 2.99792458*10**8


class Particle:
    """Class describing a generic particle"""
    def __init__(self, name, mass, charge, beta=0.):
        self.name = str(name)

        self.mass = mass
        if self.mass < 0:
            logging.error(' Mass value not acceptable')
            exit()

        self.charge = charge
        if type(self.charge) != int:
            logging.error(' Charge value not acceptable')
            exit()

        self.beta = beta
        if self.beta < 0 or self.beta > 1:
            logging.error(' Lorentz factor value not acceptable')
            exit()

    @property
    def gamma(self):
        return math.sqrt(1/(1-(self.beta**2)))

    @gamma.setter
    def gamma(self, gamma):
        self.beta = math.sqrt(1-(1/(gamma**2)))

    @property
    def momentum(self):
        return self.beta*self.gamma*self.mass*conv_MeV_kg*c

    @momentum.setter
    def momentum(self, momentum):
        self.beta = momentum/(self.gamma*self.mass*conv_MeV_kg*c)

    @property
    def energy(self):
        return (self.gamma-1)*self.mass

    @energy.setter
    def energy(self, energy):
        self.gamma = (energy/self.mass)+1

    def __repr__(self):
        return 'Particle name: {} \n' \
               'Particle mass: {}MeV/c^2 \n' \
               'Particle charge: {}e \n' \
               'Particle Lorentz factor: {} \n'.format(self.name, self.mass, self.charge, self.beta)


class Proton(Particle):
    """Class describing a proton. It inherits from class Particle"""
    def __init__(self, beta=0.):
        Particle.__init__(self, 'Proton', 939.3, 1, beta)

    def __repr__(self):
        return Particle.__repr__(self)


class Alpha(Particle):
    """Class describing a proton. It inherits from class Particle"""
    def __init__(self, beta=0.):
        Particle.__init__(self, 'Alpha', 3727.4, 2, beta)

    def __repr__(self):
        return Particle.__repr__(self)


if __name__ == '__main__':
    electron = Particle('Electron', 0.511, -1, 0.5)
    print(electron)

    proton = Proton()
    print(proton)

    alpha = Alpha()
    print(alpha)

    print(electron.gamma)
