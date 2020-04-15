import pytest
# --fixtures

#2 Структура данных - Список (List)
# Метод List Append + параметризация

cars = ['BMW', 'Mercedes benz', 'Audi', 'Lexus']
@pytest.fixture(params=cars)
def first_fixture_for_test_one_list(request):
    print("\n===> Начало теста")
    return request.param


def test_one(first_fixture_for_test_one_list):
    """
    This is first test in List
    """
    cars.append('Range rover')
    assert cars != ['BMW', 'Mercedes benz', 'Audi', 'Lexus']
    if cars == ['BMW', 'Mercedes benz', 'Audi', 'Lexus', 'Range rover']:
            print('Тест успешно пройден')
    else:
        print('Тест не пройден')
#       yield
#       print("\n===> Завершение теста")

# Не понимаю как сделать вывод "\n===> Завершение теста" в конце выполнения теста, если раскоментить две верхние строки,
# то появляется Tests ignored

# Метод List Count
@pytest.fixture()
def second_fixture_for_test_two_list():
    print("\n===> Начало теста")

def test_two(second_fixture_for_test_two_list):
    """
    This is second test in List
    """
    fruits = ['orange', 'apple', 'pear', 'apple', 'banana']
    fruits.count('apple')
    print(fruits.count('apple'))
    assert fruits.count('apple') == 2
    if fruits.count('apple') == 2:
        print('Тест успешно пройден')
    else:
        print('Тест не пройден')
#       yield
#       print("\n===> Завершение теста")


# Метод List Copy
@pytest.fixture()
def third_fixture_for_test_three_list():
    print("\n===> Начало теста")

def test_three(third_fixture_for_test_three_list):
    """
    This is the third test in List
    """
    a = [1, 2, 3, 4, 5]
    b = a.copy()
    print(b)
    assert a == b
    if b == a:
        print('Тест успешно пройден')
    else:
        print('Тест не пройден')
#       yield
#       print("\n===> Завершение теста")


# Метод List Insert
@pytest.fixture()
def four_fixture_for_test_four_list():
    print("\n===> Начало теста")

def test_four(four_fixture_for_test_four_list):
    """
    This is the four test in List
    """
    z = [7, 3, 3, 4, 5]
    z.insert(4, [1, 2])
    print(z)
    assert (z.index(5)) == 5
    if (z.index(5)) == 5:
        print('Тест успешно пройден')
    else:
        print('Тест не пройден')
#       yield
#       print("\n===> Завершение теста")

# Метод List Remove
@pytest.fixture()
def five_fixture_for_test_five_list():
    print("\n===> Начало теста")


def test_five(five_fixture_for_test_five_list):
    """
    This is the five test in List
    """
    rx = [7, 3, 3, 4, 5]
    rx.remove(3)
    print(rx)
    assert rx == [7, 3, 4, 5]
    if rx == [7, 4, 5]:
        print('Тест успешно пройден')
    else:
        print('Тест не пройден')
#       yield
#       print("\n===> Завершение теста")