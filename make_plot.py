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
    canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)
    #hist = plotter.getHistFromFile(plot_info)
    hist = plotter.CompHistFromTwoFile(plot_info)
    if type(hist) == "<class '__main__.TH2F'>":
        hist_opts = "colz"
    elif plot_info["is_data"]:
        hist_opts = "e1"
        line_color = ROOT.kBlack
        fill_color = ROOT.kBlack
    else:
        hist_opts = "hist"
        line_color = ROOT.kRed+4
        fill_color = ROOT.kOrange-8
    #plotter.setHistAttributes(hist, plot_info, line_color, fill_color)
    #plotter.makePlot(hist, hist_opts, plot_info)
def getPlotArgs():
    parser = plotter.getBasicParser()
    parser.add_argument("-n", "--file_name", nargs='+', type=str, required=False,
                        help="Name of root file where plots are stored")
    parser.add_argument("--is_data", action='store_true',
                        help="Plot histogram with data points")
    return vars(parser.parse_args())
    
if __name__ == "__main__":
    main()
