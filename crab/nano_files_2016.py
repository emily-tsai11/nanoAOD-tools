import sys
import os
import subprocess
import readline
import string

data2016_samples = {}
mc2016_samples = {}
# data2016_samples['DYM10to50'] = ['address', 'data/mc', 'dataset', 'year', 'run', 'cross section', 'lumi', 'Neventsraw']

# scalar interaction
# mc2016_samples['2016_LFVStScalarU_UL'] = [['/eos/user/e/etsai/workspace/MCProduction/2016_SMEFTsim_ST_clequ1_lltu/root_NanoAOD/'], 'mc', 'LFVStScalarU', '2016', '', '0.417', '16.81', '100000', 1]
# mc2016_samples['2016_LFVTtScalarU_UL'] = [['/eos/cms/store/user/etsai/workspace/MCProduction/2016_SMEFTsim_TT_clequ1_lltu/root_NanoAOD/'], 'mc', 'LFVTtScalarU', '2016', '', '0.012', '16.81', '100000', 1]

# background samples
# mc2016_samples['2016_DY10to50_UL'] = [['/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '18610', '16.81', '67981236']
# mc2016_samples['2016_DY50_UL'] = [['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '18610', '16.81', '67981236']
# mc2016_samples['2016_TTTo2L2Nu_UL'] = [['/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '87.31', '16.81', '79140880']
# mc2016_samples['2016_TTToSemiLeptonic_UL'] = [['/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '87.31', '16.81', '79140880']
# mc2016_samples['2016_TTH_UL'] = [['/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.2118', '16.81', '4941250']
# mc2016_samples['2016_TTW_UL'] = [['/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.235', '16.81', '3120397']
# mc2016_samples['2016_TTZ_UL'] = [['/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.281', '16.81', '6017000']
# mc2016_samples['2016_WZ_UL'] = [['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '4.9173', '16.81', '10441724']
# mc2016_samples['2016_ZZ_UL'] = [['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '1.256', '16.81', '52104000']
# mc2016_samples['2016_WWW_UL'] = [['/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.2086', '16.81', '69000']
# mc2016_samples['2016_WWZ_UL'] = [['/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.1651', '16.81', '67000']
# mc2016_samples['2016_WZZ_UL'] = [['/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.05565', '16.81', '137000']
# mc2016_samples['2016_ZZZ_UL'] = [['/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.01476', '16.81', '72000']
# mc2016_samples['2016_WWTo2L2Nu_UL'] = [['/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.01476', '16.81', '72000']
# mc2016_samples['2016_ZZTo2L2Nu_UL'] = [['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM'], 'mc', '', '2016', '', '0.01476', '16.81', '72000']

# data samples
# data2016_samples['2016_F_MuonEG'] = [['/MuonEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'MuonEG', '2016', 'F', '1', '1', '1']
# data2016_samples['2016_G_MuonEG'] = [['/MuonEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'MuonEG', '2016', 'G', '1', '1', '1']
# data2016_samples['2016_H_MuonEG'] = [['/MuonEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'MuonEG', '2016', 'H', '1', '1', '1']

# data2016_samples['2016_F_DoubleEG'] = [['/DoubleEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'DoubleEG', '2016', 'F', '1', '1', '1']
# data2016_samples['2016_G_DoubleEG'] = [['/DoubleEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'DoubleEG', '2016', 'G', '1', '1', '1']
# data2016_samples['2016_H_DoubleEG'] = [['/DoubleEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'DoubleEG', '2016', 'H', '1', '1', '1']

# data2016_samples['2016_F_DoubleMuon'] = [['/DoubleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'DoubleMuon', '2016', 'F', '1', '1', '1']
# data2016_samples['2016_G_DoubleMuon'] = [['/DoubleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016', 'G', '1', '1', '1']
# data2016_samples['2016_H_DoubleMuon'] = [['/DoubleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'DoubleMuon', '2016', 'H', '1', '1', '1']

# data2016_samples['2016_F_SingleElectron'] = [['/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'SingleElectron', '2016', 'F', '1', '1', '1']
# data2016_samples['2016_G_SingleElectron'] = [['/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'SingleElectron', '2016', 'G', '1', '1', '1']
# data2016_samples['2016_H_SingleElectron'] = [['/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'SingleElectron', '2016', 'H', '1', '1', '1']

# data2016_samples['2016_F_SingleMuon'] = [['/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'SingleMuon', '2016', 'F', '1', '1', '1']
# data2016_samples['2016_G_SingleMuon'] = [['/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'SingleMuon', '2016', 'G', '1', '1', '1']
data2016_samples['2016_H_SingleMuon'] = [['/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data', 'SingleMuon', '2016', 'H', '1', '1', '1']
