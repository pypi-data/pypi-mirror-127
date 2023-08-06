#!/usr/bin/env python
#
# plotdos.py
#
# Simple script to visualize phonon DOS
#
# Copyright (c) 2014 Terumasa Tadano
#
# This file is distributed under the terms of the MIT license.
# Please see the file 'LICENCE.txt' in the root directory
# or http://opensource.org/licenses/mit-license.php for information.
#

from __future__ import print_function, division
import numpy as np
import optparse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# parser options
usage = "usage: %prog [options] file1.dos file2.dos ... "
parser = optparse.OptionParser(usage=usage)

parser.add_option("--pdos", action="store_true", dest="print_pdos", default=False,
                  help="print atom-projected phonon DOS")
parser.add_option("--nokey", action="store_false", dest="print_key", default=True,
                  help="don't print the key in the figure")
parser.add_option("-u", "--unit", action="store", type="string", dest="unitname", default="kayser",
                  help="print the band dispersion in units of UNIT. Available options are kayser, meV, and THz", metavar="UNIT")
parser.add_option("--emin", action="store", type="float", dest="emin",
                  help="minimum value of the energy axis")
parser.add_option("--emax", action="store", type="float", dest="emax",
                  help="maximum value of the energy axis")


# font styles
mpl.rc('font', **{'family': 'Times New Roman', 'sans-serif': ['Helvetica']})

# line colors and styles
color = ['k', 'b', 'g', 'r', 'm', 'c', 'y', 'r',
         'darkred', 'darkblue', 'darkgreen', 'darkmagenta']
lsty = ['-', '-', '-', '-', '--', '--', '--', '--', '-', '-', '-', '-']


def get_natoms_and_symbols(file_in):

    ftmp = open(file_in, 'r')
    str_symbols = ftmp.readline().rstrip('\n').split()
    str_natoms = ftmp.readline().rstrip('\n').split()
    ftmp.close()

    if str_symbols[0] == '#' and str_natoms[0] == '#':
        symbols = str_symbols[1:]
        natoms = [int(x) for x in str_natoms[1:]]

        return symbols, natoms
    else:
        return [], []


def get_xy_minmax(xarray, yarray):

    ymin, ymax = (0, 0)
    eps = 1e-3
    
    xa = np.array(xarray)
    ya = np.array(yarray)
    
    ymax = max(ymax, ya.max())
    
    xmin = xa[  (abs(ya) > eps*ymax).any(axis=-1) ].min()
    xmax = xa[  (abs(ya) > eps*ymax).any(axis=-1) ].max()
    
    return xmin, xmax*1.1, ymin, ymax


def change_xscale(array, str_scale):

    str_tmp = str_scale.lower()

    if str_tmp == 'kayser':
        print("Phonon DOS will be shown in units of cm^{-1}")
        return array

    elif str_tmp == 'mev':
        print("Phonon DOS will be shown in units of meV")
        kayser_to_mev = 0.0299792458 * 1.0e+12 * \
            6.62606896e-34 / 1.602176565e-19 * 1000

        for i in range(len(array)):
            array[i] *= kayser_to_mev

        return array

    elif str_tmp == 'thz':
        print("Phonon DOS will be shown in units of THz")
        kayser_to_thz = 0.0299792458

        for i in range(len(array)):
            array[i] *= kayser_to_thz

        return array

    else:
        print("Unrecognizable option for --unit %s" % str_scale)
        print("Phonon DOS will be shown in units of cm^{-1}")
        return array


def sum_atom_projected_dos(pdos_tmp, natoms_tmp):

    nenergy, natom = np.shape(pdos_tmp)
    nkinds = len(natoms_tmp)

    pdos_sum = np.zeros((nenergy, nkinds))

    counter = 0

    for i in range(nkinds):
        for j in range(natoms_tmp[i]):

            for k in range(nenergy):
                pdos_sum[k][i] += pdos_tmp[k][counter]

            counter += 1

    return pdos_sum


def main():
    options, args = parser.parse_args()
    files = args[0:]
    nfiles = len(files)

    if nfiles == 0:
        print("Usage: plotdos.py [options] file1.dos file2.dos ...")
        print("For details of available options, please type\n$ python plotdos.py -h")
        exit(1)
    else:
        print("Number of files = %d" % nfiles)

    energy_axis = []
    dos_merged = []

    for file in files:
        data_tmp = np.loadtxt(file, dtype=float)
        energy_axis.append(data_tmp[:, 0])
        dos_merged.append(data_tmp[:, 1:])

    energy_axis = change_xscale(energy_axis, options.unitname)
    xmin, xmax, ymin, ymax = get_xy_minmax(energy_axis, dos_merged)

    counter_line = 0

    for i in range(len(dos_merged)):
        counter_line = counter_line % 12

        plt.plot(energy_axis[i][:], dos_merged[i][:, 0],
                 linestyle=lsty[counter_line], color=color[counter_line],
                 label=files[i] + ":Total")

        counter_line += 1

        if options.print_pdos:
            symbols, natoms = get_natoms_and_symbols(files[i])

            if len(dos_merged[i][0, 1:]) != np.sum(natoms):
                print("Error: Projected DOS is not contained in the %d-th file" % (i + 1))
                exit(1)
            else:
                pdos = sum_atom_projected_dos(dos_merged[i][:, 1:], natoms)

                for j in range(len(pdos[0, :])):

                    plt.plot(energy_axis[i][:], pdos[:, j], linestyle=lsty[counter_line],
                             color=color[counter_line],
                             label=files[i] + ":" + symbols[j])

                    counter_line += 1

    if options.unitname.lower() == "mev":
        plt.xlabel("Frequency (meV)", fontsize=16, labelpad=20)
    elif options.unitname.lower() == "thz":
        plt.xlabel("Frequency (THz)", fontsize=16, labelpad=20)
    else:
        plt.xlabel("Frequency (cm${}^{-1}$)", fontsize=16, labelpad=10)

    plt.ylabel("Phonon DOS", fontsize=16, labelpad=20)

    if options.emin == None and options.emax == None:
        factor = 1.00
        xmin *= factor
        xmax *= factor
    else:
        if options.emin != None:
            xmin = options.emin
        if options.emax != None:
            xmax = options.emax

        if xmin > xmax:
            print("Warning: emin > emax")

    ymax *= 1.05
    plt.axis([xmin, xmax, ymin, ymax])

    plt.xticks(fontsize=16)
    plt.yticks([])

    if options.print_key:
        plt.legend(loc='upper right', prop={'size': 12})

    plt.savefig('dos_tmp.pdf', dpi=300, transparent=False)

if __name__ == '__main__':
    main()
