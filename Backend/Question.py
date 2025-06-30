from User import User
import DBFetcher


class Question:
    def __init__(self, question, answer, level, unit, type, style):
        self.question = question
        self.answer = answer
        self.level = level
        self.type = type
        self.style = style

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def getLevel(self):
        return self.level

    def getType(self):
        return self.type

    def getUnit(self):
        return self.unit

    def getGrade(self, answer):
        return self.answer.getGrade()

    def getStyle(self):
        return self.style

    def getUnit(self):
        return self.unit

    def getPoints(self, user: User, grade: float):
        expectedPts = 1 / (1 + 10 ** ((user.getLevel() - self.level) / 400))
        if user.getLevel() > DBFetcher.getMaxLevel(self.type) / 1.6:
            K = 16
        else:
            K = 32

        points = K * (grade - expectedPts)

        return points
