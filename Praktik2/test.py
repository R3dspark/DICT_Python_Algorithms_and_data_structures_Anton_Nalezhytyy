from RAM import RAM
from generator import Generator


def test_gpu():
    r = RAM("Corsair", "Vengeance", "DDR4", ["LPX", 16, 3000.0, ""], "CL16")
    assert r.manufacture == "Corsair"
    assert r.model == "Vengeance"
    assert r.type == "DDR4"
    assert r.mod == "LPX"
    assert r.memory == 16
    assert r.frequency == 3000.0
    assert r.prefix == ""
    assert r.timing == "CL16"


def test_gpu_get_info():
    r = RAM("Corsair", "Vengeance", "DDR4", ["LPX", 16, 3000.0, ""], "CL16")
    assert isinstance(r.get_info(), str)


def test_gen_single_type():
    r = Generator()
    i = r.generator()
    assert isinstance(i, RAM)
    assert isinstance(i.manufacture, str)
    assert isinstance(i.model, str)
    assert isinstance(i.type, str)
    assert isinstance(i.mod, str)
    assert isinstance(i.memory, int)
    assert isinstance(i.frequency, float)
    assert isinstance(i.timing, str)
    assert isinstance(i.prefix, str)


def test_gen_1000_type():
    r = Generator()
    i = r.generate_1000()
    assert isinstance(i, list)
    assert isinstance(i[0], RAM)
    assert len(i) == 1000


def test_gen_10000_type():
    r = Generator()
    i = r.generate_10000()
    assert isinstance(i, list)
    assert isinstance(i[0], RAM)
    assert len(i) == 10000
