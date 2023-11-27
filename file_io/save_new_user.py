from utils import File


def save_new_user(user: dict):
    file = File("utils", ".user.txt")

    if not file.file_exists():
        try:
            with open(file.map_dir(), "w") as txt_file:
                user.update({"last_visit": "abc123"})
                txt_file.writelines(str(user))
                print("A query was successfully added.")
        except(IOError, OSError) as e:
            print(f"An error occurred: {e}")
    else:
        print("File already exists")
