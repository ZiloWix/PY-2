class Figure:
    def __init__(self, x: int, y: int):
        """
        Базовый класс шахматная фигура - Figure

        :param x: координата х на доске [0, 7]
        :param y: координата y на доске [0, 7]
        _x, _y protected, так как незачем пользователю иметь к ним доступ и производные классы должны их унаследовать
        """
        self._x = x
        self._y = y

    @staticmethod
    def is_selected(self) -> bool:
        """
        Метод, который проверяет выделена ли фигура

        :return: выделена или нет
        """
        ...

    def make_move(self, new_x: int, new_y: int) -> None:
        """
        Метод, результатом которого является смена координат фигууры на доске

        :param new_x: новая координата фигуры по х
        :param new_y: новая координата фигуры по у
        """
        self._x = new_x
        self._y = new_y

    def possible_moves(self) -> (int, int):
        """
        Метод, который возвращает список пар с координатами возможных ходов
        Что-то вроде виртуальной функции, которая будет переопределена в производных классах

        :return: возвращает список пар возможных ходов(х, у)
        """
        ...

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, new_x: int):
        if not isinstance(new_x, int):
            raise TypeError("Координата фигуры должна быть типа int")
        if new_x < 0 or new_x > 8:
            raise ValueError("Координата фигуры должна быть [0; 7]")
        self._x = new_x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, new_y: int):
        if not isinstance(new_y, int):
            raise TypeError("Координата фигуры должна быть типа int")
        if new_y < 0 or new_y > 8:
            raise ValueError("Координата фигуры должна быть [0; 7]")
        self._y = new_y

    def __str__(self) -> str:
        return f"{self.__class__.__name__} с координатами ({self._x}, {self._y})"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self._x!r}, y={self._y!r})"


class Rook(Figure):
    def __init__(self, x: int, y: int):
        """
        Производный клаас Ладья от Фигуры Rook

        Наследует от базового класса конструктор и следующие методы
        __str__,
        __repr__,
        is_selected,
        make_move

        Были переопределены следующие методы:
        possible_moves, так как у ладьи свои ходы

        """
        super().__init__(x, y)

    def possible_moves(self) -> (int, int):
        """
        Метод переопределён, так как у каждой шахматной фигуры свои правила для хода
        """
        possible_moves = []

        for i in range(0, 8):
            if i != self._x:
                possible_moves.append((i, self._y))
            if i != self._y:
                possible_moves.append((self._x, i))

        return possible_moves


if __name__ == "__main__":
    rook = Rook(0, 0)
    print(rook.possible_moves())
    print(rook)
    print(repr(rook))
    pass
