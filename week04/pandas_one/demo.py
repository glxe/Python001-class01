import numpy as np
import pandas as pd
df = pd.DataFrame({"Person":
                   ["John", "Myla", "Lewis", "John", "Myla"],
                   "Age": [24., np.nan, 21., 33, 26],
                   "Single": [False, True, True, True, False]})


df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'order_id': ['aaaaaaaa', 'bbbbbbbbbb', 'ccccccccccc', 'dddddddddd', 'eeeeeeeeeee', 'fffffffffff', 'gggggggggggg',
    'hhhhhhhhhhh', 'aaaaaaaa']
})