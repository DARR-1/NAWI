import pandas as pd
import random
from User import User
import DBFetcher
from Question import Question

db = pd.read_csv("questions.csv")


def getQuestion(level, type: str, topic: str, user):
    if topic is None:
        id = random.randint(0, len(db["question"][level][topic][type]) - 1)
        question = db["question"][level][
            random.randint(0, user.getUnlockedTopics() - 1)
        ][type][id]
    else:
        id = random.randint(0, len(db["question"][level][topic][type]) - 1)
        question = db["question"][level][topic][type][id]

    return question


def getQuestions(user, size: int, topic=None, type=None):
    questions = []

    for i in range(size):
        if type is None:
            for j in range(4):
                if i < size / 2:
                    question = getQuestion(user.getLevel(type) + 100, j, topic, user)
                else:
                    question = getQuestion(user.getLevel(type), j, topic, user)
        else:
            for j in range(4):
                for k in range(type[k]):
                    if i < size / 2:
                        question = getQuestion(
                            user.getLevel(type) + 100, k, topic, user
                        )
                    else:
                        question = getQuestion(user.getLevel(type), k, topic, user)

        questions.append(question)

    return questions
