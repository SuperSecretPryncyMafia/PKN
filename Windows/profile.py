import psutil

class Profile:
    @staticmethod
    def profile():
        print(psutil.cpu_percent())
        print(psutil.virtual_memory())
