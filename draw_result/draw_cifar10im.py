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

# ######################################################################################
# # cifar 10 - im
# ######################################################################################
cifar10_ratios = list(range(1, 11))
cifar10_labels = [str(item+1) for item in range(10)]

cifar10_tavaal = np.array([19.33, 23.59, 25.61, 27.48, 28.93, 30.23, 31.47, 33.02, 34.85, 36.65])
cifar10_tavaal_error = np.array([1.21, 0.69, 1.34, 1.18, 1.32, 1.50, 1.65, 1.84, 2.20, 2.10])

cifar10_UGCN = np.array([19.08, 23.32, 25.14, 26.84, 27.67, 29.05, 30.19, 31.46, 34.48, 36.24])
cifar10_UGCN_error = np.array([1.17, 1.32, 1.71, 1.90, 1.42, 0.97, 1.07, 0.91, 0.97, 1.16])

cifar10_LL4AL = np.array([19.33, 23.14, 24.68, 26.39, 28.03, 29.51, 30.58, 32.00, 33.55, 36.17])
cifar10_LL4AL_error = np.array([1.21, 0.98, 1.22, 1.41, 1.23, 1.63, 1.44, 1.71, 3.21, 2.59])

cifar10_coreset = np.array([19.08, 23.24, 25.06, 26.86, 27.85, 29.24, 30.94, 32.29, 35.21, 36.01])
cifar10_coreset_error = np.array([1.17, 0.79, 1.03, 1.00, 0.53, 0.78, 0.63, 1.24, 1.96, 1.69])

cifar10_random = np.array([19.08, 22.92, 25.11, 26.39, 27.59, 28.72, 30.02, 31.23, 33.56, 34.67])
cifar10_random_error = np.array([1.17, 1.30, 1.51, 0.94, 0.68, 1.06, 1.10, 1.05, 1.27, 1.08])

plt.figure(figsize=(8,6), dpi=500)
# fig, ax = plt.subplots(dpi=500)
plt_props()
plt.grid(color = 'lightgrey')
ax = plt.gca()
ax.set_facecolor('white')
ax.set_xticks(cifar10_ratios)
ax.set_xticklabels(cifar10_labels, fontproperties=fontprop_ticks)

ax.set_yticks([20, 25, 30, 35])
ax.set_yticklabels([20, 25, 30, 35], fontproperties=fontprop_ticks)

plt.ylim(16, 39)
plt.xlabel('Cycle', fontproperties=fontprop)
plt.ylabel('Accuracy (%)', fontproperties=fontprop)


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

plt.legend(ncol=3, loc='lower right', prop=fontprop_legend)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))


plt.tight_layout()
save_dir = './figures'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
plt.savefig(os.path.join(save_dir, 'CIFAR10im(benchmarks).png'))
