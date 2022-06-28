from AbstractStructure import AbstractStructure
from Praktik3.generator import Generator
from Praktik3.RAM import RAM


class StandardList2(AbstractStructure):
    __list: list = []
    size: int = 0

    def add(self, value: RAM, index: [str, None] = None) -> bool:
        if index is not None and self.size <= index < -self.size:
            return False
        if index is None:
            self.__list.append(value)
        else:
            self.__list.insert(index, value)
        self.size += 1
        return True

    def insert(self, value: RAM, index: int) -> bool:
        if (index is not None and self.size <= index < -self.size) or index is None:
            return False
        self.__list[index] = value
        return True

    def find(self, value: RAM) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        return None

    def get(self, index: int) -> [RAM, None]:
        if -self.size < index <= self.size:
            return self.__list[index]
        return None

    def remove(self, value: RAM) -> bool:
        if value in self.__list:
            self.__list.remove(value)
            self.size -= 1
            return True
        return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self) -> int:
        return self.size


if __name__ == "__main__":
    r = Generator()
    ram1 = r.generator()
    ram2 = r.generator()
    ram3 = r.generator()
    ram4 = r.generator()
    ram5 = r.generator()
    ram6 = r.generator()
    print([ram1, ram2, ram3, ram4, ram5, ram6])
    print("-" * 300)
    s_list = StandardList2()
    print(f"add1: {s_list.add(ram1)}")
    print(f"add2: {s_list.add(ram2)}")
    print(f"add3: {s_list.add(ram3)}")
    print(f"add4: {s_list.add(ram4)}")
    print(f"add5: {s_list.add(ram5)}")
    print("-" * 300)
    print(f"insert: {s_list.insert(ram6, 1)}")
    print(f"get_all1: {s_list.get_all()}")
    print(f"len1: {len(s_list)}")
    print("-" * 300)
    print(f"find ram1: {s_list.find(ram1)}")
    print(f"find ram2: {s_list.find(ram2)}")
    print("-" * 300)
    print(f"get1: {s_list.get(1)}")
    print("-" * 300)
    print(f"remove ram3: {s_list.remove(ram3)}")
    print(f"remove ram3: {s_list.remove(ram3)}")
    print(f"get_all2: {s_list.get_all()}")
    print(f"len2: {len(s_list)}")
