print("======================================")
print("      SMART NOTES ORGANIZER")
print("======================================")

sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n"
]

with open("class-notes.txt", "w") as file:
    file.writelines(sample_notes)

print("Sample file created successfully.\n")

print("PART 1: Preview File")

with open("class-notes.txt", "r") as file:
    print(file.read(50))

print("\nPART 2: Display All Notes")

with open("class-notes.txt", "r") as file:
    notes = file.readlines()

print("Total Notes:", len(notes))

for number, note in enumerate(notes, start=1):
    print(f"{number}. {note.strip()}")

print("\nPART 3: Reading Line by Line")

with open("class-notes.txt", "r") as file:
    for note in file:
        print(">", note.strip())

print("\nPART 4: Filter Notes")

important = 0
todo = 0

with open("class-notes.txt", "r") as file:
    for note in file:
        if note.startswith("SKIP"):
            print("Skipped:", note.strip())
        else:
            print("Kept:", note.strip())

        if note.startswith("IMPORTANT"):
            important += 1
        elif note.startswith("TODO"):
            todo += 1

print("\nPART 5: Saving Selected Notes")

with open("organized-notes.txt", "w") as output:
    for note in notes:
        if note.startswith(("IMPORTANT", "TODO")):
            output.write(note)

print("organized-notes.txt created successfully.")

print("\nOrganized Notes")

with open("organized-notes.txt", "r") as file:
    for note in file:
        print(note.strip())

print("\n======================================")
print("SUMMARY")
print("======================================")
print("Previewed first 50 characters using read(n).")
print("Read all lines using readlines().")
print("Looped through the file line by line.")
print("Filtered SKIP notes.")
print(f"IMPORTANT Notes : {important}")
print(f"TODO Notes      : {todo}")
print("Saved IMPORTANT and TODO notes into organized-notes.txt.")
print("======================================")