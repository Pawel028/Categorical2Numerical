import pandas as pd
import numpy as np
from scipy.stats.distributions import chi2




class Cat2Num:
    def __init__(self,data,varname,depvar=[],nclass=[],classlist=[], aggregate=[], npoints=[], dist=[], result=[]):
        self.data = data
        self.varname = varname
        self.nclass = nclass
        self.classlist = classlist
        self.depvar = depvar
        self.aggregate=aggregate
        self.npoints = npoints
        self.dist = dist
        self.result = result


    def mode(self):
        return(self)
    
    def find_dist(self):
        return(self)
    
    def update_const(self):
        for name in self.data.columns:
            if name!=self.varname:
                self.depvar=name
        self.classlist = self.data[self.varname].unique()
        self.nclass = len(self.classlist)
        self.npoints = self.data[self.depvar].sum()
        return(self)


    def aggregated(self):
        self.aggregate = self.data.groupby(self.varname).sum()
        return(self)
    
    def find_dist(self):
        self.dist = pd.DataFrame(self.aggregate/self.npoints)
        self.dist.rename(columns={self.depvar:'Dist'})
        return self
    
    def set_number_val(self):
        self.update_const()
        self.aggregated()
        self.find_dist()
        a=pd.concat([self.aggregate, self.dist],axis=1)
        a.columns = [self.depvar,'Dist']
        b=pd.DataFrame(chi2.ppf(a.Dist, df=1))
        b.columns = ['NumVal']
        b.index = self.aggregate.index
        self.result=pd.concat([a,b],axis=1)
        return(self)
