class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class UrTube:
    def __int__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for nickname in self.users:
            if nickname == self.users[nickname] and password == self.users[nickname]:
                current_user = nickname

    def register(self, nickname, password, age):
        nickname = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        age = input("Введите возраст: ")
        if nickname in users[]:
            print(f'Пользователь {nickname} уже существует')
        else:
            users[].add(users.nickname, users.password, users.age)





    # def log_out(self):
    #
    # def add(self):
    #
    # def get_video(self):
    #
    # def watch_video(self):




