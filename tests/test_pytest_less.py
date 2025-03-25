# test_pytest_less.py - это имя модуля, обратите внимание, что начинается с test_

from testfile import add  # здесь мы импортируем функцию add в текущий модуль

def test_add():
    assert add(2, 3) == 5
    assert add(1, -1) == 0
    assert add(-1, -1) == -2