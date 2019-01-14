import unittest
from tests import worker
# from .publisher import Publisher

def main():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(worker))
    # suite.addTests(loader.loadTestsFromModule(publisher))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


