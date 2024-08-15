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
    # you can change only this line!!
    'file:/eos/home-e/etsai/workspace/TopLFV_Nano_CMSSW_10_6_27/src/PhysicsTools/NanoAOD/test/2016postVFP_TTTo2L2Nu.root'
    # 'file:/eos/home-e/etsai/workspace/TopLFV_Nano_CMSSW_10_6_27/src/PhysicsTools/NanoAOD/test/2016postVFP_TTToSemiLeptonic.root'
    # 'file:/eos/user/e/etsai/workspace/TopLFV_Nano_CMSSW_10_6_27/src/PhysicsTools/NanoAOD/test/2016postVFP_TTW.root'
    # 'file:/eos/home-e/etsai/workspace/TopLFV_Nano_CMSSW_10_6_27/src/PhysicsTools/NanoAOD/test/2016postVFP_DYM50.root'
]
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(10))
process.output = cms.OutputModule('PoolOutputModule',
                                  fileName=cms.untracked.string('tree.root'))
process.out = cms.EndPath(process.output)
