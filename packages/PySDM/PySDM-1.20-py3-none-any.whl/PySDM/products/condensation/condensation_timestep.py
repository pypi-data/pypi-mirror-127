import numpy as np

from PySDM.impl.product import Product


class _CondensationTimestep(Product):

    def __init__(self, extremum, label, reset_value):
        super().__init__(
            name=f'dt_cond_{label}',
            unit='s',
            description=f'Condensation timestep ({label})'
        )
        self.extremum = extremum
        self.reset_value = reset_value
        self.value = None
        self.condensation = None
        self.range = None

    def register(self, builder):
        super().register(builder)
        self.particulator.observers.append(self)
        self.condensation = self.particulator.dynamics['Condensation']
        self.range = self.condensation.dt_cond_range
        self.value = np.full_like(self.buffer, np.nan)

    def notify(self):
        self.download_to_buffer(self.condensation.counters['n_substeps'])
        self.buffer[:] = self.condensation.particulator.dt / self.buffer
        self.value = self.extremum(self.buffer, self.value)

    def get(self):
        self.buffer[:] = self.value[:]
        self.value[:] = self.reset_value
        return self.buffer


class CondensationTimestepMin(_CondensationTimestep):
    def __init__(self):
        super().__init__(np.minimum, 'min', np.inf)


class CondensationTimestepMax(_CondensationTimestep):
    def __init__(self):
        super().__init__(np.maximum, 'max', -np.inf)
