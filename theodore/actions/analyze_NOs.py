"""
Driver script for analyzing a set of NO files.
"""

from __future__ import print_function, division
import sys

from .actions import Action
from .. import theo_header, lib_sden, input_options

class AnalyzeNOs(Action):

    name = 'analyze_nos'

    _colt_description = 'Analysis of natural orbital (NO) files'

    _questions = """
    # List of NO files in Molden format
    no_files = :: list(existing_file)
    # Main input file
    ifile = dens_ana.in :: existing_file, alias=f
    """

    def run(no_files, ifile):
        theo_header.print_header(__class__._colt_description, cfile=__file__)
        # set options
        ioptions = input_options.sden_ana_options(ifile, check_init=False)
        ioptions['rtype'] = 'nos'
        ioptions['mo_file'] = no_files[0]
        ioptions['ana_files'] = no_files[1:]

        #--------------------------------------------------------------------------#        
        # Parsing and computations
        #--------------------------------------------------------------------------#

        sdena = lib_sden.sden_ana(ioptions)
        sdena.read_mos()
        sdena.read_dens()

        if ioptions['AD_ana']:
            sdena.compute_all_AD()
        if ioptions['pop_ana']:
            sdena.print_all_pop_table()
        if ioptions['BO_ana']:
            sdena.compute_all_BO()
            sdena.print_all_BO()

        sdena.print_summary()