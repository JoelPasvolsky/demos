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

def subplot_x_1(x, y):
    gs = GridSpec(2, 3)
    plt.figure(figsize=(10, 10))
    for i in range(len(x)):
        xi = x[i]
        ax = 'ax' + str(xi)
        ax = plt.subplot(gs[0, i])
        ax.set_title("Input "+str(i))
        ax.plot(np.linspace(-np.pi, np.pi, 100), xi)
    axy = plt.subplot(gs[1, :])
    axy.set_title("Output")
    axy.plot(np.linspace(-np.pi, np.pi, 100), y, 'r')

def plot_12_13(x, y, model, popt_12, popt_13):
    ax1 = plt.subplot(1, 2, 1)
    ax1.set_title("f(in1, in2)")
    ax1.plot(np.linspace(-np.pi, np.pi, 100), y, 'r')
    ax1.plot(np.linspace(-np.pi, np.pi, 100), model((x[0], x[1]), *popt_12), 'b.')
    ax2 = plt.subplot(1, 2, 2)
    ax2.set_title("f(in1, in3)")
    ax2.plot(np.linspace(-np.pi, np.pi, 100), y, 'r')
    ax2.plot(np.linspace(-np.pi, np.pi, 100), model((x[0], x[2]), *popt_13), 'b.')
