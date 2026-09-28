
import json
def get_student_stats():
    with open("week_5/lab_9/value.json", "r") as file:
        data = json.load(file)
    grades = [student["grade"] for student in data]
    names = [student["name"] for student in data]
    avg_grades = sum(int(grade) for grade in grades) / len(grades)
    max_grade = max(int(grade) for grade in grades)
    min_grade = min(int(grade) for grade in grades)
    max_grade_student = names[[int(grade) for grade in grades].index(max_grade)]
    min_grade_student = names[[int(grade) for grade in grades].index(min_grade)]
    passing_students = [name for name, grade in zip(names, grades) if int(grade) >= 60]
    return {
        "average": avg_grades,
        "max": {"name": max_grade_student, "grade": max_grade},
        "min": {"name": min_grade_student, "grade": min_grade},
        "passing": passing_students
    }

if __name__ == "__main__":
    print(get_student_stats())