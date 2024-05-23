import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

from matplotlib.axes import Axes
import numpy as np
# from IPython.display import Image, display
from PIL import Image
from subprocess import call
from collections import OrderedDict
import matplotlib.ticker as mticker
from matplotlib.ticker import FormatStrFormatter

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import matplotlib.ticker as ticker
import matplotlib.patches as patches

import matplotlib.font_manager as fm
path = 'fonts/times.ttf'
fontprop = fm.FontProperties(fname=path, size=22)
fontprop_ticks = fm.FontProperties(fname=path, size=20)
fontprop_legend = fm.FontProperties(fname=path, size=16)

sns.set()
sns.set_style("dark")

def plt_props():
    plt.rcParams['font.size'] = 20
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.style'] = 'normal'
    plt.rcParams['font.variant'] = 'normal' 
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    plt.rcParams['legend.fontsize'] = 14
    plt.rcParams['figure.titlesize'] = 20
    # plt.rcParams['figure.figsize'] = 6, 4
    # plt.rcParams['figure.figsize'] = (1,5)
    # plt.rcParams['lines.linewidth'] = 2.5
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 8
    plt.rcParams['axes.facecolor']='lightgrey'
    # plt.rcParams['savefig.facecolor']='lightgrey'
    


m={}
m['OO4AL']='o'
m['HSamp']='>'
m['SBias']='^'
m['TS']='*'
m['TAVAAL']='h'
m['UGCN']='p'
m['LL4AL']='d'
m['Core-set']='s'
m['Random']='v'

# ######################################################################################
# # cifar 10
# ######################################################################################
cifar10_ratios = list(range(1, 11))
cifar10_labels = [str(item+1) for item in range(10)]

cifar10_tavaal =np.array([45.15, 58.69, 70.74, 79.77, 82.95, 85.76, 87.33, 88.30, 89.20, 89.13])
cifar10_tavaal_error = np.array([1.19, 0.48, 1.36, 0.58, 0.43, 0.48, 0.34, 0.39, 0.11, 0.18])

cifar10_UGCN =np.array([46.20, 57.27, 66.38, 73.44, 80.17, 83.75, 85.88, 87.07, 88.14, 88.99])
cifar10_UGCN_error = np.array([2.52, 2.26, 2.29, 2.88, 1.00, 0.60, 0.58, 0.58, 0.50, 0.65])

cifar10_LL4AL = np.array([45.15, 58.68, 70.74, 79.71, 82.92, 86.17, 87.77, 88.62, 89.39, 89.86])
cifar10_LL4AL_error = np.array([1.19, 0.70, 0.92, 0.72, 0.28, 0.25, 0.34, 0.14, 0.27, 0.22])

cifar10_coreset = np.array([46.20, 57.22, 66.32, 73.24, 79.70, 83.80, 85.81, 87.36, 88.46, 89.22])
cifar10_coreset_error = np.array([2.52, 2.31, 2.89, 2.77, 1.43, 0.71, 0.47, 0.28, 0.48, 0.18])

cifar10_random = np.array([46.20, 56.81, 65.17, 72.12, 78.11, 82.03, 84.16, 85.42, 86.43, 86.89])
cifar10_random_error = np.array([2.52, 2.74, 2.81, 2.25, 1.38, 0.59, 0.57, 0.31, 0.20, 0.32])

plt.figure(figsize=(8, 6), dpi=500)
# fig, ax = plt.subplots(dpi=500)
plt_props()
plt.grid(color = 'lightgrey')
ax = plt.gca()
ax.set_facecolor('white')
ax.set_xticks(cifar10_ratios)
ax.set_xticklabels(cifar10_labels, fontproperties=fontprop_ticks)

ax.set_yticks([40, 50, 60, 70, 80, 90])
ax.set_yticklabels([40, 50, 60, 70, 80, 90], fontproperties=fontprop_ticks)

plt.ylim(35, 95)
plt.xlabel('Cycle', fontproperties=fontprop)
plt.ylabel('Accuracy (%)', fontproperties=fontprop)
# plt.title('CIFAR10', fontsize=20)


##################
# VAAL VERSION
##################

cifar10_LL4AL_plot = plt.errorbar(cifar10_ratios, cifar10_LL4AL, label='LL4AL',marker=m['LL4AL'], color='#4C71B0', ms=6)
plt.fill_between(cifar10_ratios, cifar10_LL4AL - cifar10_LL4AL_error, cifar10_LL4AL + cifar10_LL4AL_error, alpha = 0.35, color='#4C71B0', edgecolor="None")

cifar10_tavaal_plot = plt.errorbar(cifar10_ratios, cifar10_tavaal, label='TAVAAL', marker=m['TAVAAL'], color='#93785F', ms=6)
plt.fill_between(cifar10_ratios, cifar10_tavaal - cifar10_tavaal_error, cifar10_tavaal + cifar10_tavaal_error, alpha = 0.35, color='#93785F', edgecolor="None")

cifar10_coreset_plot = plt.errorbar(cifar10_ratios, cifar10_coreset, label='Core-set', marker=m['Core-set'], color='#e8b74a', ms=6)
plt.fill_between(cifar10_ratios, cifar10_coreset - cifar10_coreset_error, cifar10_coreset + cifar10_coreset_error, alpha = 0.35, color='#e8b74a', edgecolor="None")

cifar10_UGCN_plot = plt.errorbar(cifar10_ratios, cifar10_UGCN, label='UGCN', marker=m['UGCN'],color='#54A868', ms=6)
plt.fill_between(cifar10_ratios, cifar10_UGCN - cifar10_UGCN_error, cifar10_UGCN + cifar10_UGCN_error, alpha = 0.35, color='#54A868', edgecolor="None")

cifar10_random_plot = plt.errorbar(cifar10_ratios, cifar10_random, label='Random', marker=m['Random'], color='#C04D50', ms=6)
plt.fill_between(cifar10_ratios, cifar10_random - cifar10_random_error, cifar10_random + cifar10_random_error, alpha = 0.35, color='#C04D50', edgecolor="None")

plt.legend(ncol=3, loc='lower right', 
           prop=fontprop_legend)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))


plt.tight_layout()
save_dir = './figures'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
plt.savefig(os.path.join(save_dir, 'CIFAR10(benchmarks).png'))
