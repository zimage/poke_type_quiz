import unittest
from type_effectiveness import *

class AtackerTestCase(unittest.TestCase):

    def testGoodCreate(self):
        types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
        for t in types:
            x = Attack(t)
            assert isinstance(x, Attack)

    def testBadCreate(self):
        try:
            x = Attack("FooBar")
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def testReflexive(self):
        x = Attack("Bug")
        y = Attack("Bug")
        assert x==y

class DefenderTestCase(unittest.TestCase):

    def testGoodCreate(self):
        types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
        for t in types:
            x = Defender(t)
            assert isinstance(x, Defender)

    def testBadCreate(self):
        try:
            x = Defender("FooBar")
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def testGoodDoubleCreate(self):
        types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]
        for x in types:
            for y in types:
                if x == y:
                    break
                p = Defender([x,y])
                assert isinstance(p, Defender)

    def testBadDoubleCreateSingleType(self):
        try:
            x = Defender(["Bug"])
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def testBadDoubleCreateTwoSameType(self):
        try:
            x = Defender(["Bug", "Bug"])
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def testBadDoubleCreateUnknownType(self):
        try:
            x = Defender(["Bug", "Foo"])
        except ValueError:
            pass
        else:
            fail("expected a ValueError")

    def testReflexive(self):
        x = Defender(["Bug", "Dark"])
        y = Defender(["Bug", "Dark"])
        assert x==y

    def testSymmetricCreate(self):
        x = Defender(["Bug", "Dark"])
        y = Defender(["Dark", "Bug"])
        assert x==y

if __name__ == "__main__":
    unittest.main()
