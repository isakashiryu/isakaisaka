import sys
sys.path.append('/Users/michel/anaconda3/lib/python3.10/site-packages')
import numpy as np

def arange_square_matrix(n):
    return np.array([np.arange(i, n+i) for i in range(n)])

                                     # ↑for文にはこんな使い方もある
                                     #  内包表記て奴らしい


      


