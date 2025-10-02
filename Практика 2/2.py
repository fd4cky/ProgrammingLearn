scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14] # test
student_score = 48

def check_winners(scores: list, student_score: int) -> str:
    scores_sorted = sorted(scores, reverse=True)
    student_index = scores_sorted.index(student_score)

    if student_index + 1 <= 3:
        return "Вы в тройке победителей!"
    return "Вы не попали в тройку победителей."

print(check_winners(scores, student_score))