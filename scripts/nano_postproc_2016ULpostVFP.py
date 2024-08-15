#!/usr/bin/env python

# python3 nano_postproc_2016ULpostVFP.py . ../../NanoAOD/test/2016postVFP_SAMPLE.root

import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *

# this takes care of converting the input files from CRAB

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
# from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.top.topLeptonMVAModule import *
# from PhysicsTools.NanoAODTools.postprocessing.modules.top.lfvSignalModule import *

modulesList = []
# modulesList.append(lfvSignalProducer())
mvareader = topLeptonMVA2016
modulesList.append(mvareader())

cut = "((Sum$(Electron_pt>18 && abs(Electron_eta)<2.5 && Electron_sip3d<15) + Sum$(Muon_pt>18 && abs(Muon_eta)<2.4 && Muon_sip3d<15 && Muon_mediumId))>=2)"
cut += " && ((Sum$(Tau_pt>18 && abs(Tau_eta)<2.3 && Tau_decayMode!=5 && Tau_decayMode!=6))>=1)"
jmeCorrections = createJMECorrector(True, 'UL2016', '', 'Total', 'AK4PFPuppi')
modulesList.append(jmeCorrections())
# modulesList.append(btagSFUL2016()) # No SFs yet
p = PostProcessor('.',
                  inputFiles(),
                  cut,
                  modules=modulesList,
                  provenance=True,
                  fwkJobReport=True,
                  jsonInput=runsAndLumis(),
                  outputbranchsel="keep_and_drop.txt")

p.run()

print('DONE')
