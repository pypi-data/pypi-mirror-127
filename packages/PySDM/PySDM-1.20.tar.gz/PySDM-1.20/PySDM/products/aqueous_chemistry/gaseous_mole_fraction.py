from PySDM.impl.product import Product
from PySDM.physics.aqueous_chemistry.support import GASEOUS_COMPOUNDS, SPECIFIC_GRAVITY
from PySDM.physics.constants import convert_to, PPB


class GaseousMoleFraction(Product):
    def __init__(self, key):
        super().__init__(
            name=f'gas_{key}_ppb',
            unit='ppb',
            description=f'gaseous {key} mole fraction'
        )
        self.aqueous_chemistry = None
        self.compound = GASEOUS_COMPOUNDS[key]

    def register(self, builder):
        super().register(builder)
        self.aqueous_chemistry = self.particulator.dynamics['AqueousChemistry']

    def get(self):
        tmp = self.formulae.trivia.mixing_ratio_2_mole_fraction(
            self.aqueous_chemistry.environment_mixing_ratios[self.compound],
            specific_gravity=SPECIFIC_GRAVITY[self.compound]
        )
        convert_to(tmp, PPB)
        return tmp
