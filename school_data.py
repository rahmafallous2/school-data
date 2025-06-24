class_journal = {
    "Layla": [89, 91, 86],
    "Tariq": [77, 84, 73],
    "Jana": [100, 97, 94],
    "Ziad": [62, 71, 75]
}
#avg for each student
def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)
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
    smallest_diff = None  
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

    return most_consistent_name

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

#total grades entered across the whole class
def total_grades():
    total = 0
    for key in class_journal:
        grades = class_journal[key]
        count = 0
        for grade in grades:
            count += 1  
        total += count  
    return total

print(f"The total number of grades entered is {total_grades()}")

#overall class avg
def overall_class_avg():
    total = 0
    count = 0
    for key in class_journal:
        grades = class_journal[key]
        for grade in grades:
            total += grade
            count += 1
    return total/count if count != 0 else 0

print(f"The overall class average is {overall_class_avg()}")

#new grades
new_grades = [["Jana", 99], ["Ziad", 78], ["Layla", 84]]
for student, grade in new_grades:
    class_journal[student].append(grade)

#print the class_journal in txt file
def printJournal():
    output = ""
    for key in class_journal:
        output += f"{key} has grades {class_journal[key]} and the average grade is {calculate_average(class_journal[key])}\n"
    return output
#txt file
output_text = ""
output_text += printJournal()

highest_student = highest_average()
output_text += f"\nThe student with the highest average is {highest_student}\n"

most_consistent_student, consistency_diff = most_consistent_performance()
output_text += f"The most consistent performance's student is {most_consistent_student} \n"

students_below = students_below_70()
output_text += f"Students with any grade below 70: {', '.join(students_below) if students_below else 'None'}\n"

total = total_grades()
output_text += f"Total number of grades entered: {total}\n"

overall_avg = overall_class_avg()
output_text += f"Overall class average is: {overall_avg}\n"

# saving output to text file
with open("grades_analysis_report.txt", "w") as file:
    file.write(output_text)

print("Analysis saved to 'grades_analysis_report.txt'")
