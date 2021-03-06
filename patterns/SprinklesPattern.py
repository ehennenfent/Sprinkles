from sample_pattern import SamplePattern
import random

class SprinklesPattern(SamplePattern):

    def setup(self, size=(6,6,12)):
        super().setup()
        self.pixels = []


        self.i = 0
        self.change = 1

    def tick(self):
        results = []

        for i in range(self.max_elements):
            if i == self.i:
                results.append(next(self.color))

            else:
                results.append((0,0,0))
        self.i = (self.i + self.change) % self.max_elements 

        return results

    def teardown(self):
        pass

class SprinklesReversePattern(SprinklesPattern):

    def setup(self, size=(6,6,12)):
        super().setup()

        self.change = -1

    def tick(self):
        return super().tick()

    def teardown(self):
        super().teardown()
