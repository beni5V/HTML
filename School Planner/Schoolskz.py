# PART 1 — STUDENT PROFILE (TUPLE)
student_profile = ("Hussain Mustafa", "Grade 6", "Section F", 6)
print("╔══════════════════════════════════════╗")
print("║       MY SCHOOL SUBJECT PLANNER      ║")
print("╚══════════════════════════════════════╝")

print("\nSTUDENT PROFILE")
print("──────────────────────────────────────")
print("Name          :", student_profile[0])
print("Grade         :", student_profile[1])
print("Section       :", student_profile[2])
print("Total Subjects:", student_profile[3])

# PART 2 — ACCESSING TUPLE ELEMENTS
student_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
total_subjects = student_profile[3]

print("\nPROFILE DETAILS")
print("──────────────────────────────────────")
print("Student Name  :", student_name)
print("Grade         :", grade)
print("Section       :", section)

print("\nFirst Two Details:", student_profile[0:2])

# PART 3 — SUBJECT SETS
monday_subjects = {"Math", "Science", "English", "Computer", "Art"}
tuesday_subjects = {"Math", "History", "English", "Sports", "Music"}

print("\nWEEKLY SUBJECTS")
print("──────────────────────────────────────")
print("Monday Subjects :", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)


# PART 4 — UPDATING SUBJECTS
monday_subjects.add("Library")
monday_subjects.discard("Art")

tuesday_subjects.add("Computer")
tuesday_subjects.discard("Music")

print("\nUPDATED SUBJECTS")
print("──────────────────────────────────────")
print("Monday Subjects :", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)


# PART 5 — SET OPERATIONS
all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects)
only_tuesday = tuesday_subjects.difference(monday_subjects)
different_subjects = monday_subjects.symmetric_difference(tuesday_subjects)
print("\nSUBJECT ANALYSIS")
print("──────────────────────────────────────")
print("All Subjects          :", all_subjects)
print("Common Subjects       :", common_subjects)
print("Only Monday           :", only_monday)
print("Only Tuesday          :", only_tuesday)
print("Different Subjects    :", different_subjects)

# FINAL SUMMARY
print("\n╔══════════════════════════════════════╗")
print("║           FINAL SUMMARY              ║")
print("╚══════════════════════════════════════╝")
print("Student            :", student_name)
print("Grade              :", grade)
print("Monday Subjects    :", monday_subjects)
print("Tuesday Subjects   :", tuesday_subjects)
print("Subjects on Both   :", common_subjects)
print("All Unique Subjects:", all_subjects)

print("\n✦ Stay organized. Study smart. ✦")
print("========================================")