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

    def get_video(self, word):
        result = []
        for title in self.title:
            if word.lower() in title.lower():
                result.append(title)
            return result

    def watch_video(self, title):
        for name_video in self.title:
            if name_video == title:
                self.duration = name_video
                self.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

