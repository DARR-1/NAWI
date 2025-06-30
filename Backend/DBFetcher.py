import pandas as pd


def getMaxLevel(type: str):
    db = pd.read_csv("users.csv")
    return db[type].max()


def getTopicsNum():
    db = pd.read_csv("topics.csv")
    return len(db["topics"])
