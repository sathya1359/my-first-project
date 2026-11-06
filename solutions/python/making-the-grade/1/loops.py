"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return list(map(round, student_scores))

def count_failed_students(student_scores):
    failed = 0

    for score in student_scores:
        if score <= 40:
            failed += 1

    return failed
def above_threshold(student_scores, threshold):
    result = []

    for score in student_scores:
        if score >= threshold:
            result.append(score)

    return result

def letter_grades(highest):
    step = (highest - 40) // 4

    return [
        41,
        41 + step,
        41 + 2 * step,
        41 + 3 * step
    ]

def student_ranking(student_scores, student_names):
    result = []

    for rank, name in enumerate(student_names, start=1):
        result.append(f"{rank}. {name}: {student_scores[rank - 1]}")

    return result

def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student

    return []