import unittest
from tests import worker
from tests import publisher
import time

def main():
    # incializa o suite de testes
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # adiciona o teste ao suite
    suite.addTests(loader.loadTestsFromModule(worker))
    # limpa a pasta folder_test, roda o script que simula a criação dos 
    # e depois limpa a pasta novamente
    publisher.remove_files()
    time.sleep(1)
    publisher.main()
    publisher.remove_files()
    # inicializar o runner, passa o teste e roda
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


