import pandas as pd

import numpy as np

a = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

a.to_csv('./test.csv')  

print('succes')