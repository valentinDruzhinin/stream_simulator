import numpy


class NormalDistributionGenerator:

    def __init__(self, mean=0, width=1):
        self.samples = []
        self.mean = mean
        self.width = width

    def get_sample(self):
        if not self.samples:
            self.samples = list(numpy.random.normal(self.mean, self.width, 1000))
        return self.samples.pop()
