# MCVar.py

import numpy as np
from scipy.stats import rv_continuous, rv_discrete, describe
from scipy.stats.stats import DescribeResult
from monaco.MCVal import MCVal, MCInVal, MCOutVal
from monaco.MCVarStat import MCVarStat
from monaco.MCEnums import SampleMethod
from monaco.mc_sampling import mc_sampling
from copy import copy
from typing import Union, Any
from warnings import warn
from abc import ABC, abstractmethod


### MCVar Base Class ###
class MCVar(ABC):
    def __init__(self, 
                 name              : str, 
                 ndraws            : int, 
                 firstcaseismedian : bool,
                 ):
        self.name = name 
        self.ndraws = ndraws 
        self.firstcaseismedian = firstcaseismedian
        
        self.ncases = ndraws + 1
        self.setFirstCaseMedian(firstcaseismedian)
        self.vals       : list[Any]
        self.valmap     : dict
        self.nums       : list[float]
        self.nummap     : dict
        self.pcts       : list[float]
        self.size       : tuple
        self.isscalar   : bool
        self.mcvarstats : list[MCVarStat] = []
        

    def setFirstCaseMedian(self, 
                           firstcaseismedian : bool,
                           ) -> None:
        if firstcaseismedian:
           self.firstcaseismedian = True
           self.ncases = self.ndraws + 1
        else:
           self.firstcaseismedian = False
           self.ncases = self.ndraws


    def stats(self) -> DescribeResult:
        stats = describe(self.nums)
        return stats
    
    
    def addVarStat(self, 
                   stattype   : str, 
                   statkwargs : dict[str, Any] = None, 
                   name       : str = None,
                   ) -> None:
        if statkwargs is None:
            statkwargs = dict()
        self.mcvarstats.append(MCVarStat(mcvar=self, stattype=stattype, statkwargs=statkwargs, name=name))


    def clearVarStats(self) -> None:
        self.mcvarstats = []


    @abstractmethod
    def getVal(self, 
               ncase : int,
               ) -> MCVal:
        pass

    @abstractmethod
    def getMedian(self) -> Any:
        pass



### MCInVar Class ###
class MCInVar(MCVar):
    def __init__(self, 
                 name              : str, 
                 ndraws            : int, 
                 dist              : Union[rv_discrete, rv_continuous], 
                 distkwargs        : dict         = None,
                 nummap            : dict         = None,
                 samplemethod      : SampleMethod = SampleMethod.SOBOL_RANDOM,
                 ninvar            : int          = None,
                 seed              : int          = np.random.get_state(legacy=False)['state']['key'][0], 
                 firstcaseismedian : bool         = False,
                 autodraw          : bool         = True,
                 ):
        super().__init__(name=name, ndraws=ndraws, firstcaseismedian=firstcaseismedian)
        
        self.dist = dist
        if distkwargs is None:
            distkwargs = dict()
        self.distkwargs = distkwargs
        self.samplemethod = samplemethod
        self.ninvar = ninvar 
        self.seed = seed 
        self.nummap = nummap 
        
        self.isscalar = True
        self.size = (1, 1)
        
        self.genValMap()
        if autodraw:
            self.draw(ninvar_max=None)


    def mapNums(self) -> None:
        self.vals = copy(self.nums)
        if self.nummap is not None:
            for i in range(self.ncases):
                self.vals[i] = self.nummap[self.nums[i]]


    def genValMap(self) -> None:
        if self.nummap is None:
            self.valmap = None
        else:
            self.valmap = {val:num for num, val in self.nummap.items()}


    def setNDraws(self, 
                  ndraws : int,
                  ) -> None:
        self.ndraws = ndraws
        self.setFirstCaseMedian(self.firstcaseismedian)
        
        
    def draw(self, 
             ninvar_max : int = None,
             ) -> None:
        self.pcts = []
        self.nums = []
        dist = self.dist(**self.distkwargs)

        if self.firstcaseismedian:
            self.ncases = self.ndraws + 1
            self.pcts.append(0.5)
            self.nums.append(self.getMedian())
            
        pcts = mc_sampling(ndraws=self.ndraws, method=self.samplemethod, ninvar=self.ninvar, ninvar_max=ninvar_max, seed=self.seed)
        self.pcts.extend(pcts)
        self.nums.extend(dist.ppf(pcts).tolist())
        
        if any(np.isinf(num) for num in self.nums):
            warn(f'Infinite value drawn. Check distribution and parameters: {self.dist=}, {self.distkwargs=}')
            if self.samplemethod in (SampleMethod.SOBOL, SampleMethod.HALTON):
                warn(f"Infinite value draw may happen with {self.dist=} for the first point of the {self.samplemethod} sampling method. Consider using {SampleMethod.SOBOL_RANDOM} instead.")

        if any(np.isnan(num) for num in self.nums):
            raise ValueError(f'Invalid draw. Check distribution and parameters: {self.dist=}, {self.distkwargs=}')

        self.mapNums()


    def getVal(self,
               ncase : int,
               ) -> MCInVal:
        ismedian = False
        if (ncase == 0) and self.firstcaseismedian:
            ismedian = True

        val = MCInVal(name=self.name, ncase=ncase, pct=self.pcts[ncase], num=self.nums[ncase], dist=self.dist, nummap=self.nummap, ismedian=ismedian)
        return val


    def getMedian(self) -> float:
        dist = self.dist(**self.distkwargs)
        median = dist.ppf(0.5)
        return median


    def getMean(self) -> float:
        dist = self.dist(**self.distkwargs)
        ev = dist.expect()
        
        if isinstance(self.dist, rv_continuous):
            return ev

        # For a discrete distribution, we take the nearest discrete value closest to the expected value
        elif isinstance(self.dist, rv_discrete):
            eps = np.finfo(float).eps
            p = dist.cdf(ev)
            ev_candidates = dist.ppf([p - eps, p, p + eps])
            ev_candidates_dist = abs(ev_candidates - ev)
            ev_closest = ev_candidates[np.nanargmin(ev_candidates_dist)]
            return ev_closest
        
        else:
            return None



