from Praktik3.ram_specification import corsair, hyperX


class RAM:
    manufacture: str
    model: str
    memory: str
    type: str
    frequency: str
    timing: str

    def __init__(self, manufacture: str, model: str, type: str,
                 mod_memory_frequency: list, timing: str):
        self.manufacture = manufacture
        self.model = model
        self.mod, self.memory, self.frequency, self.prefix = mod_memory_frequency
        self.type = type
        self.timing = timing

    def __repr__(self) -> str:
        return f"{self.manufacture} {self.prefix} {self.model}{self.mod} {self.memory}GB {self.type} " \
               f"{self.frequency} MHz {self.timing}"

    def __eq__(self, other):
        return self.manufacture == other.manufacture and \
               self.model == other.model and \
               self.mod == other.mod and \
               self.memory == other.memory and \
               self.frequency == other.frequency and \
               self.prefix == other.prefix and \
               self.type == other.type and \
               self.timing == other.timing

    def __print_unknown(self) -> str:
        return f"""Видеокарта: {self.model}{self.mod}
Производитель: {self.manufacture}
Графический чип: {self.type}
Объем памяти: {self.memory}
Поддерживаемое разрешение экрана {self.timing}
Отсутствует"""

    def __print_known(self, year) -> str:
        return f"""Видеокарта: {self.prefix} {self.model} {self.mod}
Производитель: {self.manufacture}
Графический чип: {self.type}
Объем памяти: {self.memory}GB
Частотой ядра: {self.frequency} MHz
Год выпуска: {year}
Поддерживаемое разрешение экрана {self.timing}
{'-' * 40}"""

    def get_info(self) -> str:
        year: int = 0
        if self.manufacture.strip().lower() == "Corsair":
            for i in corsair:
                if self.model in i:
                    year = corsair[i]
            self.prefix = ""
        elif self.manufacture.strip().lower() == "HyperX":
            for i in hyperX:
                if self.model in i:
                    year = hyperX[i]
            self.prefix = ""
        else:
            return self.__print_unknown()
        return self.__print_known(year)
