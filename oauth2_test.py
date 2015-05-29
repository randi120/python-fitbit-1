
import unittest
from fitbit_tests.test_auth import Auth2Test


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(Auth2Test)
	unittest.TextTestRunner(verbosity=2).run(suite)
