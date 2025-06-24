class_journal = {
    "Layla": [89, 91, 86],
    "Tariq": [77, 84, 73],
    "Jana": [100, 97, 94],
    "Ziad": [62, 71, 75]
}

def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)
#print the class_journal
for key in class_journal:
    print(f"{key} has grades {class_journal[key]} and the average grade is {calculate_average(class_journal[key])}")
 #highest avg
def highest_average():
    highest_avg = 0
    highest_avg_name = ""
    for key in class_journal:
        avg = calculate_average(class_journal[key])
        if avg > highest_avg:
            highest_avg = avg
            highest_avg_name = key
    return highest_avg_name
print(f"THe student with highest average is {highest_average()} ")

#most consistent performance
def most_consistent_performance():
    most_consistent = 0
    most_consistent_name = ""
    for key in class_journal:
        grades = class_journal[key]

        highest = grades[0]
        lowest = grades[0]
        for grade in grades:
            if grade > highest:
                highest = grade
            if grade < lowest:
                lowest = grade
    diff = highest - lowest
    if smallest_diff is None or diff < smallest_diff:
            smallest_diff = diff
            most_consistent_name = key

    return most_consistent_name, smallest_diff
print(f"The most consistent performance's student is {most_consistent_performance()} ")

#studens below 70
def students_below_70():
    students_below = []
    for key in class_journal:
        grades = class_journal[key]
        if min(grades) < 70:
            students_below.append(key)
        return students_below
print(f"The student below 70 is {students_below_70()}")