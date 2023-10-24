import random as rnd
from typing import Tuple, List


def open_file(filename: str) -> list:
    """Получаем название файла со словами и преобразуем данные в список"""

    word_list = []

    with open(f"{filename}.txt", encoding="utf-8") as file:
        for word in file:
            word_list.append(word.strip())

    return word_list


def get_list(words) -> list:
    """Вернет список слов"""

    return words


def get_user_name(user_name: str) -> str:
    """Вернет имя пользователя """

    return user_name


def choose_word(word_list: list) -> tuple[str, str]:
    """Выбираем случайное слово из списка и перемешиваем буквы"""

    word = rnd.choice(word_list)
    lst_word = list(word)
    rnd.shuffle(lst_word)
    shuffle_word = "".join(lst_word)

    return "".join(word), shuffle_word


def play() -> None:
    """Запускает игру, пока длина списка использованных слов не равна
    списку загаданных слов, перемешивает буквы в слове и выводит только те слова, которых ранее не было.
    Проверяет правильность ответа. После чего сохраняет данные игры"""

    word_list = get_list(open_file("words"))
    used_words = []
    answers = []

    user_name = get_user_name(role("Введите ваше имя"))

    input("Нажмите Enter, чтобы продолжить....")

    while len(used_words) != len(word_list):
        word, shuffle_word = choose_word(word_list)
        if word not in used_words:
            check_answer(answers, role(f"Угадайте слово: {shuffle_word}"), word)
            used_words.append(word)

    save_data(user_name, total_score(answers), "history")
    print(leaderstats("history"))


def role(text: str = "", members: int = 2) -> None or str:
    """Возвращает ответ пользователя, если подразумевается ответ пользователя"""

    progr = "Программа:"
    user = "Пользователь:"

    if members == 1:
        print(f"{progr} {text} ")
    elif members == 2:
        print(f"{progr} {text} ")
        user = input(f"{user} ")

        return user


def total_score(answers: list) -> int:
    """Считает сумму все верных ответов с заданным извне кол-вом баллов"""

    score = sum([10 for answer in answers if answer])

    return score


def check_answer(answers: list, answer: str, word: str) -> list:
    """Проверяет правильный ответ и вносит данные проверки в указанный список"""

    if answer.lower() == word.lower():
        answers.append(True)
        role("Верно! Вы получаете 10 очков.", 1)
    else:
        answers.append(False)
        role(f"Неверно! Верный ответ – {word}..", 1)

    return answers


def save_data(user_name: str, score: int, filename: str) -> None:
    """Считывает данные из файла с общими результатами.
    Добавляет и записывает данные текущего пользователя и результатов игры."""

    records = read_records(filename)
    records.append((user_name, score))
    write_records(filename, records)


def leaderstats(filename: str) -> str:
    """Возвращает строку с лучшими результатами"""

    stats = read_records(filename)
    result = [tup[1] for tup in stats]

    return f"Всего игр сыграно: {len(stats)}\nМаксимальный рекорд: {max(result)}"


def read_records(filename: str) -> List[Tuple[str, int]]:
    """Читает файл и возвращает данные с результатами игроков в виде кортежа"""

    records = []

    with open(f"{filename}.txt", "r", encoding="utf-8") as file:
        for line in file:
            name, score = line.strip().split()
            records.append((name, int(score)))

    return records


def write_records(filename: str, records: List[Tuple[str, int]]) -> None:
    """Открывает файл на дозапись и вносит новые данные"""

    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
        for name, score in records:
            file.write(f"{name} {score}\n")


# запускаем игру
play()
