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



#studens below 70
def students_below_70():
    students_below = []
    for key in class_journal:
        grades = class_journal[key]
        if min(grades) < 70:
            students_below.append(key)
        return students_below
print(f"The student below 70 is {students_below_70()}")