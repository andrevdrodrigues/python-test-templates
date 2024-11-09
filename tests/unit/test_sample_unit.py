import unittest

class MainClass:
    def __init__(self, name):
        self.name = name

    def showCompleteName(self):
        return "Selected name is: {}".format(self.name)

def inputName():
    name = MainClass("Andre Rodrigues")
    return name.showCompleteName()

from unittest.mock import patch

class TestMainClass(unittest.TestCase):

    def test_input_name(self):
        with patch.object(MainClass, 'showCompleteName', return_value="Mocked Object Succesfully"):
            assert inputName() == "Mocked Object Succesfully"            

if __name__ == '__main__':
    unittest.main()
