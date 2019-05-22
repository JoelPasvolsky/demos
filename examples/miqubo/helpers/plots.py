#    Copyright 2018 D-Wave Systems Inc.

#    Licensed under the Apache License, Version 2.0 (the "License")
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http: // www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

def subplot_xx_y(df):
    xnum = df.shape[1]-1
    gs = GridSpec(2, xnum)
    plt.figure(figsize=(10, 10))
    for i in range(xnum):
        ax = 'ax_' + df.columns[i]
        ax = plt.subplot(gs[0, i])
        ax.set_title(df.columns[i])
        ax.plot(np.linspace(-np.pi, np.pi, 100), df[df.columns[i]].values)
    axy = plt.subplot(gs[1, :])
    axy.set_title(df.columns[-1])
    axy.plot(np.linspace(-np.pi, np.pi, 100), df[df.columns[-1]].values, 'r')

def plot_vars_out(data, vars1, vars2, y, model):
    ax1 = plt.subplot(1, 2, 1)
    ax1.set_title("Modeling %s" % vars1[:2])
    ax1.plot(np.linspace(-np.pi, np.pi, 100), y, 'ro')
    ax1.plot(np.linspace(-np.pi, np.pi, 100), model((data[vars1[0]].values, data[vars1[1]].values), *vars1[2]), 'bv')
    ax1.legend(["out", "model"])
    ax2 = plt.subplot(1, 2, 2)
    ax2.set_title("Modeling %s" % vars2[:2])
    ax2.plot(np.linspace(-np.pi, np.pi, 100), y, 'ro')
    ax2.plot(np.linspace(-np.pi, np.pi, 100), model((data[vars2[0]].values, data[vars2[1]].values), *vars2[2]), 'bv')
    ax1.legend(["out", "model"])
