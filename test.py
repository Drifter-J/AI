class test(individual):
	def __init__(self, answer, genLimit=200, size=400,pbCO=0.8,pbM=0.000000011):
		# 변수 값은 정하기 나름
		self.genCnt = 0 # 몇 세대까지 갔는지 세기 위한 변수 
		self.genLimit = genLimit # n세대를 넘어가도 답을 맞추지 못하면 강제로 멈추기 위한 변수
		self.size = size # 크로모섬의 크기
		self.pbCO = pbCO # crossover 확률
		self.pbM = pbM # mutate 확률
		self.answer = self.ansToChromo(answer) # 제공된 답의 코드 값
		self.listOfAnswer = answer # 답
	
	def init(self): 
		# 처음으로 크로모솜을 선언된 크기만큼 랜덤하게 만든다.
		return [self.randomChromo() for i in range(self.size)]

	def fitness(self, chromosome):
		# 높으면 높을수록 next generation에 survive할 확률이 높다.
		return -sum(abs(a - b) for a, b in zip(chromosome, self.answer))

	def pbCrossover(self): return self.pbCO

	def pbMutate(self): return self.pbM

	def step(self, fitPop):
		# 한 세대를 넘어가기위해 수행되는 함수
		self.genCnt = self.genCnt + 1
		match = list(sorted(fitPop))[-1][1]
		fit = [d for d, char in fitPop]
		best = max(fit) # 가장 높은 fitness값
		avg = sum(fit)/len(fit) # fitness 중간값
		worst = max(fit) # 가장 낮은 fitness값
		# 만약 다음 세대에 generate된 군집이 사용자가 임의로 입력한 답과 같지 않으면 next generation으로 가고
		if(self.chromoToAns(match) != self.listOfAnswer):
			print("%d Gen - new(best:%d avg:%d worst:%d): %r origin: %r" % (self.genCnt, best, avg, worst, 
					self.chromoToAns(match), self.listOfAnswer))
		# 아니면 stop, 강제로 limit까지 점프한다.
		else:cnt를 
			print("%d Gen - new(best:%d avg:%d worst:%d): %r origin: %r" % (self.genCnt, best, avg, worst, 
					self.chromoToAns(match), self.listOfAnswer))
			self.genCnt = self.genLimit
		# 임의로 설정한 세대수 limit을 넘어버리면 답을 찾지 못하더라도 종료한다.	
		return self.genCnt >= self.genLimit	

	def parents(self, fitPop):
		# selection(선택 연산자)가 진행되는 파트
		while True: # 룰렛방식이 아닌 토너먼트 방식으로 부모 둘이 선택된다.
			firstParent = self.tournament(fitPop)
			secondParent = self.tournament(fitPop)
			yield (firstParent, secondParent)

	def crossover(self, parents):
		# crossover가 진행되는 파트
		# 부모의 일부분을 때어 다른 부모의 일부분과 합친다.
		# 일부분은 랜덤함수로 선택하게 되어있다.
		# 이렇게 crossover으로 새로이 탄생된 child들을 return한다.  
		firstParent, secondParent = parents 
		firstIndex = random.randint(1, len(self.answer) - 2)
		secondIndex = random.randint(1, len(self.answer) - 2)
		if firstIndex > secondIndex: firstIndex, secondIndex = secondIndex, firstIndex
		firstChild = firstParent[:firstIndex] + secondParent[firstIndex:secondIndex] + firstParent[secondIndex:]
		secondChild = secondParent[:firstIndex] + firstParent[firstIndex:secondIndex] + secondParent[secondIndex:]
		return (firstChild, secondChild)

	def mutate(self, chromosome):
		# mutate가 진행되는 파트
		# 마찬가지로 random하게 mutate될 일부분을 선택하며,
		# 돌연변이가 된 개체를 return한다.
		index = random.randint(0, len(self.answer) - 1)
		difference = random.randint(-4, 4)
		mutant = list(chromosome)
		# mutate할 때 잘못된 ascii 값이 나올 수 있기 때문에 if문에서 예외 처리를 해줄 수 있는데,
		# 이 경우 생물에서 일어나는 true mutation이 아니기 때문에 (mutation이 항상 좋은 결과를
		# 가져다 주는 것은 아니므로) 일단 방법만 소개했다.  
		#if(mutant[index]+difference < 53 and mutant[index]+difference > 48): mutant[index] += difference
		mutant[index] += difference
		return mutant

	def tournament(self, fitPop):
		# 토너먼트 방식으로 알고리즘을 구성했다.
		# 임의로 개체를 무작위로 선택한 후 그 중 fitness가 높은 개체를 next generation으로 삼는다.
		fpFit, firstParent = self.selectRandom(fitPop)
		spFit, secondParent = self.selectRandom(fitPop)
		return firstParent if fpFit > spFit else secondParent

	def selectRandom(self, fitPop):
		return fitPop[random.randint(0, len(fitPop)-1)]
 
	def ansToChromo(self, answer):
		return [ord(char) for char in answer]
       
	def chromoToAns(self, chromosome):
		# 49='1', 50='2', 51='3', 52='4'
		# 답은 1과 4사이의 정수이므로  chromosome을 만들 때도 1-4로 구성되게끔 한다.
		return "".join(chr(max(49, min(char, 52))) for char in chromosome)
 
	def randomChromo(self):
		# 49='1', 50='2', 51='3', 52='4'
		return [random.randint(49, 52) for i in range(len(self.answer))]
