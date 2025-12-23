import os
def create_file():
    filename=input("Enter file name: ")
    try:
        with open(filename,'x'):
            print("File created successfully.")
    except FileExistsError:
        print("Error: File already exists.")
def write_file():
    filename=input("Enter file name: ")
    data=input("Enter content to write: ")
    with open(filename,'w') as f:
        f.write(data)
    print("Data written successfully.")
def read_file():
    filename=input("Enter file name: ")
    try:
        with open(filename,'r') as f:
            print("\n--- File Content ---")
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")
def append_file():
    filename=input("Enter file name: ")
    data=input("Enter content to append: ")
    with open(filename,'a') as f:
        f.write("\n"+data)
    print("Data appended successfully.")
def replace_text():
    filename=input("Enter file name: ")
    try:
        with open(filename,'r') as f:
            content=f.read()
        old_text=input("Enter text to replace: ")
        new_text=input("Enter new text: ")
        if old_text not in content:
            print("Error: Text not found in file.")
            return
        content=content.replace(old_text,new_text)
        with open(filename,'w') as f:
            f.write(content)
        print("Text replaced successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
def rename_file():
    old_name=input("Enter current file name: ")
    if not os.path.exists(old_name):
        print("Error: File does not exist.")
        return
    new_name=input("Enter new file name: ")
    if os.path.exists(new_name):
        print("Error: A file with the new name already exists.")
        return
    os.rename(old_name,new_name)
    print("File renamed successfully.")
def delete_file():
    filename=input("Enter file name: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("Error: File does not exist.")
def menu():
    while True:
        print("\n===== File Handling Application =====")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Replace Text")
        print("6. Rename File")
        print("7. Delete File")
        print("8. Exit")
        choice=input("Enter your choice (1-8): ")
        if choice=='1':
            create_file()
        elif choice=='2':
            write_file()
        elif choice=='3':
            read_file()
        elif choice=='4':
            append_file()
        elif choice=='5':
            replace_text()
        elif choice=='6':
            rename_file()
        elif choice=='7':
            delete_file()
        elif choice=='8':
            print("Exiting application. Thank you!")
            break
        else:
            print("Error: Invalid option! Please enter a number between 1 and 8.")
menu()
