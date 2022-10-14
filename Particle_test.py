import unittest
from assignment_2 import *


class TestParticle(unittest.TestCase):
    def test_proton(self):
        proton = Proton()
        print(proton)

    def test_alpha(self):
        alpha = Alpha(0.11)
        print(alpha)

    def test_create_new(self):
        electron = Particle('Electron', 0.511, -1, 0.5)
        print(electron)

    def test_change(self):
        proton = Proton(0.6)
        print(f'The proton Gamma factor is: {proton.gamma} \n'
              f'The proton Energy is: {proton.energy} MeV \n'
              f'The proton Momentum is: {proton.momentum} kg*m/s \n')

        proton.beta = 0.7
        print(f'The proton Gamma factor is: {proton.gamma} \n'
              f'The proton Energy is: {proton.energy} MeV \n'
              f'The proton Momentum is: {proton.momentum} kg*m/s \n')

        proton.gamma = 1.5
        print(f'The proton Gamma factor is: {proton.gamma} \n'
              f'The proton Energy is: {proton.energy} MeV \n'
              f'The proton Momentum is: {proton.momentum} kg*m/s \n')


if __name__ == '__main__':
    unittest.main()
