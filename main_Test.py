from unittest import mock
from unittest import TestCase

import numpy

from main import ConnectFour

FIELD_RENDER = str(numpy.zeros((6, 7)))
class connectFour_Test(TestCase):
    @mock.patch('ConnectFour.getMove.input', )
    def setUp(self) -> None:
        self.connectFour = ConnectFour()

    def test_field_exists(self):
        self.assertIsNotNone(self.connectFour._field)

    def test_getMove_inbounds(self, mocked_input):
        mocked_input.side_effect = 4





if __name__ == '__main__':
    unittest.main()
