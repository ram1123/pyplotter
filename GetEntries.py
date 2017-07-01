import os
import ROOT as ROOT
#source = '/eos/uscms/store/user/rasharma/CMSSW_FullSimulation_April2017/aQGC_WPlepWMhadJJ_EWK_SM_DefaultCut_Pythia8CUEP8M1_13TeV_Madgraph/RunIISummer15wmLHEGS/170409_231734/0000'
source = '/uscms_data/d3/rasharma/aQGC_analysis/pyPlotter'
source = '/eos/uscms/store/user/rasharma/CMSSW_FullSimulation_April2017/aQGC_WPlepWMhadJJ_EWK_LO_SMNoDecay_mjj200_Pythia8CUEP8M1_13TeV_Madgraph/RunIISummer15wmLHEGS/170410_120247/'
source = '/eos/uscms/store/user/rasharma/CMSSW_FullSimulation_April2017/aQGC_WPlepWMhadJJ_EWK_LO_NPle1_mjj200_Pythia8CUEP8M1_13TeV_Madgraph'

search1='log'
search2='failed'
Arrayfilepath = []
#for root, dirs, filenames in os.walk(source):
for root, dirs, filenames in os.walk(source):	
	for f in filenames:
		filepath = root + os.sep + f
		#print f
		if filepath.find(search2) == -1:
			if filepath.find(search2) == -1:
				if filepath.endswith(".root"):
					Arrayfilepath.append(filepath)
#print len(Arrayfilepath)					
#print Arrayfilepath[0]

"""
for i in range(0,len(Arrayfilepath)):
	file = ROOT.TFile(Arrayfilepath[i])
	print Arrayfilepath[i]
	if not file:
		print 'Failed to open %s' % Arrayfilepath[i]
		exit(0)
	tree = file.Get('Events')
	print tree.GetEntries()
"""	
print "myfilelist = cms.untracked.vstring()"
print "myfilelist.extend( ["
for i in range(0,len(Arrayfilepath)):
	if ((i+1)%250==0):
		print "\t'file:"+Arrayfilepath[i]+"'"
		print "])"
		print "myfilelist.extend( ["
	else:
		print "\t'file:"+Arrayfilepath[i]+"',"
print "])"
print "process.source = cms.Source(\"PoolSource\", fileNames = myfilelist)"
