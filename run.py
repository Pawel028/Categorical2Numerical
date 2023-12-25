import pandas as pd
import numpy as np
from Cat2Num import Cat2Num
from numpy import random
from scipy.stats.distributions import chi2

data = pd.read_excel("pivot1.xlsx")
data1 = pd.DataFrame({'Prov_Nm':data.Prov_Nm,'Claims':data.Claims})
Cat2Num_obj = Cat2Num(data=data1,varname='Prov_Nm')
Cat2Num_obj.set_number_val()
print(Cat2Num_obj.result.NumVal[Cat2Num_obj.result.index=='Match'])
