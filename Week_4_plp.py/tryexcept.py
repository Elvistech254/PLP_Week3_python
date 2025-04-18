def read_user_file():
    filename = input("Enter the name of the file you want to read: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"\n❌ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"\n⚠️ An unexpected error occurred: {e}")

# Run the function
read_user_file()
