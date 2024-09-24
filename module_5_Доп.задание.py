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
        for user_log in self.users:
            if user_log.nickname == nickname and user_log.password == password:
                self.current_user = user_log

    def register(self, nickname, password, age):
        for user_reg in self.users:
            if user_reg.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                new_user = User(nickname, password, age)
                self.users.append(new_user)

    def log_out(self):
        self.current_user = None

    def add(self, title, duration, time_now, adult_mode):
        for video_ in self.videos:
            if video_.title != title:
                new_video = Video(title, duration, time_now, adult_mode)
                self.videos.append(new_video)

    #def get_video(self):
    #
    # def watch_video(self):



