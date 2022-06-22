class RAM:
    manufacture: str
    model: str
    memorysize: str
    memorytype: str
    frequency: str
    timing: str

    def __init__(self, manufacture: str, model: str, memorysize: str, memorytype: str, frequency: str, timing: str):
        self.manufacture = manufacture
        self.model = model
        self.memorysize = memorysize
        self.memorytype = memorytype
        self.frequency = frequency
        self.timing = timing
        self.check()

    def check(self):
        Corsair = {"ValueSelect": "DDR2",
                  ("Vengeance", "VengeancePro", "XMS"): "DDR3",
                  ("VengeanceLPX", "VengeanceRGB", "DominatorPlatinum"): "DDR4"}
        HyperX = {"Fury": "DDR3",
                  ("FURY", "FURYRGB"): "DDR4"}
        year = None
        model = "".join(list(self.model)).split()
        if self.manufacture == "Nvidia":
            for i in Corsair.keys():
                if model[1] in i:
                    year = Corsair.get(i)
                    self.info(year)
            return year
        elif self.manufacture == "Radeon":
            for i in HyperX.keys():
                if model[1] in i:
                    year = HyperX.get(i)
                    self.info(year)
            return year
        else:
            print(f"""{"-"*70}
Подобная информация о оперативной памяти {self.model} от производителя {self.manufacture},
с типом памяти {self.memorytype}
выпущена в {year} году с такими характеристиками: 
объёмом памяти в {self.memorysize},
и латентностью в {self.timing} 
Отсутствует.
{"-"*70}""")

    def info(self, year):
        print(f"""{"-"*70}
Оперативная память {self.model} от производителя {self.manufacture},
с типом памяти {self.memorytype}
выпущена в {year} году с такими характеристиками: 
объёмом памяти в {self.memorysize},
и латентностью в {self.timing}.
{"-"*70}""")


if __name__ == "__main__":
    ram1 = RAM("Corsair", "ValueSelect", "2GB", "DDR2", "800 MHz", "2.5 Trcd; 6 Trp; 15 Tras")
    ram2 = RAM("Corsair", "VengeanceLPX", "8GB", "DDR4", "2666 MHz", "0.75 Trcd; 18 Trp; 13.5 Tras")
    ram3 = RAM("HyperX", "Fury", "4GB", "DDR3", "1600 MHz", "1.25 Trcd; 11 Trp; 13.75 Tras")
    ram4 = RAM("HyperX", "FURYRGB", "8GB", "DDR4", "2666 MHz", "0.75 Trcd; 18 Trp; 13.5 Tras")
