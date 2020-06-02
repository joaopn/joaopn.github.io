#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:40:36 2020

@author: joaopn
"""

import numpy as np
import matplotlib.pyplot as plt


# Simple model

plt.figure(figsize=(5, 3))
R_vec = np.linspace(0, 1)

P = lambda CFR, K: 1-np.power(1 - CFR * R_vec, K)

plt.plot(100 * R_vec, 100 * P(0.0138, 150), label='K = 150', lw=3)
plt.plot(100 * R_vec, 100 * P(0.0138, 1000), label='K = 1000', lw=3)
plt.xlabel('Fraction R of infected (in %)')
plt.ylabel('Probability P of deaths (in %)')
plt.legend(loc='lower right', frameon=False)
plt.xlim([0, 100])
plt.ylim([0, 105])
plt.xticks([0, 25, 50, 75, 100])
plt.yticks([0, 25, 50, 75, 100])
plt.tight_layout()
plt.savefig('P_simple.png', dpi=200)

# R needed for P = 0.5
CFR_vec = np.linspace(0.001, 0.1, 1000)
R_50 = lambda P,K: (1-np.power(1-P, 1/K))/CFR_vec

plt.figure(figsize=(5, 3))
plt.plot(100 * CFR_vec, 100 * R_50(0.5, 150), label='K=150', lw=3)
plt.plot(100 * CFR_vec, 100 * R_50(0.5, 1000), label='K=1000', lw=3)
plt.ylim([0, 100])
plt.xlabel('Disease CFR (in %)')
plt.ylabel(r'R needed for P = 0.5 (in %)')
plt.xlim([0, 10])
#plt.yticks([0, 25, 50, 75, 100])
plt.legend(frameon=False)
plt.yscale('log')
plt.ylim([0.5, 100])
plt.tight_layout()
plt.savefig('CFR_dependence.png', dpi=200)

# Age_group model
R_vec = np.linspace(0, 1)
CFR_CH = [0,0.2,0.2,0.2,0.4,1.3,3.6,8.0,14.8]

age_group_BR = [0.138300149359734, 0.149884610729674, 0.161959146658846, 0.163166370447876, 0.136948509226406, 0.113843462490905, 0.077196029999007, 0.039806250399462, 0.01889547068809]

age_group_US = [0.121227888295366, 0.128844093702034, 0.140334209495812, 0.133651649653068, 0.122433106413468, 0.129329149968302, 0.115008000077991, 0.069923084507973, 0.039248817885986]

age_group_IT = [0.084286841380852, 0.094803026888877, 0.101324800629535, 0.117270556748287, 0.152355920450129, 0.156121447346438, 0.122066305035507, 0.098018810607257, 0.073752290913117]

CFR_BR = np.dot(CFR_CH, age_group_BR)
CFR_US = np.dot(CFR_CH, age_group_US)
CFR_IT = np.dot(CFR_CH, age_group_IT)

label_BR = 'Brazil (CFR = {:0.2f}%)'.format(CFR_BR)
label_US = 'United States (CFR = {:0.2f}%)'.format(CFR_US)
label_IT = 'Italy (CFR = {:0.2f}%)'.format(CFR_IT)

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.plot(100 * R_vec, 100 * P(CFR_BR/100, 150), label=label_BR, lw=3)
ax.plot(100 * R_vec, 100 * P(CFR_US/100, 150), label=label_US, lw=3)
ax.plot(100 * R_vec, 100 * P(CFR_IT/100, 150), label=label_IT, lw=3)

ax.set_xlabel('Fraction R of infected (in %)')
ax.set_ylabel('Probability P of deaths (in %)')
ax.legend(loc='lower right', frameon=False)
ax.set_title('K = 150')
ax.set_xlim([0, 100])
ax.set_ylim([0, 105])
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_yticks([0, 25, 50, 75, 100])
#ax.set_tight_layout()
#ax.set_savefig('P_countries_K150.png', dpi=200)

ax2.plot(100 * R_vec, 100 * P(CFR_BR/100, 1000), label=label_BR, lw=3)
ax2.plot(100 * R_vec, 100 * P(CFR_US/100, 1000), label=label_US, lw=3)
ax2.plot(100 * R_vec, 100 * P(CFR_IT/100, 1000), label=label_IT, lw=3)

ax2.set_xlabel('Fraction R of infected (in %)')
ax2.set_ylabel('Probability P of deaths (in %)')
ax2.legend(loc='lower right', frameon=False)
ax2.set_title('K = 1000')
ax2.set_xlim([0, 100])
ax2.set_ylim([0, 105])
ax2.set_xticks([0, 25, 50, 75, 100])
ax2.set_yticks([0, 25, 50, 75, 100])
# ax2.set_tight_layout()
# ax2.set_savefig('P_countries_K1000.png', dpi=200)
fig.tight_layout()
fig.savefig('P_countries', dpi=200)