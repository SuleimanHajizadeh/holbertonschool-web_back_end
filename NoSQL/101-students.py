#!/usr/bin/env python3
"""101-students.py"""
def top_students(mongo_collection):
    """
    Returns all students sorted by average score (descending).
    Adds 'averageScore' key to each student dictionary.
    """
    students = list(mongo_collection.find())
    for student in students:
        topics = student.get("topics", [])
        if topics:
            avg = sum(topic.get("score", 0) for topic in topics) / len(topics)
            student["averageScore"] = avg
        else:
            student["averageScore"] = 0
    return sorted(students, key=lambda s: s["averageScore"], reverse=True)

