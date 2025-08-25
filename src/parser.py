from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    def __init__(self, file_worker=None):
        """
        - file_worker отвечает за сохранение и загрузку данных в файлы JSON и CSV
        """
        self.file_worker = file_worker

    @abstractmethod
    def connect_to_api(self):
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """Метод для получения вакансий по ключевому слову"""
        pass
