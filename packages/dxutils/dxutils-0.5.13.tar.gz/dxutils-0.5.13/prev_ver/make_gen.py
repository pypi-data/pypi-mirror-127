#!/usr/bin/env python3

import sys
import ase.io
from ase.units import Bohr
import spglib
import click
from collections import OrderedDict

@click.command()
@click.argument('action', default='gen')
@click.option('-o', '--order', default=1, help='Approximation order (1)')
@click.option('-p', '--prefix', default='CRYST', help='Prefix used in calculations (CRYST)')
@click.option('-n', '--name', default='SPOSCAR', type=click.Path(exists=True), help='Supercell POSCAR file (SPOSCAR)')
@click.option('-s', '--scale', default=1.0, help='Scale of the unit cell (1.0)')
@click.option('-e', '--evec', default=1, help='Print eigenvectors (1)')
@click.option('-m', '--msd', default=1, help='Print mean squere displacement (1)')
@click.option('-t', '--tmax', default=1000, help='Max temperature (1000)')
@click.option('-b', '--born', default='', help='Use info from <prefix>.born as Born effective charges')
def gen(name, order, prefix, scale, action, evec, msd, tmax, born):
    """Generates input files for alm. 
       Possible actions: gen (default), phon, dos
    """

    tmpl={'gen':
'''
&general
  PREFIX = {prefix}
  MODE = suggest
  NAT = {nat}
  NKD = {nkd}
  KD = {kd}
/

&interaction
  NORDER = {order}  # 1: harmonic, 2: cubic, ..
/

&cell
  {scale:14.10f} # factor 
  {cell} # cell matrix
/

&cutoff 
  {cutoff}
/

&position
  {positions}
/
''',
          'phon':
'''
&general
  PREFIX = {prefix}
  MODE = phonons ;   
  FCSXML = {prefix}.xml 
  NKD = {nkd}
  KD = {kd}
  MASS = {mass}
  TMAX = {tmax}
  EMIN = 0; EMAX = 1000; DELTA_E = 2
  {born}
/


&cell
  {scale:14.10f} # factor 
  {cell} # cell matrix
/


&analysis
  PRINTMSD = {msd}
  PRINTEVEC = {evec}
/

'''}


    cr = ase.io.read(name)
    
    cell = cr.get_cell()
    if action in ['phon','dos']:
        cell=spglib.find_primitive(cr)[0]    
        action='phon'

    cell = '\n  '.join([' '.join(['%14.10f' % c for c in v]) for v in cell])
    
    nat = len(cr.get_atomic_numbers())
    nkd = len(set(cr.get_atomic_numbers()))
    kd = ' '.join(list(OrderedDict.fromkeys(cr.get_chemical_symbols())))
    scl = scale/Bohr # in A -> bohr
    elems = {e:n+1 for n, e in enumerate(kd.split())}
    masses = {e:m for e,m in zip(cr.get_chemical_symbols(), cr.get_masses())}
    
    positions='\n  '.join(['{:d} {:14.10f} {:14.10f} {:14.10f}'.format(elems[e], p[0], p[1], p[2])
        for e, p in zip(cr.get_chemical_symbols(),cr.get_scaled_positions())])
    
    elm=kd.split()
    cutoff='\n  '.join(['{}-{} {}'.format(a,b, order * ' None') 
                        for k,a in enumerate(elm) for l,b in enumerate(elm) if k<=l])
    
    mass = ' '.join(['{:14.10f}'.format(masses[e]) for e in kd.split()])
    
    if born :
        born = 'BORNINFO = {prefix}.born \n  NONANALYTIC = {born} \n'.format(prefix=prefix, born=born)
    else :
        born = ''

    print(tmpl[action].format(prefix=prefix, nat=nat, nkd=nkd, kd=kd, order=order, 
                              evec=evec, msd=msd, scale=scl, cell=cell, cutoff=cutoff, 
                              positions=positions, mass=mass, tmax=tmax, born=born))

if __name__ == '__main__':
    gen()
