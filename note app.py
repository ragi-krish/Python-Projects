"""
📘 Note-Taking App
1️⃣ Write a Note
2️⃣ View Notes
3️⃣ Search Notes
4️⃣ Delete All Notes
5️⃣ Export Notes to CSV
6️⃣ Exit
"""




import os
import csv
from datetime import datetime

NOTES_FILE = "notes.txt"

def write_note():
    """Write a new note with a category and timestamp"""
    category = input("Enter category (Work/Personal/Study/Others): ").strip()
    note = input("Enter your note: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(NOTES_FILE, "a") as file:
        file.write(f"{timestamp} | {category} | {note}\n")

    print("✅ Note saved successfully!")

def view_notes():
    """View all saved notes"""
    note_path = os.path.abspath(NOTES_FILE)

    print("Note Path:", note_path)
    if not os.path.exists(NOTES_FILE):
        print("⚠ No notes found!")
        return

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    if notes:
        print("\n📜 Your Notes:")
        for note in notes:
            print(note.strip())
    else:
        print("⚠ No notes available.")

def search_notes():
    """Search for a specific note"""
    if not os.path.exists(NOTES_FILE):
        print("⚠ No notes found!")
        return

    keyword = input("Enter a keyword to search: ").strip().lower()
    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    found_notes = [note for note in notes if keyword in note.lower()]
    """
    found_notes = []  # Initialize an empty list to store matching notes

for note in notes:  # Loop through each note in the notes list
    if keyword in note.lower():  # Convert note to lowercase and check if keyword exists
        found_notes.append(note)  # Add the matching note to found_notes

# Now found_notes contains only the notes that matched the keyword

    """
    if found_notes:
        print("\n🔍 Search Results:")
        for note in found_notes:
            print(note.strip())
    else:
        print("⚠ No matching notes found.")

def delete_notes():
    """Delete all notes"""
    confirmation = input("Are you sure you want to delete all notes? (yes/no): ").strip().lower()
    
    if confirmation == "yes":
        if os.path.exists(NOTES_FILE):
            os.remove(NOTES_FILE)
            print("🗑 All notes have been deleted.")
        else:
            print("⚠ No notes to delete.")
    else:
        print("✅ Notes were not deleted.")

def export_notes_to_csv():
    """Export notes to a CSV file"""
    if not os.path.exists(NOTES_FILE):
        print("⚠ No notes found!")
        return

    csv_file = "notes.csv"
    with open(NOTES_FILE, "r") as file, open(csv_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Category", "Note"])
        
        for line in file:
            writer.writerow(line.strip().split(" | "))

    print(f"📄 Notes exported successfully to {csv_file}")

def main():
    """Main menu loop"""
    while True:
        print("\n📘 Note-Taking App")
        print("1️⃣ Write a Note")
        print("2️⃣ View Notes")
        print("3️⃣ Search Notes")
        print("4️⃣ Delete All Notes")
        print("5️⃣ Export Notes to CSV")
        print("6️⃣ Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            write_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_notes()
        elif choice == "5":
            export_notes_to_csv()
        elif choice == "6":
            print("👋 Goodbye! Have a great day.")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
