%matplotlib inline 
from matplotlib.pyplot import *
import numpy as np

index = []
j = 0

for i in range(0,len(generationCnt)):
    j+=1
    index.append(j)

sumGen = 0
    
for i in range(0,len(generationCnt)):
    sumGen += generationCnt[i]    
    
print sumGen
print len(generationCnt)

y = np.array(generationCnt)
x = np.array(index)

fig, ax = plt.subplots(figsize=(10,10))

# visual setting
matplotlib.rcParams.update({'font.size': 10})
ax.spines['top'].set_visible(False) 
ax.spines['right'].set_visible(False) 
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()  

# rotating the axis text
fig.autofmt_xdate()

# labeling
plt.title('Probability of Crossover = '+ str(probCrossover[0]) +'\n'
          + 'Probability of mutation = ' + str(probMutation[0]) + '\n' 
          + 'Size of Chromosome = ' + str(sizeOfChromo[0]) + '\n')
plt.xlabel('Iteration\n')
plt.ylabel('# of Generation\n')

plt.autoscale(enable=True, axis=u'both', tight=False) 

width =1
tab = np.arange(len(generationCnt))

ax.bar(tab, y, width, color = "#0987B2")

plt.legend(["Avg Generation: " + str(sumGen/len(generationCnt))],loc = "left", fancybox=True)

plt.draw()
plt.savefig("fig")
plt.show()