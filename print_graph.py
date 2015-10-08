%matplotlib inline 
import matplotlib.pyplot as plt
import numpy as np

index = []
j = 0
fitness=[-6, -5, -4, -1, -1, 0]
for i in range(0,generationCnt[-1]):
    j+=1
    index.append(j)

print index

y = np.array(fitness)    
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

plt.autoscale(enable=True, axis=u'both', tight=False) 

# labeling
plt.title('Probability of Crossover = '+ str(probCrossover[0]) +'\n'
          + 'Probability of mutation = ' + str(probMutation[0]) + '\n' 
          + 'Size of Chromosome = ' + str(sizeOfChromo[0]) + '\n')
plt.xlabel('# of Generation\n')
plt.ylabel('Avg fitness\n')


line = ax.plot(x, y, 'r-o', color = 'red')

plt.draw()
plt.savefig("fig")
plt.show()