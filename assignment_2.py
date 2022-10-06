"""Second assignment of CMEPDA Course, 2022/2023"""

import logging


class Particle:
    """Class describing a generic particle"""
    def __init__(self, name, mass, charge):
        self.name = str(name)
        self.mass = mass
        if self.mass < 0:
            logging.error(' Mass value not acceptable')
            exit()
        self.charge = charge
        if type(self.charge) != int:
            logging.error(' Charge value not acceptable')
            exit()

    def __repr__(self):
        return 'Particle name: {} \nParticle mass: {}MeV \nParticle charge: {}e'.format(self.name, self.mass, self.charge)


if __name__ == '__main__':
    electron = Particle('Electron', 0.511, -1)
    print(electron)
