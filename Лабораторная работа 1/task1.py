import doctest


class Student:
    def __init__(self, surname: str, first_name: str, average_score: float):
        """
        Создание и подготовка к работе объекта "Студент"

        :param surname: Фадилия студента
        :param first_name: Имя студента
        :param average_score: Средний балл студента

        Примеры:
        >>> student = Student("Иванов", "Иван", 4.3)
        """
        if not isinstance(surname, str):
            raise TypeError("Фамилия студента должна быть типа str")
        self.surname = surname

        if not isinstance(first_name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.first_name = first_name

        if not isinstance(average_score, (int, float)):
            raise TypeError("Средний балл студента должен быть типа int или float")
        if average_score < 0:
            raise ValueError("Средний балл студента должен быть неотрицательным")
        self.average_score = average_score

    def get_surname(self) -> str:
        """
        Функция, которая возвращает фамилию студента

        :return: Возвращает фамилию студента

        Примеры:
        >>> student = Student("Иванов", "Иван", 4.3)
        >>> student.get_surname()
        'Иванов'
        """
        return self.surname

    def get_first_name(self) -> str:
        """
        Функция, которая возвращает имя студента

        :return: Возвращает имя студента

        Примеры:
        >>> student = Student("Иванов", "Иван", 4.3)
        >>> student.get_first_name()
        'Иван'
        """
        return self.first_name

    def get_average_score(self) -> float:
        """
        Функция, которая возвращает средний балл студента

        :return: Возвращает средний балл студента

        Примеры:
        >>> student = Student("Иванов", "Иван", 4.3)
        >>> student.get_average_score()
        4.3
        """
        return self.average_score


class Employee:
    def __init__(self, surname: str, first_name: str, post: str):
        """
        Создание и подготовка к работе объекта "Сотрудник"

        :param surname: Фадилия сотрудника
        :param first_name: Имя сотрудника
        :param post: Должность сотрудника

        Примеры:
        >>> employee = Employee("Иванов", "Иван", "Директор")
        """
        if not isinstance(surname, str):
            raise TypeError("Фамилия сотрудника должна быть типа str")
        self.surname = surname

        if not isinstance(first_name, str):
            raise TypeError("Имя сотрудника должно быть типа str")
        self.first_name = first_name

        if not isinstance(surname, str):
            raise TypeError("Должность сотрудника должна быть типа str")
        self.post = post

    def get_surname(self) -> str:
        """
        Функция, которая возвращает фамилию сотрудника

        :return: Возвращает фамилию сотрудника

        Примеры:
        >>> employee = Employee("Иванов", "Иван", "Директор")
        >>> employee.get_surname()
        'Иванов'
        """
        return self.surname

    def get_first_name(self) -> str:
        """
        Функция, которая возвращает имя работника

        :return: Возвращает имя работника

        Примеры:
        >>> employee = Employee("Иванов", "Иван", "Директор")
        >>> employee.get_first_name()
        'Иван'
        """
        return self.first_name

    def get_post(self) -> str:
        """
        Функция, которая возвращает средний балл работника

        :return: Возвращает средний балл работника

        Примеры:
        >>> employee = Employee("Иванов", "Иван", "Директор")
        >>> employee.get_post()
        'Директор'
        """
        return self.post


class Phone:
    def __init__(self, model: str, price: float, is_the_phone_on: bool):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param model: Модель телефона
        :param price: Стоимость телефона
        :param is_the_phone_on: Включён ли телефон

        Пример:
        >>> phone = Phone("TECNO Pova 5 Pro 5G 8/256GB (Dark Illusion)", 20929, True) # вовсе не реклама:)
        """
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть типа str")
        self.model = model

        if not isinstance(price, (int, float)):
            raise TypeError("Стоимость телефона должна быть типа int или float")
        if price < 0:
            raise ValueError("Стоимость телефона должна быть неотрицательным")
        self.price = price

        if not isinstance(is_the_phone_on, bool):
            raise TypeError("Состояние телефона (выкл/вкл) должно быть типа bool")
        self.is_the_phone_on = is_the_phone_on

    def get_model(self) -> str:
        """
        Функция, которая возвращает модель телефона

        :return: Модель телефона

        Примеры:
        >>> phone = Phone("TECNO Pova 5 Pro 5G 8/256GB (Dark Illusion)", 20929, True)
        >>> phone.get_model()
        'TECNO Pova 5 Pro 5G 8/256GB (Dark Illusion)'
        """
        return self.model

    def get_price(self) -> float:
        """
        Функция, которая возвращает стоимость телефона

        :return: Стоимость телефона

        Примеры:
        >>> phone = Phone("TECNO Pova 5 Pro 5G 8/256GB (Dark Illusion)", 20929, True)
        >>> phone.get_price()
        20929
        """
        return self.price

    def turn_off_the_phone(self) -> None:
        """
        Процедура, которая выключает телефон

        :return: None

        Примеры:
        >>> phone = Phone("TECNO Pova 5 Pro 5G 8/256GB (Dark Illusion)", 20929, True)
        >>> phone.turn_off_the_phone()
        """
        if self.is_the_phone_on is True:
            self.is_the_phone_on = False


if __name__ == "__main__":
    doctest.testmod()
    pass
