class Vacancy:
    """
    Класс для работы с вакансиями
    """

    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary, description: str):
        self.title = title
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    @staticmethod
    def _validate_salary(salary):
        """
        Принудительное указание зарплаты, если она не объявлена явно
        """
        if (
            salary is None
            or salary == ""
            or (isinstance(salary, str) and salary == "зарплата не указана")
        ):
            return 0
        try:
            return int(salary)
        except (ValueError, TypeError):
            return 0

    def __lt__(self, other):
        """
        Сравнение вакансий по зарплате (меньше)
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __eq__(self, other):
        """
        Проверка равенства вакансий по зарплате и названию
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary and self.title == other.title

    def __repr__(self) -> str:
        """
        Строковое представление вакансии для отладки
        """
        return (
            f"Vacancy(title={self.title!r}, url={self.url!r}, "
            f"salary={self.salary}, description={self.description!r})"
        )

    def __str__(self):
        """
        Представление вакансии в строковом виде
        """
        return f"Название: {self.title}\nСсылка: {self.url}\nЗарплата: {self.salary}\nОписание: {self.description}"

    def to_dict(self):
        """
        Преобразует объект класса Vacancy в словарь
        """

        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }
