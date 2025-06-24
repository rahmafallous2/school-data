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