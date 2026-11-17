import csv
passed = []
failed = []
scores = []

filepath = "student_test_scores.csv"
with open(filepath, "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for line in reader:
        name = line[0]
        score = int(line[1])
        scores.append(score)

        if score >= 70:
            passed.append(line)
        else:
            failed.append(line)

#Passed
with open("passed.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(passed)
 
#Failed
with open("failed.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(failed)
 
#Highest, lowest, average
highest = max(passed + failed, key=lambda x: int(x[1]))
lowest = min(passed + failed, key=lambda x: int(x[1]))
average = sum(scores) / len(scores)
 
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")
