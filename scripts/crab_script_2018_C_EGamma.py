#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *

# this takes care of converting the input files from CRAB

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.top.topLeptonMVAModule import *
# from PhysicsTools.NanoAODTools.postprocessing.modules.top.lfvSignalModule import *

modulesList = []
# modulesList.append(lfvSignalProducer())
mvareader = topLeptonMVA2018
modulesList.append(mvareader())

cut = '((Sum$(Electron_pt>20 && abs(Electron_eta)<2.4 && Electron_sip3d<8 && abs(Electron_dxy)<0.05 && abs(Electron_dz)<0.1 && Electron_miniPFRelIso_all<0.4 && Electron_lostHits<2 && Electron_convVeto && Electron_tightCharge>0)'
cut += ' + Sum$(Muon_pt>18 && abs(Muon_eta)<2.4 && Muon_mediumId && Muon_sip3d<8 && abs(Muon_dxy)<0.05 && abs(Muon_dz)<0.1 && Muon_miniPFRelIso_all<0.4))>=1)'
cut += ' && ((Sum$(Tau_pt>18 && abs(Tau_eta)<2.3 && Tau_idDeepTau2017v2p1VSe>=2 && Tau_idDeepTau2017v2p1VSmu>=8 && Tau_idDeepTau2017v2p1VSjet>=1 && Tau_decayMode!=5 && Tau_decayMode!=6))>=1)'
jmeCorrections = createJMECorrector(False, 'UL2018', 'C', 'Total', 'AK4PFchs')
modulesList.append(jmeCorrections())
p = PostProcessor('.',
                  inputFiles(),
                  cut,
                  modules=modulesList,
                  provenance=True,
                  fwkJobReport=True,
                  jsonInput=runsAndLumis())

p.run()

print('DONE')
