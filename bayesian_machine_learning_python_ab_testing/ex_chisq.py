# Goal: determine whether or not the CTRs are statistically significantly different
import pandas as pd
from scipy.stats import chi2
import numpy as np

def get_p_value(T):
    det = T[0, 0]*T[1,1] - T[0, 1]*T[1,0]

    # chi^2 = (ad - bc)^2 (a + b + c + d) / [ (a + b)(c + d)(a + c)(b + d)]
    # degrees of freedom = (#cols - 1) x (#rows - 1) = (2 - 1)(2 - 1) = 1

    c2 = float(det) / T[0].sum() * det / T[1].sum() * T.sum() / T[:, 0].sum() / T[:, 1].sum()
    p = 1 - chi2.cdf(x=c2, df=1)
    return p

data = pd.read_csv('advertisement_clicks.csv')

clicks_A = data[data['advertisement_id'] == 'A']['action']
clicks_B = data[data['advertisement_id'] == 'B']['action']

A_clk = clicks_A.sum()
A_noclk = clicks_A.size - A_clk
B_clk = clicks_B.sum()
B_noclk = clicks_B.size - B_clk

T = np.array([[A_clk, A_noclk], [B_clk, B_noclk]])

p = get_p_value(T)

print(p)
