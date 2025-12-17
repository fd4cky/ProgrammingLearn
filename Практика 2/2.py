scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14]  # test
student_score = 48


def check_winners(scores: list, student_score: int) -> None:
    """
    Проверяет, входит ли студент в тройку лучших по списку оценок.

    Аргументы:
        scores (list): Список всех результатов студентов.
        student_score (int): Результат конкретного студента.

    Возвращает:
        None: Выводит сообщение о попадании или непопадании в тройку лидеров.
    """
    scores_sorted = sorted(scores, reverse=True)
    student_index = scores_sorted.index(student_score)

    if student_index + 1 <= 3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


check_winners(scores, student_score)