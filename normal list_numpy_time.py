import time

""":cvar

start=time.time()

price =  [i*10 for i in range(100000)]
earning = [i+0.001 for i in range(100000)]


price_to_earn=[]
for i,j in zip(price,earning):
    price_to_earn.append(i/j)

end=time.time()

print("Total time is : ", end-start)

# Output : Total time is :  0.04587960243225098

Commenting the above code and running with numpy
"""

import numpy as np

start=time.time()

price_n=np.array([i*10 for i in range(100000)])
earning_n=np.array([i+0.001 for i in range(100000)])
np.divide(price_n,earning_n)

end=time.time()

print("Total time is : ", end-start)

# output for above code ==>  Total time is :  0.029961109161376953
# Usage of numpy is faster than normal list