import time

class Timer:
	#Конструктор с аргументом по умолчанию 
	def __init__(self, num_runs = 10):
		self.num_runs = num_runs

	#функция вызываемая, когда пишем Timer()
	def __call__(self, func):
		def wrap(*args, **kwargs):
			avg_time = 0
			for _ in range(self.num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
				avg_time += t1 - t0
			avg_time /= self.num_runs
			print("Выполнение заняло %.5f секунд" % avg_time)
		return wrap

	#запускается через with 
	def __enter__(self):
		self.t0 = time.time()
		return
		
	#Запускается, когда выходим из тела with
	def __exit__(self, *args, **kvargs):
		avg_time = (time.time() - self.t0)
		print("Выполнение заняло %.5f секунд" % avg_time)


#Используем класс, через специальную функцию __call__ 
@Timer()
def f():
    for j in range(1000000):
        pass

#Вспомогательная функция без декоратора
def g():
    for j in range(1000000):
        pass

def main():
	#создаем объект класса
	timer = Timer()

	#вызываем фунцию f
	f()

	#Используем класс, через специальные функции __enter__, __exit__
	with timer as t:
		g()


if __name__=="__main__":
	main()