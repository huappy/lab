import unittest
from classes import *

class Test_television(unittest.TestCase):
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        self.setup_method()
        assert self.tv1.__str__() == "TV status: Is on = False, channel = 0, volume = 0"
        self.teardown_method()

    def test_power(self):
        self.setup_method()
        self.tv1.power()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 0"
        self.tv1.power()
        assert self.tv1.__str__() == "TV status: Is on = False, channel = 0, volume = 0"


    def test_channel_up(self):
        self.setup_method()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "TV status: Is on = False, channel = 0, volume = 0"

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 1, volume = 0"

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 0"
        self.teardown_method()

    def test_channel_down(self):
        self.setup_method()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "TV status: Is on = False, channel = 0, volume = 0"

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 3, volume = 0"

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 0"
        self.teardown_method()


    def test_volume_up(self):
        self.setup_method()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "TV status: Is on = False, channel = 0, volume = 0"

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 1"

        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 2"
        self.teardown_method()

    def test_volume_down(self):
        self.setup_method()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "TV status: Is on = False, channel = 0, volume = 0"

        self.tv1.power()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 0"

        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "TV status: Is on = True, channel = 0, volume = 1"
        self.teardown_method()


if __name__ == '__main__':
    unittest.main()
