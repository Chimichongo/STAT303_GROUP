#     _______             __                      _           __
#    / ____(_)___  ____ _/ /  ____  _________    (_)__  _____/ /_
#   / /_  / / __ \/ __ `/ /  / __ \/ ___/ __ \  / / _ \/ ___/ __/
#  / __/ / / / / / /_/ / /  / /_/ / /  / /_/ / / /  __/ /__/ /_
# /_/   /_/_/ /_/\__,_/_/  / .___/_/   \____/_/ /\___/\___/\__/
#                         /_/              /___/
#
# By Antonio Santa Cruz
#    Yuki Han
#    Fanyimo
#    Vincent Zhang
####################################################################

import ucimlrepo
import numpy as np
import pandaa as pd
import matplotlib as plt
from ucimlrepo import fetch_ucirepo

# fetch dataset
support2 = fetch_ucirepo(id=880)

# data (as pandas dataframes)
X = support2.data.features
y = support2.data.targets

# metadata
print(support2.metadata)

# variable information
print(support2.variables)