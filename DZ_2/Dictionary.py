import pytest
# --fixtures

# #1 Структура данных - Словари (dict)
# Тесты находятся в классе. Тест №1 - Создание словаря, Тест №2 - Добавление ключа в словарь;
# Тест №3 - Удаление ключа ; Тест №4 - Удаление словаря ; Тест №5 - Получение ключа, которого нет в словаре
# множеств (test6_1 & test6_2).

@pytest.fixture
def first_fixture_for_test_one_dict():
    print("\n===> Начало теста #1")

@pytest.fixture
def second_fixture_for_test_two_dict():
    print("\n===> Начало теста #2")


@pytest.fixture()
def third_fixture_for_test_three_dict():
    print("\n===> Начало теста #3")

@pytest.fixture
def four_fixture_for_test_four_dict():
    print("\n===> Начало теста #4")

@pytest.fixture
def five_fixture_for_test_five_dict():
    print("\n===> Начало теста #5")


dict_param = [1, 2, 3]
@pytest.fixture(params=dict_param)
def first_fixture_for_test_one_dict(request):
    print("\n===> Начало теста #1")
    return request.param


class TestFunction:
    def test_from_test_class_one(self, first_fixture_for_test_one_dict):
        """
        This is first test in test class
        """
        test1 = dict(Moskva=495, Piter=812, Penza=8412)
        assert test1 == {'Moskva': 495, 'Piter': 812, 'Penza': 8412}
        print("\n===> Завершение теста")
# В примере какому-то значению внутри словаря присваивается ключ.
# Как написать тест, чтобы какому-то значению внутри словаря присваивался рандомный ключ (495, 812, 8412)?
# Хочу сделать проверку правильного присванения ключей городам с вероятностью 33%
#       yield
#       print("\n===> Завершение теста")

    def test_from_test_class_two(self, second_fixture_for_test_two_dict):
        """
        This is second test in test class
        """
        test2 = {
            #key:value,
            'banan': 'yellow',
            'watermelon': 'red',
            'cucumber': 'green'
                }
        test2['eggplant'] = 'purple'
        print(test2)
        assert test2 == {'banan': 'yellow', 'watermelon': 'red', 'cucumber': 'green', 'eggplant': 'purple'}
        print("\n===> Завершение теста")

    def test_from_test_class_three(self, third_fixture_for_test_three_dict):
        """
        This is the third test in test class
        """
        test3 = {
            #key:value,
            'banan': 'yellow',
            'watermelon': 'red',
            'cucumber': 'green'
                }
        print(test3)
        del test3['cucumber']
        print(test3)
        assert test3 == {'banan': 'yellow', 'watermelon': 'red'}
        print("\n===> Завершение теста")

    def test_from_test_class_four(self, four_fixture_for_test_four_dict):
        """
        This is the four test in test class
        """
        test4 = {
            # key:value,
            'banan': 'yellow',
            'watermelon': 'red',
            'cucumber': 'green'
                }
        print(test4)
        test4.clear()
        print(test4)
        assert test4 == {}
        print("\n===> Завершение теста")

    def test_from_test_class_five(self, five_fixture_for_test_five_dict):
        """
        This is the five test in test class
        """
        test5 = {
            # key:value,
            'banan': 'yellow',
            'watermelon': 'red',
            'cucumber': 'green'
                }
        print(test5.get('eggplant'))
        print(test5)
        assert (test5.get('eggplant')) == None
        print("\n===> Завершение теста")