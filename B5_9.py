import time

class Timer:
    def __init__(self, function, num_runs = 10):
        self.function = function
        self.num_runs = num_runs

    def __call__(self):
        avg_time = 0
        for i in range(self.num_runs):
            t0 = time.time()
            self.function()
            t1 = time.time()
            avg_time += (t1 - t0)
            print(f"Время прогона {i + 1}: {t1 - t0}")
        avg_time /= self.num_runs
        print(f"Среднее время выполнения функции: {avg_time}")
        return self.function()

@Timer
def f():
    for j in range(1000000):
        pass

f()