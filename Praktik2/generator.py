import random
from Praktik2.RAM import RAM
from Praktik2.ram_specification import corsair, hyperX, corsair_type, hyperX_type


class Generator:
    def _create_manufacture(self) -> str:
        self.manufacture = random.choice(["Corsair", "HyperX"])
        return self.manufacture

    def _create_series(self) -> str:
        if self.manufacture == "Corsair":
            self.series = random.choice(list(corsair.keys()))
        else:
            self.series = random.choice(list(hyperX.keys()))
        return self.series

    def _create_type(self) -> str:
        if self.manufacture == "Corsair":
            self.type = corsair_type[self.series]
            if len(self.type) > 1:
                self.type = self.type[random.randint(0, 1)].split()
            elif len(self.type) == 1:
                self.type.append("".join(self.type))
        else:
            self.type = hyperX_type[self.series]
        return str("".join(self.type))

    def _memory_and_modification(self) -> list:
        if self.manufacture == "Corsair":
            if self.series == "ValueSelect":
                self.memory = 2
                self.frequency = 800.0
                self.mod = ""
                self.prefix = ""
            if self.series == "VengeanceLP":
                self.memory = random.choice([4, 8])
                self.frequency = 1600.0
                self.mod = ""
                self.prefix = ""
            elif self.series == "VengeancePro":
                self.memory = random.choice([4, 8])
                if self.memory == 4:
                    self.frequency = 1600.0
                else:
                    self.frequency = 2400.0
                self.mod = ""
                self.prefix = ""
            elif self.series == "VengeancePRO":
                self.memory = random.choice([8, 16])
                if self.memory == 8:
                    self.frequency = random.choice([2133.0, 2666.0, 3000.0, 3200.0, 3600.0, 4000.0])
                else:
                    self.frequency = random.choice([3000.0, 3200.0, 3600.0])
                self.mod = ""
                self.prefix = ""
            elif self.series == "VengeanceLPX":
                self.memory = random.choice([4, 8, 16, 32])
                if self.memory == 4:
                    self.frequency = random.choice([2133.0, 2400.0])
                elif self.memory == 8:
                    self.frequency = random.choice([1600.0, 2133.0, 2400.0, 2666.0, 3000.0, 3200.0, 3600.0, 4000.0, 4133.0, 4266.0, 4333.0, 4400.0])
                elif self.memory == 16:
                    self.frequency = random.choice([2400.0, 2666.0, 3000.0, 3200.0, 3600.0, 4000.0, 4133.0])
                elif self.memory == 32:
                    self.frequency = random.choice([2400.0, 2666.0, 3200.0])
                self.mod = ""
                self.prefix = ""
            elif self.series == "Dominator":
                self.memory = random.choice([8, 16])
                if self.memory == 8:
                    self.frequency = random.choice([3000.0, 3200.0, 3466.0, 3600.0, 4000.0])
                elif self.memory == 16:
                    self.frequency = random.choice([3000.0, 3200.0, 4000.0])
                self.mod = "Platinum"
                self.prefix = ""
            else:
                self.mod, self.memory, self.frequency = "ERROR", 0, 0.0
        else:
            if self.series == "Fury":
                self.memory = random.choice([4, 8])
                if self.memory == 4:
                    self.frequency = random.choice([1333.0, 1600.0, 1866.0])
                else:
                    self.frequency = random.choice([1600.0, 1866.0])
                self.mod = ""
                self.prefix = ""
            elif self.series == "FURY":
                self.memory = random.choice([4, 8, 16, 32])
                if self.memory == 4:
                    self.frequency = random.choice([2666.0, 3000.0, 3200.0])
                elif self.memory == 8:
                    self.frequency = random.choice([2133.0, 2666.0, 3200.0, 3466.0, 3600.0, 3733.0])
                elif self.memory == 16:
                    self.frequency = random.choice([2400.0, 2666.0, 3000.0, 3200.0, 3466.0, 3600.0, 3733.0])
                elif self.memory == 32:
                    self.frequency = random.choice([2666.0, 3000.0, 3200.0, 3466.0, 3600.0])
                self.mod = ""
                self.prefix = ""
            elif self.series == "Predator":
                self.memory = random.choice([8, 16, 32])
                if self.memory == 8:
                    self.frequency = random.choice([3000.0, 3200.0, 3333.0, 3600.0, 4000.0])
                elif self.memory == 16:
                    self.frequency = random.choice([3000.0, 3200.0, 3333.0, 3600.0])
                elif self.memory == 32:
                    self.frequency = random.choice([3000.0, 3200.0, 3600.0])
                self.mod = ""
                self.prefix = ""
            else:
                self.mod, self.memory, self.frequency = "ERROR", 0, 0.0
        return [self.mod, self.memory, self.frequency, self.prefix]

    def generator(self) -> RAM:
        return RAM(self._create_manufacture(), self._create_series(), self._create_type(),
                   self._memory_and_modification(), "CL16")

    def generate_1000(self) -> list:
        return [self.generator() for i in range(1000)]

    def generate_10000(self) -> list:
        return [self.generator() for i in range(10000)]


if __name__ == "__main__":
    gen = Generator()
    [print(i) for i in gen.generate_10000()]
