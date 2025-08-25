import logging

from src.hh import HH
from src.json_saver import JSONSaver
from src.user_interaction import user_interaction


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler()],  # Логи выводятся в консоль
    )

    # Инициализация объектов API и сохранения
    hh_api = HH()
    saver = JSONSaver("data/vacancies.json")

    print("Подключение к HH API...")
    connected = hh_api.connect_to_api()
    if connected:
        print("Подключение к HH API успешно")
    else:
        print("Не удалось подключиться к HH API. Проверьте соединение!")

    # Запускаем взаимодействие с пользователем
    user_interaction(hh_api, saver)


if __name__ == "__main__":
    main()
