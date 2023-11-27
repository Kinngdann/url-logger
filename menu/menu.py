
class Menu:
    menu_stack = list()
    def __init__(self):
        self.menu_structure = dict()
        self.current = dict()

    def add_option(self, parent_key:str=None, options:list, nested_key=None):
        if parent_key:
            sub_option = dict()
            # nested_key = nested_key() if callable(nested_key) else self.menu_structure.items()
            for key, value in nested_key.items():
                if key == parent_key:
                    for option in options:
                        sub_option[option] = None
                    self.menu_structure[parent_key] = sub_option # Problem: know the right nested key to append
                    return

                else:
                    if isinstance(value, dict):
                        self.add_option(parent_key, options, lambda: value)
        else:
            for option in options:
                self.menu_structure[option] = None

    def __str__(self):
        print(self.menu_structure)
        # print(self.current)
