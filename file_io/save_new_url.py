import csv
from utils import File


def save_new_url(query_info: dict):
    file = File("utils", "query_list.csv")
    csv_header = [key for key in query_info]

    try:
        file_path = file.map_dir()
        file_exists = file.file_exists()

        with open(file_path, mode="a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_header)

            if not file_exists:
                writer.writeheader()

            writer.writerow(query_info)
        print("A query was successfully added.")

    except (IOError, OSError) as e:
        print(f"An error occurred: {e}")
