# Task 3
from typing import Callable


class UserAccountDB:
    __database: dict[str: str] = {}

    def __init__(self, user_data: dict[str: str] = None):
        if user_data is None:
            user_data = {}
        self.__database = user_data

    def add_user(self, login, password):
        if self.check_user(login):
            rewrite = input(f"User with login {login} already exists. Overwrite?(y/n)")
            if rewrite == "y":
                self.__database[login] = password
        else:
            self.__database[login] = password

    def remove_user(self, login):
        if self.check_user(login):
            del self.__database[login]

    def check_user(self, login) -> bool:
        return login in self.__database.keys()

    def change_login(self, old_login, new_login):
        if self.check_user(old_login):
            if not self.check_user(new_login):
                self.__database[new_login] = self.__database[old_login]
                del self.__database[old_login]
            else:
                raise ValueError(f"User with login {new_login} already exists.")
        else:
            raise ValueError(f"User with login {old_login} does not exists.")

    def change_password(self, login, new_password):
        if self.check_user(login):
            self.__database[login] = new_password
        else:
            raise ValueError(f"User with login {login} does not exists.")

    def show(self) -> str:
        return str(self.__database)


users = UserAccountDB()
command_dict = {
    1: (users.add_user, " - add new user", ("Enter login>", "Enter password>")),
    2: (users.remove_user, " - delete existing user", ("Enter login>",)),
    3: (users.check_user, " - check if user exist", ("Enter login>",)),
    4: (users.change_login, " - change the login of an existing user", ("Enter old login>", "Enter a new login>")),
    5: (users.change_password, " - change the password of an existing user", ("Enter login>", "Enter a new password>")),
    6: (users.show, " - show all users data", ())
}


def show_menu(menu_dict: dict[int, tuple[Callable, str, ...]]) -> str:
    menu_str = "Menu\n\t0 - quit\n"
    for k, v in menu_dict.items():
        menu_str += "\t" + str(k) + v[1] + "\n"
    return menu_str


while True:
    print(show_menu(command_dict))
    command = int(input("Enter command> "))
    if command in command_dict or command == 0:
        if command == 0:
            print("shutdown...")
            break
        else:
            result: str | None = command_dict[command][0](*[input(prompt) for prompt in command_dict[command][2]])
            print(result if not (result is None) else "")
