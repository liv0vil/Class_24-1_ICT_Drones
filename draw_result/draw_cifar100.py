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
m['HSamp']='>'
m['SBias']='^'
m['TS']='*'
m['TAVAAL']='h'
m['UGCN']='p'
m['LL4AL']='d'
m['Core-set']='s'
m['Random']='v'

# #################
# CIFAR100
# #################

cifar100_ratios = list(range(1, 11))
cifar100_labels = [str(item+1) for item in range(10)]

cifar100_tavaal =np.array([12.93, 18.00, 22.80, 28.74, 34.89, 40.56, 44.59, 48.13, 51.25, 53.98])
cifar100_tavaal_error = np.array([0.73, 0.59, 0.75, 1.68, 0.97, 0.87, 0.81, 0.48, 0.45, 0.33])

cifar100_UGCN =np.array([12.93, 17.46, 23.44, 29.04, 33.72, 39.92, 43.83, 47.25, 50.09, 52.58])
cifar100_UGCN_error = np.array([0.52, 0.73, 0.80, 1.79, 1.91, 1.63, 1.00, 0.77, 0.60, 0.55])

cifar100_LL4AL = np.array([12.93, 17.52, 22.53, 28.41, 34.26, 40.09, 43.79, 47.95, 50.84, 53.55])
cifar100_LL4AL_error = np.array([0.73, 0.64, 0.83, 1.53, 1.81, 0.94, 0.91, 0.49, 0.59, 0.48])

cifar100_coreset = np.array([12.93, 18.02, 23.50, 28.78, 34.16, 40.94, 44.77, 48.12, 51.03, 53.69])
cifar100_coreset_error = np.array([0.52, 0.74, 0.88, 1.63, 1.23, 1.11, 0.57, 0.55, 0.36, 0.62])

cifar100_random = np.array([12.93, 18.86, 23.95, 29.19, 33.99, 40.60, 43.40, 46.60, 49.40, 52.01])
cifar100_random_error = np.array([0.52, 0.44, 0.89, 1.22, 0.94, 0.61, 0.79, 0.28, 0.35, 0.27])


plt.figure(figsize=(8, 6), dpi=500)
# fig, ax = plt.subplots(dpi=500)
plt_props()
plt.grid(color = 'lightgrey')
ax = plt.gca()
ax.set_facecolor('white')
ax.set_xticks(cifar100_ratios)
ax.set_xticklabels(cifar100_labels, fontproperties=fontprop_ticks)

ax.set_yticks([10, 20 ,30, 40, 50])
ax.set_yticklabels([10, 20 ,30, 40, 50], fontproperties=fontprop_ticks)

plt.ylim(10, 55)
plt.xlabel('Cycle', fontproperties=fontprop)
plt.ylabel('Accuracy (%)', fontproperties=fontprop)



######################################################################################
# Main Part
######################################################################################

cifar100_LL4AL_plot = plt.errorbar(cifar100_ratios, cifar100_LL4AL, label='LL4AL',marker=m['LL4AL'], color='#4C71B0', ms=6)
plt.fill_between(cifar100_ratios, cifar100_LL4AL - cifar100_LL4AL_error, cifar100_LL4AL + cifar100_LL4AL_error, alpha = 0.35, color='#4C71B0', edgecolor="None")

cifar100_tavaal_plot = plt.errorbar(cifar100_ratios, cifar100_tavaal, label='TAVAAL', marker=m['TAVAAL'], color='#93785F', ms=6)
plt.fill_between(cifar100_ratios, cifar100_tavaal - cifar100_tavaal_error, cifar100_tavaal + cifar100_tavaal_error, alpha = 0.35, color='#93785F', edgecolor="None")

cifar100_coreset_plot = plt.errorbar(cifar100_ratios, cifar100_coreset, label='Core-set', marker=m['Core-set'], color='#e8b74a', ms=6)
plt.fill_between(cifar100_ratios, cifar100_coreset - cifar100_coreset_error, cifar100_coreset + cifar100_coreset_error, alpha = 0.35, color='#e8b74a', edgecolor="None")

cifar100_UGCN_plot = plt.errorbar(cifar100_ratios, cifar100_UGCN, label='UGCN', marker=m['UGCN'],color='#54A868', ms=6)
plt.fill_between(cifar100_ratios, cifar100_UGCN - cifar100_UGCN_error, cifar100_UGCN + cifar100_UGCN_error, alpha = 0.35, color='#54A868', edgecolor="None")

cifar100_random_plot = plt.errorbar(cifar100_ratios, cifar100_random, label='Random', marker=m['Random'], color='#C04D50', ms=6)
plt.fill_between(cifar100_ratios, cifar100_random - cifar100_random_error, cifar100_random + cifar100_random_error, alpha = 0.35, color='#C04D50', edgecolor="None")

plt.legend(ncol=3, loc='lower right', prop=fontprop_legend)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))

plt.tight_layout()
save_dir = './figures'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
plt.savefig(os.path.join(save_dir, 'CIFAR100(benchmarks).png'))
