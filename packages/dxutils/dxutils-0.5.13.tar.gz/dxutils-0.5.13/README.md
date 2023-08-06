# Title



dxutils -- Utils for DepX
================

This is a set of utilities which started as tools for internal use of our department.
At that time it was Department X (10) - of computational materials science.
The current name is different but the package name stucked. It turns out that the tools
may be os some use for other researchers and can be used in other programs.
They are centered around solid state computational physics.

Installation
---------------
You can install the package from pypi. It has several dependencies and requires python 3.5 or later.

To install from pypi (better use some virtual environment using e.g.: `python3 -m venv venv && . venv/bin/activate`):

```
pip install dxutils 
```

Usage
------

The package provides a number of utility functions organized in the library you can use in your python programs and a command line program `gen_alamode` for generating ALAMODE input files from the DFT structural data. The default format is VASP 5+ POSCAR file but you can use any format which is known to the ASE library used for reading and transforming the data. Get help on `gen_alamode`:

```
$ gen_alamode --help
Usage: gen_alamode [OPTIONS] [ACTION]

  Generates gen/opt/phon/dos file depending on the ACTION (default: opt). The
  default values of parameters are enclosed in parethesis.

Options:
  -o, --order INTEGER  Approximation order (1)
  -p, --prefix TEXT    Prefix used in calculations (CRYST)
  -n, --name PATH      Supercell POSCAR file (SPOSCAR)
  -s, --scale FLOAT    Scale of the unit cell (1.0)
  -e, --evec INTEGER   Print eigenvectors (1)
  -m, --msd INTEGER    Print mean squere displacement (1)
  --c1 TEXT            First order interaction cutoff (None)
  --c2 TEXT            Second order interaction cutoff (10)
  --c3 TEXT            Third order interaction cutoff (10)
  -k, --kpath PATH     File with reciprocal space path
  -g, --grid TEXT      k-grid for dos calculation (10x10x10)
  -d, --ndat INTEGER   Number of data points used in fitting (All)
  -f, --dfset TEXT     Name of the DFSET file (DFSET)
  -t, --tmax INTEGER   Max temperature (1000)
  -c, --charge TEXT    Name of the Born effective charges file (<prefix>.born)
  -b, --born INTEGER   If non-zero use info from <prefix>.born as Born
                       effective charges. Use <born> = [1,2,3] value to select
                       method of non-analytic correction.
  --help               Show this message and exit.
```

