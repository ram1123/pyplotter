#!/usr/bin/env python
import ROOT
import CMS_lumi, tdrstyle
import argparse
import plot_functions as plotter

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(0)

def main():
    plot_info = getPlotArgs()
    print plot_info
    print "\n======= Start Makeing plots =================\n"
    
    print "\n========= plot FT0  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "ft0_m")
    print key
    print val
    print val[-14:]
    plotter.aQGC_plotting (plot_info, key[-1:], val[-1:],"FT0_",1)

    """
    key,val = plotter.getaQGC_parameters(plot_info, "ft0_m")
    print key
    print val
    print val[-14:]
    plotter.aQGC_plotting (plot_info, key[-14:], val[-14:],"FT0_")

    print "\n========= plot FT1  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "ft1_m")
    print key
    print val
    print val[-6:]
    plotter.aQGC_plotting (plot_info, key[-6:], val[-6:],"FT1_")
    # plot FT2
    print "\n========= plot FT2  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "ft2_m")
    print key
    print val
    print val[-11:]
    plotter.aQGC_plotting (plot_info, key[-11:], val[-11:],"FT2_")
    # plot FS0
    print "\n========= plot FS0  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "fs0_m")
    print key
    print val
    print val[-5:]
    plotter.aQGC_plotting (plot_info, key[-5:], val[-5:],"FS0_")
    # plot FS1
    print "\n========= plot FS1  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "fs1_m")
    print key
    print val
    print val[-11:]
    plotter.aQGC_plotting (plot_info, key[-11:], val[-11:],"FS1_")
    # plot FM0
    print "\n========= plot FM0  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "fm0_m")
    print key
    print val
    plotter.aQGC_plotting (plot_info, key, val,"FM0_")
    # plot FM1
    print "\n========= plot FM1  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "fm1_m")
    print key
    print val
    print val[-6:]
    plotter.aQGC_plotting (plot_info, key[-6:], val[-6:],"FM1_")
    # plot FM6
    print "\n========= plot FM6  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "fm6_m")
    print key
    print val
    print val[-14:]
    plotter.aQGC_plotting (plot_info, key[-14:], val[-14:],"FM6_")
    # plot FM7
    print "\n========= plot FM7  ===========\n"
    key,val = plotter.getaQGC_parameters(plot_info, "fm7_m")
    print key
    print val
    print val[-11:]
    plotter.aQGC_plotting (plot_info, key[-11:], val[-11:],"FM7_")
    """

def getPlotArgs():
    parser = plotter.getBasicParser()
    parser.add_argument("-n", "--file_name", nargs='+', type=str, required=False,
                        help="Name of root file where plots are stored")
    parser.add_argument("--is_data", action='store_true',
                        help="Plot histogram with data points")
    return vars(parser.parse_args())
    
if __name__ == "__main__":
    main()
