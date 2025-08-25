import requests
from requests import RequestException

from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker=None):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        super().__init__(file_worker)

    def connect_to_api(self):
        """
        Проверка подключения к API HeadHunter
        """
        try:
            response = requests.get(
                self.url, headers=self.headers, params={"text": "", "per_page": 1}
            )
            return response.status_code == 200
        except RequestException:
            return False

    def load_vacancies(self, keyword: str) -> list:
        """
        Загрузка вакансий по ключевому слову
        """
        self.params["text"] = keyword
        self.params["page"] = 0
        self.vacancies = []
        max_pages = 20

        while self.params.get("page") < max_pages:
            try:
                response = requests.get(
                    self.url, headers=self.headers, params=self.params
                )
                if response.status_code != 200:
                    raise RuntimeError(
                        f"Ошибка запроса: {response.status_code} - {response.reason}"
                    )

                data = response.json()
                vacancies_page = data.get("items", [])
                if not vacancies_page:
                    break

                self.vacancies.extend(vacancies_page)
                self.params["page"] += 1
            except requests.RequestException as e:
                raise RuntimeError(f"Ошибка подключения к API: {e}")

        return self.vacancies
