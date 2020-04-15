import pytest
# --fixtures

#4 Структура данных - Словари (string)
# Тесты находятся в классе. Тест №1 - Метод Count + параметризация, # Тест №2 - Метод find;
# Тест №3 - Метод replace ; Тест №4 - метод Rjust/Ljust ; Тест №5 - Метод Split

@pytest.fixture
def first_fixture_for_test_one_string():
    print("\n===> Начало теста #1")

@pytest.fixture
def second_fixture_for_test_two_string():
    print("\n===> Начало теста #2")


@pytest.fixture()
def third_fixture_for_test_three_string():
    print("\n===> Начало теста #3")

@pytest.fixture
def four_fixture_for_test_four_string():
    print("\n===> Начало теста #4")

@pytest.fixture
def five_fixture_for_test_five_string():
    print("\n===> Начало теста #5")

@pytest.fixture
def six_fixture_for_test_six_string():
    print("\n===> Начало теста #6")


string_param = [1, 2, 3]
@pytest.fixture(params=string_param)
def first_fixture_for_test_one_string(request):
    print("\n===> Начало теста #1")
    # Как сделать так, чтобы внутри теста 1 была параметризация вывода фикстуры? ("\n===> Начало теста #1,2,3,4,5")
    # для каждого теста свой вывод фикстуры
    return request.param

class TestFunction:
    def test_from_test_class_one(self, first_fixture_for_test_one_string):
        """
        This is first test in test class
        """
        test1 = 'hello world'
        print(test1.count('o', 5))
        if test1.count('o', 5) == 1:
            print('Тест успешно пройден')
        else:
            print('Тест не пройден')
#       yield
#       print("\n===> Завершение теста")

    def test_from_test_class_two(self, second_fixture_for_test_two_string):
        """
        This is second test in test class
        """
        test2 = 'hello world'
        print(test2.find('wor'))
        if test2.find('wor') == 6:
            print('Тест успешно пройден')
        else:
            print('Тест не пройден')
#      yield
#      print("\n===> Завершение теста")

    def test_from_test_class_three(self, third_fixture_for_test_three_string):
        """
        This is the third test in test class
        """
        test3 = 'hello world'
        print(test3.replace('o', '!!!'))
        if (test3.replace('o', '!!!')) == 'hell!!! w!!!rld':
            print('Тест успешно пройден')
        else:
            print('Тест не пройден')
#      yield
#      print("\n===> Завершение теста")

    def test_from_test_class_four(self, four_fixture_for_test_four_string):
        """
        This is the four test in test class
        """
        test4 = '12345'
        test4.rjust(10, '5')
        print(test4.rjust(10, '5'))
        test4.ljust(10, '5')
        print(test4.ljust(10, '5'))
        assert (test4.rjust(10, '5')) == '5555512345'
        assert (test4.ljust(10, '5')) == '1234555555'
        if (test4.rjust(10, '5')) == 5555512345 and (test4.ljust(10, '5')) == '1234555555':
            print('Тест успешно пройден')
        else:
            print('Тест не пройден')
#      yield
#      print("\n===> Завершение теста")

    def test_from_test_class_five(self, five_fixture_for_test_five_string):
        """
        This is the five test in test class
        """
        test5 = 'Крылов Кирилл Андреевич'
        test5.split()
        print(test5.split())
        len(test5.split())
        print(len(test5.split()))
        assert (test5.split()) == ['Крылов', 'Кирилл', 'Андреевич']
        assert (len(test5.split())) == 3
        if (test5.split()) == ['Крылов', 'Кирилл', 'Андреевич'] and (len(test5.split())) == 3:
            print('Тест успешно пройден')
        else:
            print('Тест не пройден')
#      yield
#      print("\n===> Завершение теста")