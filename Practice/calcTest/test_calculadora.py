from calculadora import suma
import pytest


# def main():
#     test_suma()


# def test_suma():
#     # if suma(1, 1) != 2:
#     #     print("Suma is not adding")
#     try:
#         assert suma(2, 2) == 4
#         assert suma(2, 3) == 5
#         assert suma(4, 4) == 8
#     except AssertionError:
#         print("Suma is not adding numbers")


# if __name__ == "__main__":
#     main()

def test_suma():
    assert suma(2, 2) == 4
    assert suma(2, 3) == 5
    assert suma(3, 4) == 7

def test_zero():
    assert suma(0, 3) == 3


def test_negative():
    assert suma(-2, -2) == -4

def test_str():
    with pytest.raises(TypeError):
        suma("cat")
    