### MCOutVar Class ###
class MCOutVar(MCVar):
    def __init__(self, 
                 name              : str, 
                 vals              : list[Any], 
                 valmap            : dict = None, 
                 ndraws            : int  = None, 
                 firstcaseismedian : bool = False,
                 ):
        if ndraws is None:
            ndraws = len(vals)
            if firstcaseismedian:
                ndraws = ndraws - 1
        
        super().__init__(name=name, ndraws=ndraws, firstcaseismedian=firstcaseismedian)
        self.vals = vals
        self.valmap = valmap
        if valmap is None:
            self.extractValMap()
        self.genSize()
        self.genNumMap()
        self.mapVals()


    def genSize(self) -> None:
        if isinstance(self.vals[0],(list, tuple, np.ndarray)):
            self.isscalar = False
            if isinstance(self.vals[0][0],(list, tuple, np.ndarray)):
                self.size = (len(self.vals[0]), len(self.vals[0][0]))
            else:
                self.size = (1, len(self.vals[0]))
        else:
            self.isscalar = True
            self.size = (1, 1)
            
    
    def extractValMap(self) -> None:
        Val0 = self.getVal(0)
        if Val0.valmap is not None:
            if Val0.valmapsource == 'auto':
                uniquevals : set[Any] = set()
                for i in range(self.ncases):
                    uniquevals.update(self.getVal(i).valmap.keys())
                self.valmap = dict()
                for i, val in enumerate(sorted(uniquevals)):
                    self.valmap[val] = i
            else:
                self.valmap = Val0.valmap


    def genNumMap(self) -> None:
        if self.valmap is None:
            self.nummap = None
        else:
            self.nummap = {num:val for val, num in self.valmap.items()}


    def mapVals(self) -> None:
        self.nums = copy(self.vals)
        for i in range(self.ncases):
            self.nums[i] = self.getVal(i).num  


    def getVal(self, ncase : int) -> MCOutVal:
        ismedian = False
        if (ncase == 0) and self.firstcaseismedian:
            ismedian = True
            
        val = MCOutVal(name=self.name, ncase=ncase, val=self.vals[ncase], valmap=self.valmap, ismedian=ismedian)
        return val
        
    
    def getMedian(self) -> MCOutVal:
        val = None
        if self.firstcaseismedian:
            val = MCOutVal(name=self.name, ncase=0, val=self.vals[0], valmap=self.valmap, ismedian=True)
        return val
    
    
    def split(self) -> dict[str, 'MCOutVar']:
        mcvars = dict()
        if self.size[0] > 1:
            for i in range(self.size[0]):
                name = self.name + f' [{i}]'
                vals = []
                for j in range(self.ncases):
                    vals.append(self.vals[j][i])
                mcvars[name] = MCOutVar(name=name, vals=vals, ndraws=self.ndraws, \
                                        valmap=self.valmap, firstcaseismedian=self.firstcaseismedian)
                for mcvarstat in self.mcvarstats:
                    mcvars[name].addVarStat(stattype=mcvarstat.stattype, statkwargs=mcvarstat.statkwargs, name=mcvarstat.name)
        return mcvars
