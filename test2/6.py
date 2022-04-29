import pandas as pd


s = pd.Series([244, 814, 446, 787, 523, 317])
print((int((s.min() + s.mean()) is None) * 2 + 7 * 2) ** 0.5)
