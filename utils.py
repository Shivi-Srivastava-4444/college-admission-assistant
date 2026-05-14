import pandas as pd


def recommend_colleges(course, marks, city, budget, college_type):
    df = pd.read_csv("colleges.csv")

    filtered = df[
        (df["course"] == course) &
        (df["min_percentage"] <= marks) &
        (df["fees"] <= budget)
    ]

    if city:
        filtered = filtered[
            filtered["location"].str.contains(city, case=False, na=False)
        ]

    if college_type != "Any":
        filtered = filtered[
            filtered["type"] == college_type
        ]

    return filtered


def recommend_scholarships(marks):
    df = pd.read_csv("scholarships.csv")

    filtered = df[
        df["min_percentage"] <= marks
    ]

    return filtered