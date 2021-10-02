import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')
df["status"] = "allowed"


info = df["course name"] == "information technology"
freshmen = df["year"] == 1
df.loc[info & freshmen, "status"] = "not allowed"

commerce = df["course name"] == "commerce"
senior = df["year"] == 4
df.loc[commerce & senior, "status"] = "not allowed"

allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"


df
