import os


class File:
    DIRS = {
        "utils": "./.files/.utils/",
        "logs": "./.files/.logs/"
    }

    def __init__(self, file_type, file_name: str):
        self.file_type = file_type
        self.file_name = file_name

    @property
    def file_type(self) -> str:
        return self._file_type

    @file_type.setter
    def file_type(self, file_type: str):
        if file_type in self.DIRS:
            self._file_type = file_type
        else:
            raise ValueError(f"Invalid file type: {file_type}")

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
        split_file_name = file_name.split(".")
        if len(split_file_name) > 1 and split_file_name[-1] in ["csv", "txt"]:
            self._file_name = file_name
        else:
            raise ValueError("Invalid file name or extension")

    def map_dir(self) -> str:
        return os.path.join(self.DIRS[self._file_type], self._file_name)

    def file_exists(self) -> bool:
        file_path = self.map_dir()
        if os.path.exists(os.path.dirname(file_path)):  # Check if the directory exists
            return os.path.exists(file_path)  # Check if the file exists within the directory
        return False  # Return False if either directory or file doesn't exist

