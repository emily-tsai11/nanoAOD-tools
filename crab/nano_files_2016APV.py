import sys
import os
import subprocess
import readline
import string

data2016APV_samples = {}
mc2016APV_samples = {}
# data2016APV_samples['DYM10to50'] = ['address', 'data/mc', 'dataset', 'year', 'run', 'cross section', 'lumi', 'Neventsraw']

# scalar interaction
# mc2016APV_samples['2016APV_LFVStScalarU_UL'] = [['/eos/user/e/etsai/public/LFV_Signal/2016APV_SMEFTsim_ST_clequ1_lltu/root_NanoAOD/'], 'mc', 'LFVStScalarU', '2016APV', '', '0.417', '19.50', '100000', 1]
# mc2016APV_samples['2016APV_LFVTtScalarU_UL'] = [['/eos/cms/store/user/etsai/LFV_Signal/2016APV_SMEFTsim_TT_clequ1_lltu/root_NanoAOD/'], 'mc', 'LFVTtScalarU', '2016APV', '', '0.012', '19.50', '100000', 1]

# background samples
# mc2016APV_samples['2016APV_DY10to50_UL'] = [['/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '18610', '19.50', '67981236']
# mc2016APV_samples['2016APV_DY50_UL'] = [['/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '18610', '19.50', '67981236']
# mc2016APV_samples['2016APV_TTTo2L2Nu_UL'] = [['/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '87.31', '19.50', '79140880']
# mc2016APV_samples['2016APV_TTToSemiLeptonic_UL'] = [['/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '87.31', '19.50', '79140880']
# mc2016APV_samples['2016APV_TTH_UL'] = [['/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.2118', '19.50', '4941250']
# mc2016APV_samples['2016APV_TTW_UL'] = [['/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM'], 'mc', '', '2016APV', '', '0.235', '19.50', '3120397']
# mc2016APV_samples['2016APV_TTZ_UL'] = [['/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.281', '19.50', '6017000']
# mc2016APV_samples['2016APV_WZ_UL'] = [['/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '4.9173', '19.50', '10441724']
# mc2016APV_samples['2016APV_ZZ_UL'] = [['/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '1.256', '19.50', '52104000']
# mc2016APV_samples['2016APV_WWW_UL'] = [['/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.2086', '19.50', '69000']
# mc2016APV_samples['2016APV_WWZ_UL'] = [['/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.1651', '19.50', '67000']
# mc2016APV_samples['2016APV_WZZ_UL'] = [['/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.05565', '19.50', '137000']
# mc2016APV_samples['2016APV_ZZZ_UL'] = [['/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.01476', '19.50', '72000']
# mc2016APV_samples['2016APV_WWTo2L2Nu_UL'] = [['/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.01476', '19.50', '72000']
# mc2016APV_samples['2016APV_ZZTo2L2Nu_UL'] = [['/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'], 'mc', '', '2016APV', '', '0.01476', '19.50', '72000']

# data samples
# data2016APV_samples['2016APV_Bv1_MuonEG'] = [['/MuonEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'MuonEG', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_Bv2_MuonEG'] = [['/MuonEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'MuonEG', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_C_MuonEG'] = [['/MuonEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'MuonEG', '2016APV', 'C', '1', '1', '1']
# data2016APV_samples['2016APV_D_MuonEG'] = [['/MuonEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'MuonEG', '2016APV', 'D', '1', '1', '1']
# data2016APV_samples['2016APV_E_MuonEG'] = [['/MuonEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'MuonEG', '2016APV', 'E', '1', '1', '1']
# data2016APV_samples['2016APV_F_MuonEG'] = [['/MuonEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'MuonEG', '2016APV', 'F', '1', '1', '1']

# data2016APV_samples['2016APV_Bv1_DoubleEG'] = [['/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleEG', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_Bv2_DoubleEG'] = [['/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v3/NANOAOD'], 'data', 'DoubleEG', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_C_DoubleEG'] = [['/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleEG', '2016APV', 'C', '1', '1', '1']
# data2016APV_samples['2016APV_D_DoubleEG'] = [['/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleEG', '2016APV', 'D', '1', '1', '1']
# data2016APV_samples['2016APV_E_DoubleEG'] = [['/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleEG', '2016APV', 'E', '1', '1', '1']
# data2016APV_samples['2016APV_F_DoubleEG'] = [['/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleEG', '2016APV', 'F', '1', '1', '1']

# data2016APV_samples['2016APV_Bv1_DoubleMuon'] = [['/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_Bv2_DoubleMuon'] = [['/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_C_DoubleMuon'] = [['/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016APV', 'C', '1', '1', '1']
# data2016APV_samples['2016APV_D_DoubleMuon'] = [['/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016APV', 'D', '1', '1', '1']
# data2016APV_samples['2016APV_E_DoubleMuon'] = [['/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016APV', 'E', '1', '1', '1']
# data2016APV_samples['2016APV_F_DoubleMuon'] = [['/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'DoubleMuon', '2016APV', 'F', '1', '1', '1']

# data2016APV_samples['2016APV_Bv1_SingleElectron'] = [['/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleElectron', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_Bv2_SingleElectron'] = [['/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleElectron', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_C_SingleElectron'] = [['/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleElectron', '2016APV', 'C', '1', '1', '1']
# data2016APV_samples['2016APV_D_SingleElectron'] = [['/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleElectron', '2016APV', 'D', '1', '1', '1']
# data2016APV_samples['2016APV_E_SingleElectron'] = [['/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleElectron', '2016APV', 'E', '1', '1', '1']
# data2016APV_samples['2016APV_F_SingleElectron'] = [['/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleElectron', '2016APV', 'F', '1', '1', '1']

# data2016APV_samples['2016APV_Bv1_SingleMuon'] = [['/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleMuon', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_Bv2_SingleMuon'] = [['/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleMuon', '2016APV', 'B', '1', '1', '1']
# data2016APV_samples['2016APV_C_SingleMuon'] = [['/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleMuon', '2016APV', 'C', '1', '1', '1']
# data2016APV_samples['2016APV_D_SingleMuon'] = [['/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleMuon', '2016APV', 'D', '1', '1', '1']
# data2016APV_samples['2016APV_E_SingleMuon'] = [['/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleMuon', '2016APV', 'E', '1', '1', '1']
# data2016APV_samples['2016APV_F_SingleMuon'] = [['/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'], 'data', 'SingleMuon', '2016APV', 'F', '1', '1', '1']
