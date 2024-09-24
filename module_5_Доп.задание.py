class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user_log in self.users:
            if user_log.nickname == nickname and user_log.password == password:
                self.current_user = user_log
                return

    def register(self, nickname, password, age):
        for user_reg in self.users:
            if user_reg.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                new_user = User(nickname, password, age)
                self.users.append(new_user)

    def log_out(self):
        self.current_user = None

    def add(self, title, duration):
        for video_ in self.videos:
            if video_.title != title:
                new_video = Video(title, duration)
                self.videos.append(new_video)
                return

    def get_videos(self, poisk):
        result = []
        for video in self.videos:
            if poisk.lower() in video.title.lower():
                result.append(video.title)
                return result

    def watch_video(self, name_video, sleep=None):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if name_video.lower() in video.title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(1, 11):
                        print(i, end='')
                        sleep(1)
                    print(" Конец видео")
                    return
                return

    #   if self.age < 18:
    #     print("Вам нет 18 лет, пожалуйста покиньте страницу")
    #     return
    #
    #   for name_video in self.title:
    #     if name_video == self.title:
    #         self.duration = name_video
    #         self.time.sleep(1)
    #         print("Конец видео")
    #         self.time_now = 0


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
