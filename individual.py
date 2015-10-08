class individual(object): 
	# Constructor
	# individual class를 초기화 시킨다. (default값 설정)
	def init(self): return [] 
	# initial population을 리턴한다. 

	def fitness(self, chromosome): return len(chromosome) 
	# 크로모솜의 fitness value를 리턴한다.

	def step(self, fitPop): return False
	#True를 return하게 되면 멈춘다.
	#fitPop은 finess value와 	크로모솜의 리스트다.
		
	def parents(self, fitPop):
		# 부모 선택(tournament selection을 사용할 것임)
		generation = iter(sorted(fitPop))
		while True:
			firstFit, firstChar = next(generation)
			secondFit, secondChar = next(generation)
			yield (firstChar, secondChar)
		return

	def crossover(self, parents): return parents # crossover 함수

	def mutate(self, chromosome): return chromosome	# mutate 함수
		
	def pbCrossover(self): return 1.0 # crossover하는 확률

	def pbMutate(self): return 0.000000011 # mutate하는 확률