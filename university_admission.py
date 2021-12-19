maximum_number_of_students = int(input())

with open("applicant_list.txt", "r") as f:
    applicants = [x.split() for x in f.readlines()]
    rearranged = [[x[0] + " " + x[1], round((float(x[3]) + float(x[2])) / 2, 1), float(x[3]), round((float(x[5]) +
    float(x[4])) / 2, 1), float(x[4]), round((float(x[2]) + float(x[4])) / 2, 1), float(x[6]), x[7], x[8], x[9]] for x in applicants]
    departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
    successful = {department: [] for department in departments}

    ad_note_index = 6
    for priority in range(7, 10):
        for department in departments:
            filtered = list(filter(lambda x: department == x[priority], rearranged))
            sort = sorted(filtered, key=lambda x: (-max(x[6], x[departments.index(department) + 1]), x[0]))
            candidates = sort[:maximum_number_of_students - len(successful[department])]
            printable = [[x[0], max(x[6], x[departments.index(department) + 1])] for x in candidates]
            successful[department].extend(printable)
            for x in candidates:
                rearranged.remove(x)

    for department, students in successful.items():
        with open(department + ".txt", "w") as new_file:
            proper = sorted(students, key=lambda x: (-x[1], x[0]))
            result = "\n".join([student[0] + " " + str(student[1]) for student in proper])
            new_file.write(result)
