import random

class GA(object):
	def __init__(self, chromosome):
		self.chromosome = chromosome

	def execute(self):
		pop = self.chromosome.init()
		while True:
			# char는 아스키 코드 캐릭터를 의미하며, 이는 다음과 같이 변환된다. 
			# 49='1', 50='2', 51='3', 52='4'
			fitPop = [(self.chromosome.fitness(char), char) for char in pop]
			if self.chromosome.step(fitPop): break
			pop = self.next(fitPop)
		return pop

	def next(self, fit):
		makeParents = self.chromosome.parents(fit)
		size = len(fit)
		nextGen = []
		while len(nextGen) < size:
			# 설정한 크로모솜 크기만큼의 해집단을 생성한다. 
			parents = next(makeParents)
			# 설정한 crossover 확률보다 낮은 랜덤수(doCrossover는 true || false)가 나온다면,
			# parents끼리 crossover를 시키고, 아니면 original parents를 children(=자식)으로
			# 삼는다. 
			doCrossover = random.random() < self.chromosome.pbCrossover()
			children = self.chromosome.crossover(parents) if doCrossover else parents
			for char in children:
				# 설정한 mutation 확률보다 낮은 랜덤수가 나온다면,
				# children의 부분을 mutate시킨다.
				doMutate = random.random() < self.chromosome.pbMutate()
				nextGen.append(self.chromosome.mutate(char) if doMutate else char)
		# 생성이 완료되었다면 Next generation으로 proceed한다. 		
		return nextGen[0:size]	