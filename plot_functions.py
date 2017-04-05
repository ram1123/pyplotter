#!/usr/bin/env python
import ROOT as ROOT
import CMS_lumi, tdrstyle
import argparse

def getaQGC_parameters(plot_info, aQGC_par):
    	file = ROOT.TFile(plot_info["file_name"][0])
    	if not file:
    	    print 'Failed to open %s' % plot_info["file_name"][0]
    	    exit(0)
    	tree = file.Get(plot_info["tree_folder"] + plot_info["tree_name"])
	FT0_key = []
	FT0_val = []
	for n, event in enumerate(tree):
		if n>0:
			break
		indices1 = [i for i, s in enumerate(event.LHEWeightIDs) if aQGC_par in s]
	
		for i in range(0,len(indices1), len(indices1)/6):
			FT0_key.append(indices1[i])
			FT0_val.append(event.LHEWeightIDs[indices1[i]])
		indices1s = [i for i, s in enumerate(event.LHEWeightIDs) if aQGC_par.replace("_m","_0p0") in s]
		FT0_key.append(indices1s[0])
		FT0_val.append(event.LHEWeightIDs[indices1s[0]])
		#print FT0_key
		#print FT0_val
		#print "###########################################"
	return FT0_key,FT0_val

def aQGC_plotting (plot_info, aQGC_key, aQGC_val, outputNameString):
    #c1 = ROOT.TCanvas()
    c1 = getCanvas()
    legend = ROOT.TLegend(.7 ,.60 ,.9 ,.900)
    legend.SetFillColor(ROOT.kWhite)
    file1 = ROOT.TFile(plot_info["file_name"][0])
    if not file1:
        print 'Failed to open %s' % plot_info["file_name"][0]
        exit(0)
    tree1 = file1.Get(plot_info["tree_folder"] + plot_info["tree_name"])

    hist1 = ROOT.TH1F("hist1", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist2 = ROOT.TH1F("hist2", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist3 = ROOT.TH1F("hist3", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist4 = ROOT.TH1F("hist4", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist5 = ROOT.TH1F("hist5", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist6 = ROOT.TH1F("hist6", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist7 = ROOT.TH1F("hist7", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist8 = ROOT.TH1F("hist8", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    

    tree1.Draw(plot_info["tree_var"][0] + ">>hist1","LHEWeights["+str(aQGC_key[0])+"]")
    legend.AddEntry(hist1, aQGC_val[0])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist2","LHEWeights["+str(aQGC_key[1])+"]")
    legend.AddEntry(hist2, aQGC_val[1])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist3","LHEWeights["+str(aQGC_key[2])+"]")
    legend.AddEntry(hist3, aQGC_val[2])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist4","LHEWeights["+str(aQGC_key[3])+"]")
    legend.AddEntry(hist4, aQGC_val[3])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist5","LHEWeights["+str(aQGC_key[4])+"]")
    legend.AddEntry(hist5, aQGC_val[4])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist6","LHEWeights["+str(aQGC_key[5])+"]")
    legend.AddEntry(hist6, aQGC_val[5])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist7","LHEWeights["+str(aQGC_key[6])+"]")
    legend.AddEntry(hist7, aQGC_val[6])
    tree1.Draw(plot_info["tree_var"][0] + ">>hist8","LHEWeights["+str(aQGC_key[7])+"]")
    legend.AddEntry(hist8, aQGC_val[7])


    hist1.Scale(1/hist1.Integral())
    hist2.Scale(1/hist2.Integral())
    hist3.Scale(1/hist3.Integral())
    hist4.Scale(1/hist4.Integral())
    hist5.Scale(1/hist5.Integral())
    hist6.Scale(1/hist6.Integral())
    hist7.Scale(1/hist7.Integral())
    hist8.Scale(1/hist8.Integral())

    setHistAttributes(hist1, plot_info, ROOT.kBlack,0)
    setHistAttributes(hist2, plot_info, ROOT.kRed,0)
    setHistAttributes(hist3, plot_info, ROOT.kGreen,0)
    setHistAttributes(hist4, plot_info, ROOT.kYellow,0)
    setHistAttributes(hist5, plot_info, ROOT.kViolet,0)
    setHistAttributes(hist6, plot_info, ROOT.kPink,0)
    setHistAttributes(hist7, plot_info, ROOT.kMagenta,0)
    setHistAttributes(hist8, plot_info, ROOT.kBlue,0)

    hist1.Draw()
    hist2.Draw("sames")
    hist3.Draw("sames")
    hist4.Draw("sames")
    hist5.Draw("sames")
    hist6.Draw("sames")
    hist7.Draw("sames")
    hist8.Draw("sames")
    legend.Draw("same")
    if plot_info["logy"]:
        c1.SetLogy()
    if plot_info["logx"]:
        c1.SetLogx()
    if plot_info["grid"]:
    	c1.SetGrid()
    #setTDRStyle(c1, 1, 13, plot_info["printCMS"]) 
    setTDRStyle(c1, 1, 13, "No") 
    hist1.GetXaxis().SetTitle(plot_info["xlabel"])
    if plot_info["ylabel"] == "":
        plot_info["ylabel"] = "Events / %s GeV" % int(hist1.GetBinWidth(1))
    hist1.GetYaxis().SetTitle(plot_info["ylabel"])
    c1.SaveAs(str(outputNameString)+plot_info["output_file"])
    #if not hist1:
    #    print 'Failed to get hist from file'
    #    exit(0)
    #hist1.SetDirectory(ROOT.gROOT) # detach "hist" from the file
    #return hist1



def CompHistFromTwoBranchSameFile (plot_info):
    c1 = ROOT.TCanvas()
    legend = ROOT.TLegend(.6 ,.70 ,.885 ,.875)
    legend.SetFillColor(ROOT.kWhite)
    file1 = ROOT.TFile(plot_info["file_name"][0])
    if not file1:
        print 'Failed to open %s' % plot_info["file_name"][0]
        exit(0)
    tree1 = file1.Get(plot_info["tree_folder"] + plot_info["tree_name"])
    tree1 = file2.Get(plot_info["tree_folder"] + plot_info["tree_name"])
    hist1 = ROOT.TH1F("hist1", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist2 = ROOT.TH1F("hist2", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    tree1.Draw(plot_info["tree_var"][0] + ">>hist1",plot_info["weight2"])
    #tree1.Draw(plot_info["tree_var"][0] + ">>hist1","")
    legend.AddEntry(hist1, plot_info["leg1"])

    tree2.Draw(plot_info["tree_var"][1] + ">>hist2",plot_info["weight2"])
    legend.AddEntry(hist2, plot_info["leg2"])

    hist1.Sumw2()
    hist2.Sumw2()
    hist1.Scale(1/hist1.Integral())
    hist2.Scale(1/hist2.Integral())
    setHistAttributes(hist1, plot_info, ROOT.kBlack,0)
    setHistAttributes(hist2, plot_info, ROOT.kRed,0)
    hist1.Draw()
    hist2.Draw("sames")
    legend.Draw("same")
    if plot_info["logy"]:
        c1.SetLogy()
    if plot_info["logx"]:
        c1.SetLogx()
    if plot_info["grid"]:
    	c1.SetGrid()
    #setTDRStyle(c1, 1, 13, plot_info["printCMS"]) 
    setTDRStyle(c1, 1, 13, "No") 
    hist1.GetXaxis().SetTitle(plot_info["xlabel"])
    if plot_info["ylabel"] == "":
        plot_info["ylabel"] = "Events / %s GeV" % int(hist1.GetBinWidth(1))
    hist1.GetYaxis().SetTitle(plot_info["ylabel"])
    c1.SaveAs(plot_info["output_file"])
    #if not hist1:
    #    print 'Failed to get hist from file'
    #    exit(0)
    #hist1.SetDirectory(ROOT.gROOT) # detach "hist" from the file
    #return hist1
def CompHistFromTwoFile (plot_info):
    c1 = ROOT.TCanvas()
    legend = ROOT.TLegend(.6 ,.70 ,.885 ,.875)
    legend.SetFillColor(ROOT.kWhite)
    file1 = ROOT.TFile(plot_info["file_name"][0])
    file2 = ROOT.TFile(plot_info["file_name"][1])
    #print "=======================\n\n"
    #print plot_info["file_name"][0],"\t",plot_info["leg1"]
    #print plot_info["file_name"][1],"\t",plot_info["leg2"]
    #print "\n\n======================="
    if not file1:
        print 'Failed to open %s' % plot_info["file_name"][0]
        exit(0)
    if not file2:
        print 'Failed to open %s' % plot_info["file_name"][1]
        exit(0)
    tree1 = file1.Get(plot_info["tree_folder"] + plot_info["tree_name"])
    tree2 = file2.Get(plot_info["tree_folder"] + plot_info["tree_name"])
    hist1 = ROOT.TH1F("hist1", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    hist2 = ROOT.TH1F("hist2", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    tree1.Draw(plot_info["tree_var"][0] + ">>hist1",plot_info["weight1"])
    #tree1.Draw(plot_info["tree_var"][0] + ">>hist1","")
    legend.AddEntry(hist1, plot_info["leg1"])

    tree2.Draw(plot_info["tree_var"][0] + ">>hist2",plot_info["weight2"])
    legend.AddEntry(hist2, plot_info["leg2"])

    hist1.Sumw2()
    hist2.Sumw2()
    hist1.Scale(1/hist1.Integral())
    hist2.Scale(1/hist2.Integral())
    setHistAttributes(hist1, plot_info, ROOT.kBlack,0)
    setHistAttributes(hist2, plot_info, ROOT.kRed,0)
    hist1.Draw()
    hist2.Draw("sames")
    legend.Draw("same")
    if plot_info["logy"]:
        c1.SetLogy()
    if plot_info["logx"]:
        c1.SetLogx()
    if plot_info["grid"]:
    	c1.SetGrid()
    #setTDRStyle(c1, 1, 13, plot_info["printCMS"]) 
    setTDRStyle(c1, 1, 13, "No") 
    hist1.GetXaxis().SetTitle(plot_info["xlabel"])
    if plot_info["ylabel"] == "":
        plot_info["ylabel"] = "Events / %s GeV" % int(hist1.GetBinWidth(1))
    hist1.GetYaxis().SetTitle(plot_info["ylabel"])
    c1.SaveAs(plot_info["output_file"])
    #if not hist1:
    #    print 'Failed to get hist from file'
    #    exit(0)
    #hist1.SetDirectory(ROOT.gROOT) # detach "hist" from the file
    #return hist1
def getHistFromFile (plot_info):
    file = ROOT.TFile(plot_info["file_name"][0])
    print "File Name: ",plot_info["file_name"][0]
    print "Tree Folder: ",plot_info["tree_folder"]
    if not file:
        print 'Failed to open %s' % plot_info["file_name"][0]
        exit(0)
    tree = file.Get(plot_info["tree_folder"] + plot_info["tree_name"])
    hist = ROOT.TH1F("hist", "Test", plot_info["nbin"], plot_info["xmin"], plot_info["xmax"])    
    tree.Draw(plot_info["tree_var"][0] + ">>hist")
    if not hist:
        print 'Failed to get hist from file'
        exit(0)
    hist.SetDirectory(ROOT.gROOT) # detach "hist" from the file
    return hist
def setHistAttributes (hist, plot_info, line_color, fill_color):
    #hist.SetFillColor(fill_color)
    hist.SetLineColor(line_color)
    hist.SetLineWidth(2)
    if plot_info["rebin"] != 0:
        if type(hist) != "<class '__main__.TH2F'>":
            hist.Rebin(plot_info["rebin"])
        else:
            print 'Rebin only defined for 1D hist. Use --rebin2D instead.'
    #hist.Draw()
    if plot_info["xmin"] < plot_info["xmax"]:
        hist.GetXaxis().SetRangeUser(plot_info["xmin"], plot_info["xmax"])
    if plot_info["ymin"] < plot_info["ymax"]:
        hist.GetYaxis().SetRangeUser(plot_info["ymin"], plot_info["ymax"])
    hist.GetYaxis().SetTitle(plot_info["ylabel"])
def addHistToStack (hist_stack, plot_info, hist_opts, line_color, fill_color):
    hist = getHistFromFile(plot_info)
    setHistAttributes(hist, plot_info, line_color, fill_color)
    hist_stack.Add(hist, hist_opts)
def makePlot (hist, hist_opts, plot_info):
    #legend = ROOT.TLegend(.5 ,.65 ,.885 ,.875)
    canvas = getCanvas()
    setTDRStyle(canvas, 1, 13, plot_info["printCMS"]) 
    if plot_info["logy"]:
        canvas.SetLogy()
    if plot_info["logx"]:
        canvas.SetLogx()
    #draw the lumi text on the canvas
    hist.Draw(hist_opts)
    setTDRStyle(canvas, 1, 13, plot_info["printCMS"]) 
    hist.GetXaxis().SetTitle(plot_info["xlabel"])
    if plot_info["ylabel"] == "":
        plot_info["ylabel"] = "Events / %s GeV" % int(hist.GetBinWidth(1))
    #hist.GetYaxis().SetTitle(plot_info["ylabel"])
    #hist.SetTitleOffset(1.3, "y")
    #hist.SetTitleOffset(1.1, "x")
    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    #frame = canvas.GetFrame()
    #frame.Draw()
    #legend.SetFillColor(ROOT.kWhite)
    #legend.AddEntry(hist, legendName)

    #legend.Draw("same")
    canvas.Print(plot_info["output_file"]) 
def makeStackPlots (stacked, unstacked, hist_opts, plot_info):
    #legend = ROOT.TLegend(.5 ,.65 ,.885 ,.875)
    canvas = getCanvas()
    if plot_info["logy"]:
        canvas.SetLogy()
    if plot_info["logx"]:
        canvas.SetLogx()
    #draw the lumi text on the canvas
    hist1.Draw(hist_opts)
    hist1.GetXaxis().SetTitle(plot_info["xlabel"])
    if plot_info["ylabel"] == "":
        plot_info["ylabel"] = "Events / %s GeV" % int(hist.GetBinWidth(1))
    hist1.GetYaxis().SetTitle(plot_info["ylabel"])
    hist1.SetTitleOffset(1.3, "y")
    hist.SetTitleOffset(1.1, "x")
    setTDRStyle(canvas, 1, 13, plot_info["printCMS"]) 
    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    #frame = canvas.GetFrame()
    #frame.Draw()
    #legend.SetFillColor(ROOT.kWhite)
    #legend.AddEntry(hist, legendName)

    #legend.Draw("same")
    canvas.Print(plot_info["output_file"]) 

def setTDRStyle(canvas, luminosity, energy, printCMS):
    tdrstyle.setTDRStyle() 
    if printCMS == "right" or printCMS == "left":
        if energy == 13:
            CMS_lumi.lumi_13TeV = "%s fb^{-1}" % luminosity
            if printCMS == "left":
                iPos = 11
            else:
                iPos = 13
            CMS_lumi.writeExtraText = 1
            CMS_lumi.extraText = "Preliminary"
            CMS_lumi.CMS_lumi(canvas, 4, iPos)
def getCanvas():
    H_ref = 600; 
    W_ref = 800; 
    W = W_ref
    H  = H_ref

    T = 0.08*H_ref
    B = 0.12*H_ref 
    L = 0.12*W_ref
    R = 0.04*W_ref

    canvas = ROOT.TCanvas("c2","c2",50,50,W,H)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )
    canvas.SetTickx(0)
    canvas.SetTicky(0) 
    return canvas
def getBasicParser():
    parser = argparse.ArgumentParser()
    #parser.add_argument('-n', '--file_name', type=str, required=True, 
    #                    help="Name of root file in which histogram is stored.")
    parser.add_argument('-o', '--output_file', type=str, required=True,
                        help="Name of produced plot file (type pdf/png/jpg etc.).")
    parser.add_argument('-t', '--tree_name', type=str, required=False, default="Ntuple",
                        help="Name of root tree")  
    parser.add_argument('-f', '--tree_folder', type=str, required=False, default="",
                        help="Folder where tree is stored")  
    parser.add_argument('-v', '--tree_var', nargs='+', type=str, required=False,
                        help="Variable name in root tree")  
    parser.add_argument('--xlabel', type=str, required=False, default="", 
                        help="x axis label")
    parser.add_argument('--ylabel', type=str, required=False, default="", 
                        help="y axis label")
    parser.add_argument('--leg1', type=str, required=False, default="Legend 1", 
                        help="First Histo/Rootfile legend")
    parser.add_argument('--leg2', type=str, required=False, default="Legend 2", 
                        help="Second Histo/Rootfile legend")
    parser.add_argument('--weight1', type=str, required=False, default="", 
                        help="Weight corresponding to variable")
    parser.add_argument('--weight2', type=str, required=False, default="", 
                        help="Weight corresponding to variable")
    parser.add_argument('--xmin', type=float, required=False, default=0, 
                        help="minimum x value")
    parser.add_argument('--xmax', type=float, required=False, default=0, 
                        help="maximum x value")   
    parser.add_argument('--ymin', type=float, required=False, default=0, 
                        help="minimum y value")
    parser.add_argument('--ymax', type=float, required=False, default=0, 
                        help="maximum y value")
    parser.add_argument('--nbin', type=int, required=False, default=30, 
                        help="Number of bins to group together (1D only)")
    parser.add_argument('--rebin', type=int, required=False, default=0, 
                        help="Number of bins to group together (1D only)")
    parser.add_argument('--logy', action='store_true',
                        help="Set y axis to logarithmic scale")
    parser.add_argument('--logx', action='store_true', 
                        help="Set x axis to logarithmic scale")
    parser.add_argument('--grid', action='store_true', 
                        help="Set grid for x-y axis")
    parser.add_argument('--printCMS', type=str, default="left",required=False,
                        choices=["left","right"], help="""print 'CMS preliminary' 
                        in left (or right) upper corner""")
    return parser
