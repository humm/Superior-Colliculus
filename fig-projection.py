# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright INRIA
# Contributors: Wahiba Taouali (Wahiba.Taouali@inria.fr)
#               Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
#
# This software is governed by the CeCILL license under French law and abiding
# by the rules of distribution of free software. You can use, modify and/ or
# redistribute the software under the terms of the CeCILL license as circulated
# by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info/index.en.html.
#
# As a counterpart to the access to the source code and rights to copy, modify
# and redistribute granted by the license, users are provided only with a
# limited warranty and the software's author, the holder of the economic
# rights, and the successive licensors have only limited liability.
#
# In this respect, the user's attention is drawn to the risks associated with
# loading, using, modifying and/or developing or reproducing the software by
# the user in light of its specific status of free software, that may mean that
# it is complicated to manipulate, and that also therefore means that it is
# reserved for developers and experienced professionals having in-depth
# computer knowledge. Users are therefore encouraged to load and test the
# software's suitability as regards their requirements in conditions enabling
# the security of their systems and/or data to be ensured and, more generally,
# to use and operate it in the same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
# -----------------------------------------------------------------------------
import os
import numpy as np

from helper import *
from stimulus import *
from graphics import *
from projections import *


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(16,6), facecolor='w')

    # Stimuli luminances are not additive
    R = stimulus(position=(5,0))
    P = retina_projection(retina_shape, [1024,1024])


    # ---------------------------------
    ax = plt.subplot(2,1,1)
    ax.tick_params(direction="outward")
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',-0.05))


    X  = np.linspace(0,90,R.shape[1])
    for rho in [2,5,10,20,40,60,80]:
        R = stimulus(position=(rho,0))
        ax.plot(X, R[R.shape[0]//2], color='blue')

    xticks, labels = [], []
    for rho in [0,2,5,10,20,40,60,80,90]:
        xticks.append(rho)
        labels.append(u"%d°" % rho)
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    ax.set_yticks([])
    ax.set_ylim(0,4)
    ax.text(0, 1.9, u"Stimuli on retina (slice $\\theta$=0°)",
            ha="left", va="top", fontsize=14)

    # # ---------------------------------
    ax = plt.subplot(2,1,2)
    ax.tick_params(direction="outward")
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',-0.05))

    for rho in [2,5,10,20,40,60,80]:
        R = stimulus(position=(rho,0))
        SC = R[P[...,0], P[...,1]]
        X = np.linspace(0,90,SC.shape[1])
        ax.plot(X, SC[SC.shape[1]//2], color="b")

    xticks, labels = [], []
    for rho in [0,2,5,10,20,40,60,80,90]:
        x,y = polar_to_logpolar(rho/90.,0)
        xticks.append(90*x)
        labels.append(u"%d°" % rho)
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    ax.set_yticks([])
    ax.set_ylim(0,4)
    ax.text(0, 1.9, u"Projection of stimuli on superior colliculus axis (slice $\\theta$=0°)",
            ha="left", va="top", fontsize=14)

    plt.savefig("figures/fig-projection.pdf")
#    plt.savefig("fig-projection.svg")
    plt.show()
