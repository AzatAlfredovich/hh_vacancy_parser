from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class VacancySaver(ABC):
    """
    Абстрактный класс для работы с рядом вакансий: добавление, получение, удаление
    """

    @abstractmethod
    def add(self, vacancies: list[Vacancy]) -> None:
        """
        Добавление вакансии
        """
        pass

    @abstractmethod
    def get(self, criteria: dict) -> list[Vacancy]:
        """
        Получение вакансии по заданным критериям
        """
        pass

    @abstractmethod
    def delete(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии
        """
        pass
