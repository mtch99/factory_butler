import math

from requests import head
from amplpy import AMPL, Environment, add_to_path, DataFrame as ampl_df
import pandas as pd
import numpy as np

# configure ampl instance
ampl_env = Environment('/Users/maximetchagou/Downloads/ampl_macos64')
ampl = AMPL(ampl_env)           
ampl.setOption('solver', 'gurobi')
ampl.setOption('gurobi_options', 'lim:time=2')