from PySDM.impl.product import Product


class CoalescenceTimestepMin(Product):

    def __init__(self):
        super().__init__(
            name='dt_coal_min',
            unit='s',
            description='Coalescence timestep (minimal)'
        )
        self.coalescence = None
        self.range = None

    def register(self, builder):
        super().register(builder)
        self.coalescence = self.particulator.dynamics['Coalescence']
        self.range = self.coalescence.dt_coal_range

    def get(self):
        self.download_to_buffer(self.coalescence.stats_dt_min)
        self.coalescence.stats_dt_min[:] = self.coalescence.particulator.dt
        return self.buffer
