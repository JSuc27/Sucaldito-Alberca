try:
    print("=== File Handling Exercise ===")
    note1 = input("Enter your first short notes/message: ")
    
    with open("notes.txt", "w") as file:
        file.write(note1 + "\n")
    
    print("\n✅ Message saved to notes.txt")

    print("\n--- Reading the file ---")
    with open("notes.txt", "r") as file:
        content = file.read()
    print("File content:")
    print(content)

    note2 = input("\nEnter another note to append: ")
    
    with open("notes.txt", "a") as file:
        file.write(note2 + "\n")
    
    print("✅ Second note appended successfully")

    print("\n--- Updated file content ---")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
    print(updated_content)

except FileNotFoundError:
    print("❌ Error: The file 'notes.txt' was not found!")
except PermissionError:
    print("❌ Error: Permission denied when accessing the file!")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

else:
    print("\n🎉 Program completed successfully!")
