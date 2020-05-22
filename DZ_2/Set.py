import pytest
# --fixtures

# #3 Структура данных - Множество (Set)
# Тесты находятся в классе. Тест №1 - Множество из списка + параметризация, Тест №2 - Множество из списка (range);
# Тест №3 - Превращение множества в список ; Тест №4 - метод Update ; Тест №5 - len + (in/not in), Тест №6 - Пересечение
# множеств (test6_1 & test6_2).

@pytest.fixture
def first_fixture_for_test_one_set():
    print("\n===> Начало теста #1")

@pytest.fixture
def second_fixture_for_test_two_set():
    print("\n===> Начало теста #2")


@pytest.fixture()
def third_fixture_for_test_three_set():
    print("\n===> Начало теста #3")

@pytest.fixture
def four_fixture_for_test_four_set():
    print("\n===> Начало теста #4")

@pytest.fixture
def five_fixture_for_test_five_set():
    print("\n===> Начало теста #5")

@pytest.fixture
def six_fixture_for_test_six_set():
    print("\n===> Начало теста #6")


test1 = set([1, 2, 3, 4, 3, 2, 1])
@pytest.fixture(params=test1)
def first_fixture_for_test_one_set(request):
    print("\n===> Начало теста #1")
    return request.param

class TestFunction_set:
    def test_from_test_class_one(self, first_fixture_for_test_one_set):
        """
        This is first test in test class
        """
        print(test1)
        assert test1 == {1, 2, 3, 4}
        print("\n===> Завершение теста")

    def test_from_test_class_two(self, second_fixture_for_test_two_set):
        """
        This is second test in test class
        """
        test2 = set(range(5))
        print(test2)
        assert test2 == {0, 1, 2, 3, 4}
        print("\n===> Завершение теста")

    def test_from_test_class_three(self, third_fixture_for_test_three_set):
        """
        This is the third test in test class
        """
        test3 = [1, 2, 3, 1, 2, 3, 4]
        test3 = list(set(test3))
        print(test3)
        assert test3 == [1, 2, 3, 4]
        print("\n===> Завершение теста")

    def test_from_test_class_four(self, four_fixture_for_test_four_set):
        """
        This is the four test in test class
        """
        test4 = {11, 22, 33, 44, 55}
        test4.update('Otus')
        print(test4)
        print("\n===> Завершение теста")

    def test_from_test_class_five(self, five_fixture_for_test_five_set):
        """
        This is the five test in test class
        """
        test5 = {1, 2, 3, 4, 5}
        print(len(test5))
        print(4 in test5, 2 not in test5)
        assert (len(test5)) == 5
        assert (4 in test5) == True
        assert (6 not in test5) == True
        print("\n===> Завершение теста")

    def test_from_test_class_six(self, six_fixture_for_test_six_set):
        """
        This is the six test in test class
        """
        test6_1 = {1, 2, 3, 4, 5}
        test6_2 = {1, 2, 6, 7, 8}
        test6_3 = {11, 12}
        print(test6_1 & test6_2)  # или print(test6_1.intersection(test6_2))
        print(test6_1 & test6_3)  # или print(test6_1.intersection(test6_3))
        assert (test6_1 & test6_2) == {1, 2}
        print("\n===> Завершение теста")