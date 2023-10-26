import sys
import os
import subprocess
import readline
import string

data2017_samples = {}
mc2017_samples = {}
#data2017_samples ['DYM10to50'] = ['address', 'data/mc','dataset','year', 'run', 'cross section','lumi','Neventsraw']

## scalar interaction
mc2017_samples['2017_LFVStScalarU_UL'] = [['/eos/user/e/etsai/workspace/MCProduction/2017_SMEFTsim_ST_clequ1_lltu/root_NanoAOD/'], 'mc','LFVStScalarU','2017', '','0.417' ,'41.48','100000',1]
mc2017_samples['2017_LFVTtScalarU_UL'] = [['/eos/cms/store/user/etsai/workspace/MCProduction/2017_SMEFTsim_TT_clequ1_lltu/root_NanoAOD/'], 'mc','LFVTtScalarU','2017', '','0.012','41.48','100000',1]

##Background samples
# mc2017_samples['2017_DY10to50_UL'] = [['/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','18610','41.48','67981236']
# mc2017_samples['2017_DY50_UL'] = [['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM'], 'mc','','2017', '','18610','41.48','67981236']
# mc2017_samples['2017_TTTo2L2Nu_UL'] = [['/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','87.31','41.48','79140880']
# mc2017_samples['2017_TTToSemiLeptonic_UL'] = [['/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','87.31','41.48','79140880']
# mc2017_samples['2017_TTH_UL'] = [['/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.2118','41.48','4941250']
# mc2017_samples['2017_TTW_UL'] = [['/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.235','41.48','3120397']
# mc2017_samples['2017_TTZ_UL'] = [['/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.281','41.48','6017000']
# mc2017_samples['2017_WZ_UL'] = [['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM'], 'mc','','2017', '','4.9173','41.48','10441724']
# mc2017_samples['2017_ZZ_UL'] = [['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM'], 'mc','','2017', '','1.256','41.48','52104000']
# mc2017_samples['2017_WWW_UL'] = [['/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.2086','41.48','69000']
# mc2017_samples['2017_WWZ_UL'] = [['/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.1651','41.48','67000']
# mc2017_samples['2017_WZZ_UL'] = [['/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.05565','41.48','137000']
# mc2017_samples['2017_ZZZ_UL'] = [['/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.01476','41.48','72000']
# mc2017_samples['2017_WWTo2L2Nu_UL'] = [['/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM'], 'mc','','2017', '','0.01476','41.48','72000']
# mc2017_samples['2017_ZZTo2L2Nu_UL'] = [['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM'], 'mc','','2017', '','0.01476','41.48','72000']

# data2017_samples['2017_B_MuonEG'] = [['/MuonEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','MuonEG','2017', 'B','1','1','1']
# data2017_samples['2017_C_MuonEG'] = [['/MuonEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','MuonEG','2017', 'C','1','1','1']
# data2017_samples['2017_D_MuonEG'] = [['/MuonEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','MuonEG','2017', 'D','1','1','1']
# data2017_samples['2017_E_MuonEG'] = [['/MuonEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','MuonEG','2017', 'E','1','1','1']
# data2017_samples['2017_F_MuonEG'] = [['/MuonEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','MuonEG','2017', 'F','1','1','1']

# data2017_samples['2017_B_DoubleEG'] = [['/DoubleEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleEG','2017', 'B','1','1','1']
# data2017_samples['2017_C_DoubleEG'] = [['/DoubleEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleEG','2017', 'C','1','1','1']
# data2017_samples['2017_D_DoubleEG'] = [['/DoubleEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleEG','2017', 'D','1','1','1']
# data2017_samples['2017_E_DoubleEG'] = [['/DoubleEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleEG','2017', 'E','1','1','1']
# data2017_samples['2017_F_DoubleEG'] = [['/DoubleEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleEG','2017', 'F','1','1','1']

# data2017_samples['2017_B_DoubleMuon'] = [['/DoubleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleMuon','2017', 'B','1','1','1']
# data2017_samples['2017_C_DoubleMuon'] = [['/DoubleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleMuon','2017', 'C','1','1','1']
# data2017_samples['2017_D_DoubleMuon'] = [['/DoubleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleMuon','2017', 'D','1','1','1']
# data2017_samples['2017_E_DoubleMuon'] = [['/DoubleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleMuon','2017', 'E','1','1','1']
# data2017_samples['2017_F_DoubleMuon'] = [['/DoubleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','DoubleMuon','2017', 'F','1','1','1']

# data2017_samples['2017_B_SingleElectron'] = [['/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','SingleElectron','2017', 'B','1','1','1']
# data2017_samples['2017_C_SingleElectron'] = [['/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','SingleElectron','2017', 'C','1','1','1']
# data2017_samples['2017_D_SingleElectron'] = [['/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','SingleElectron','2017', 'D','1','1','1']
# data2017_samples['2017_E_SingleElectron'] = [['/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','SingleElectron','2017', 'E','1','1','1']
# data2017_samples['2017_F_SingleElectron'] = [['/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'], 'data','SingleElectron','2017', 'F','1','1','1']

# data2017_samples['2017_B_SingleMuon'] = [['/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data','SingleMuon','2017', 'B','1','1','1']
# data2017_samples['2017_C_SingleMuon'] = [['/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data','SingleMuon','2017', 'C','1','1','1']
# data2017_samples['2017_D_SingleMuon'] = [['/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data','SingleMuon','2017', 'D','1','1','1']
# data2017_samples['2017_E_SingleMuon'] = [['/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9_GT36-v2/NANOAOD'], 'data','SingleMuon','2017', 'E','1','1','1']
# data2017_samples['2017_F_SingleMuon'] = [['/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'], 'data','SingleMuon','2017', 'F','1','1','1']