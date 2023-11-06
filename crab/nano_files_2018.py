import sys
import os
import subprocess
import readline
import string

data2018_samples = {}
mc2018_samples = {}
# data2018_samples['DYM10to50'] = ['address', 'data/mc', 'dataset', 'year', 'run', 'cross section', 'lumi', 'Neventsraw']

# scalar interaction
# mc2018_samples['2018_LFVStScalarU_UL'] = [['/eos/user/e/etsai/public/LFV_Signal/2018_SMEFTsim_ST_clequ1_lltu/root_NanoAOD/'], 'mc', 'LFVStScalarU', '2018', '', '0.417', '59.83', '100000', 1]
# mc2018_samples['2018_LFVTtScalarU_UL'] = [['/eos/cms/store/user/etsai/LFV_Signal/2018_SMEFTsim_TT_clequ1_lltu/root_NanoAOD/'], 'mc', 'LFVTtScalarU', '2018', '', '0.012', '59.83', '100000', 1]

# background samples
# mc2018_samples['2018_DY10to50_UL'] = [['/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '18610', '59.83', '67981236']
# mc2018_samples['2018_DY50_UL'] = [['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'], 'mc', '', '2018', '', '18610', '59.83', '67981236']
# mc2018_samples['2018_TTTo2L2Nu_UL'] = [['/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '87.31', '59.83', '79140880']
# mc2018_samples['2018_TTToSemiLeptonic_UL'] = [['/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '87.31', '59.83', '79140880']
# mc2018_samples['2018_TTH_UL'] = [['/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.2118', '59.83', '4941250']
# mc2018_samples['2018_TTW_UL'] = [['/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.235', '59.83', '3120397']
# mc2018_samples['2018_TTZ_UL'] = [['/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.281', '59.83', '6017000']
# mc2018_samples['2018_WZ_UL'] = [['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'], 'mc', '', '2018', '', '4.9173', '59.83', '10441724']
# mc2018_samples['2018_ZZ_UL'] = [['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'], 'mc', '', '2018', '', '1.256', '59.83', '52104000']
# mc2018_samples['2018_WWW_UL'] = [['/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.2086', '59.83', '69000']
# mc2018_samples['2018_WWZ_UL'] = [['/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.1651', '59.83', '67000']
# mc2018_samples['2018_WZZ_UL'] = [['/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.05565', '59.83', '137000']
# mc2018_samples['2018_ZZZ_UL'] = [['/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.01476', '59.83', '72000']
# mc2018_samples['2018_WWTo2L2Nu_UL'] = [['/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM'], 'mc', '', '2018', '', '0.01476', '59.83', '72000']
# mc2018_samples['2018_ZZTo2L2Nu_UL'] = [['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM'], 'mc', '', '2018', '', '0.01476', '59.83', '72000']

# data samples
# data2018_samples['2018_A_MuonEG'] = [['/MuonEG/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'MuonEG', '2018', 'A', '1', '1', '1']
# data2018_samples['2018_B_MuonEG'] = [['/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'MuonEG', '2018', 'B', '1', '1', '1']
# data2018_samples['2018_C_MuonEG'] = [['/MuonEG/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'MuonEG', '2018', 'C', '1', '1', '1']
# data2018_samples['2018_D_MuonEG'] = [['/MuonEG/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'MuonEG', '2018', 'D', '1', '1', '1']

# data2018_samples['2018_A_EGamma'] = [['/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'EGamma', '2018', 'A', '1', '1', '1']
# data2018_samples['2018_B_EGamma'] = [['/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'EGamma', '2018', 'B', '1', '1', '1']
# data2018_samples['2018_C_EGamma'] = [['/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'EGamma', '2018', 'C', '1', '1', '1']
# data2018_samples['2018_D_EGamma'] = [['/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD'], 'data', 'EGamma', '2018', 'D', '1', '1', '1']

# data2018_samples['2018_A_DoubleMuon'] = [['/DoubleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'DoubleMuon', '2018', 'A', '1', '1', '1']
# data2018_samples['2018_B_DoubleMuon'] = [['/DoubleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'DoubleMuon', '2018', 'B', '1', '1', '1']
# data2018_samples['2018_C_DoubleMuon'] = [['/DoubleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'DoubleMuon', '2018', 'C', '1', '1', '1']
# data2018_samples['2018_D_DoubleMuon'] = [['/DoubleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'DoubleMuon', '2018', 'D', '1', '1', '1']

# data2018_samples['2018_A_SingleMuon'] = [['/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'SingleMuon', '2018', 'A', '1', '1', '1']
# data2018_samples['2018_B_SingleMuon'] = [['/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'SingleMuon', '2018', 'B', '1', '1', '1']
# data2018_samples['2018_C_SingleMuon'] = [['/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'SingleMuon', '2018', 'C', '1', '1', '1']
# data2018_samples['2018_D_SingleMuon'] = [['/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data', 'SingleMuon', '2018', 'D', '1', '1', '1']
