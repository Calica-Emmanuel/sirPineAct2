students_scores = [('Emman', 85), ('Matthew', 92), ('Reymel', 76), ('Gwyneth', 90)]
highest_score = students_scores[0][1]
top_student = students_scores[0][0]

for student, score in students_scores:
    if score > highest_score:
        highest_score = score
        top_student = student

print("Student with the highest score is", top_student, "with a score of", highest_score)
