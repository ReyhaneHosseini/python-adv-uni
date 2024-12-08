import requests

class Fetcher:
    def __init__(self):
        response = requests.get("https://cdn.ituring.ir/ex/users.json")
        self.students = response.json()

    def nerds(self):
        return {f"{student['first_name']} {student['last_name']}" for student in self.students if student['score'] > 18.5}

    def sultans(self):
        max_score = max(student['score'] for student in self.students)
        return tuple(f"{student['first_name']} {student['last_name']}" for student in self.students if student['score'] == max_score)

    def mean(self):
        return sum(student['score'] for student in self.students) / len(self.students)

    def get_students(self):
        return [{key: student[key] for key in student if key not in ['city', 'province', 'location']} for student in self.students]