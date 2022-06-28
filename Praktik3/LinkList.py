from AbstractStructure import AbstractStructure
from Praktik3.generator import Generator
from Praktik3.RAM import RAM
from Node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def add(self, value: RAM, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index > self.size):
            return False
        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
            self.size += 1
        elif index is None:
            current = self.__tail
            node = Node(value)
            current.next = node
            self.__tail = node

            # current = self.__head
            # while current.next:
            #     current = current.next
            # current.next = Node(value)
            self.size += 1
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
            self.size += 1
        return True

    def insert(self, value: RAM, index: int) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        return True

    def find(self, value: RAM) -> [int, None]:
        i = 0
        current = self.__head
        try:
            while current.data != value:
                current = current.next
                i += 1
            return i
        except AttributeError:
            return None

    def get(self, index: int) -> object:
        if self.size <= index or index < 0:
            return None
        else:
            i = 0
            current = self.__head
            while current.next and i < index:
                current = current.next
                i += 1
            return current.data

    def remove(self, value: RAM) -> bool:
        current = self.__head
        if current is None:
            return False
        while current:
            try:
                if current.next.data == value:
                    current.next = current.next.next
                    break
            except AttributeError:
                pass
            if current.data == value:
                self.__head = current.next
                break
            current = current.next
        self.size -= 1
        return True

    def get_all(self) -> list:
        output = []
        current = self.__head
        while current is not None:
            output.append(current.data)
            current = current.next
        return output


if __name__ == "__main__":
    r = Generator()
    ram1 = r.generator()
    ram2 = r.generator()
    ram3 = r.generator()
    ram4 = r.generator()
    ram5 = r.generator()
    ram6 = r.generator()
    s_list = LinkList()
    print(f"""all RAMs: {[ram1, ram2, ram3, ram4, ram5, ram6]}
{"-" * 300}
add ram1: {s_list.add(ram1)}
add ram2: {s_list.add(ram2)}
add ram3: {s_list.add(ram3)}
add ram4: {s_list.add(ram4)}
add ram5: {s_list.add(ram5, 1)}
find: {s_list.find(ram2)}
{"-" * 300}
get_all:  {s_list.get_all()}
size: {s_list.size}
{"-" * 300}
remove ram5: {s_list.remove(ram5)}
find: {s_list.find(ram5)}
get_all:  {s_list.get_all()}
size: {s_list.size}
{"-" * 300}
get ram1: {s_list.get(0)}
get ram4: {s_list.get(3)}
get ram5: {s_list.get(4)}
{"-" * 300}
insert ram6: {s_list.insert(ram6, 1)}
get_all:  {s_list.get_all()}
size: {s_list.size}
{"-" * 300}""")
