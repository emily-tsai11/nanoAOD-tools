# this fake PSET is needed for local test and for crab to figure the output
# filename you do not need to edit it unless you want to do a local test using
# a different input file than the one marked below
import FWCore.ParameterSet.Config as cms
process = cms.Process('NANO')
process.source = cms.Source(
    'PoolSource',
    fileNames=cms.untracked.vstring(),
    # lumisToProcess=cms.untracked.VLuminosityBlockRange('254231:1-254231:24')
)
process.source.fileNames = [
    'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL16NanoAODAPVv9/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/NANOAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2530000/18B3F965-03D8-9C4B-87CA-426B884BF8DA.root' # you can change only this line!!
]
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(10))
process.output = cms.OutputModule('PoolOutputModule',
                                  fileName=cms.untracked.string('tree.root'))
process.out = cms.EndPath(process.output)
