# test_pytest_less.py - это имя модуля, обратите внимание, что начинается с test_
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pytest_less import add  # здесь мы импортируем функцию add в текущий модуль

def test_add():
    assert add(2, 3) == 5
    assert add(1, -1) == 0
    assert add(-1, -1) == -2