import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


###############################################################################
# USER INPUT
file_name = "Y164F_EPR.xlsx"
skip_rows = [0]
###############################################################################

df = pd.read_excel(file_name, skiprows=skip_rows, dtype=float)
a = df.to_numpy()
x = a[:, 0]
a = a[:, 1:]
u, s, v = np.linalg.svd(a)

for i in range(3):
    plt.plot(x, u[:, i] * s[i])
plt.show()
