# run with command:
# python scripts/nano_postproc.py outDir /eos/cms/store/user/jingyan/LFV_Inclusive_Trilep/2016_TTH_UL/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/crab_Inclusive_Trilep_2016_TTH_UL/230331_075911/0000/tree_11.root -I PhysicsTools.NanoAODTools.postprocessing.examples.topLeptonMVAModule topLeptonMVA2016 --bi scripts/keep_and_drop.txt --bo scripts/keep_and_drop.txt


from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
import xgboost as xgb
import numpy as np
from math import log, isnan, sqrt, pi

ROOT.PyConfig.IgnoreCommandLineOptions = True


def deltaPhi(phi1, phi2, returnAbs = True):
    if isnan(phi1) or isnan(phi2): return float('nan')
    dphi = phi2 - phi1
    if dphi > pi:
        dphi -= 2.0 * pi
    if dphi <= -pi:
        dphi += 2.0 * pi
    if returnAbs:
        return abs(dphi)
    else:
        return dphi


class TopLeptonMVAProducer(Module):
    def __init__(self, year, versions = ["v1", "v2"]):
        yearstring = "UL18"
        if year == "UL2016":
            yearstring = "UL16"
        elif year == "UL2016_preVFP":
            yearstring = "UL16APV"
        elif year == "UL2017":
            yearstring = "UL17"
        elif year == "UL2018":
            yearstring = "UL18"

        self.versions = versions

        # Working points
        self.WPs = {"v1": [0.20, 0.41, 0.64, 0.81],
                    "v2": [0.59, 0.81, 0.90, 0.94]}

        directory = "data/mvaWeights/"
        # Load electron weights
        self.bst_el = {}
        self.bst_mu = {}
        if "v1" in self.versions:
            self.bst_el["v1"] = xgb.Booster()
            self.bst_el["v1"].load_model(directory + "el_TOP" + yearstring + "_XGB.weights.bin")
        if "v2" in self.versions:
            self.bst_el["v2"] = xgb.Booster()
            self.bst_el["v2"].load_model(directory + "el_TOPv2" + yearstring + "_XGB.weights.bin")
        # Load muon weights
        if "v1" in self.versions:
            self.bst_mu["v1"] = xgb.Booster()
            self.bst_mu["v1"].load_model(directory + "mu_TOP" + yearstring + "_XGB.weights.bin")
        if "v2" in self.versions:
            self.bst_mu["v2"] = xgb.Booster()
            self.bst_mu["v2"].load_model(directory + "mu_TOPv2" + yearstring + "_XGB.weights.bin")

        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for v in self.versions:
            self.out.branch("Electron_topLeptonMVA_" + v, "F", lenVar = "nElectron")
            self.out.branch("Electron_topLeptonWP_" + v, "F", lenVar = "nElectron")
            self.out.branch("Muon_topLeptonMVA_" + v, "F", lenVar = "nMuon")
            self.out.branch("Muon_topLeptonWP_" + v, "F", lenVar = "nMuon")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        results = {}
        for v in self.versions:
            results["electronMVAs_" + v] = []
            results["electronWPs_" + v] = []
            results["muonMVAs_" + v] = []
            results["muonWPs_" + v] = []

        jets = Collection(event, "Jet")
        dRmin = 0.4
        minJetPt = 25

        electrons = Collection(event, "Electron")
        for electron in electrons:
            electron_jetPtRatio = 1 / (electron.jetRelIso + 1)

            # closest jet
            electron_jetBTag = 0
            for j in jets:
                j_isNominal = j.pt > minJetPt
                if not j_isNominal: continue # compute topLeptonMVA from jets that satisfy the nominal pt cut
                deta = j.eta - electron.eta
                dphi = deltaPhi(j.phi, electron.phi) # deltaPhi has to be between -pi and +pi
                dR = sqrt(deta * deta + dphi * dphi)
                if dR < dRmin:
                    dRmin = dR
                    electron_jetBTag = j.btagDeepFlavB

            features = np.array([[
                electron.pt,
                electron.eta,
                electron.jetNDauCharged,
                electron.miniPFRelIso_chg,
                electron.miniPFRelIso_all - electron.miniPFRelIso_chg,
                electron.jetPtRelv2,
                electron_jetPtRatio,
                electron.pfRelIso03_all,
                electron_jetBTag,
                electron.sip3d,
                log(abs(electron.dxy)),
                log(abs(electron.dz)),
                electron.mvaFall17V2noIso,
                electron.lostHits,
            ]])

            dtest = xgb.DMatrix(features)
            for v in self.versions:
                mvaScore = self.bst_el[v].predict(dtest)[0]
                WP = 0
                for wp in self.WPs[v]:
                    if mvaScore > wp:
                        WP += 1
                results["electronMVAs_" + v].append(mvaScore)
                results["electronWPs_" + v].append(WP)

        muons = Collection(event, "Muon")
        for muon in muons:
            muon_jetPtRatio = 1 / (muon.jetRelIso + 1)

            # closest jet
            muon_jetBTag = 0
            for j in jets:
                j_isNominal = j.pt > minJetPt
                if not j_isNominal: continue # compute topLeptonMVA from jets that satisfy the nominal pt cut
                deta = j.eta - muon.eta
                dphi = deltaPhi(j.phi, muon.phi) # deltaPhi has to be between -pi and +pi
                dR = sqrt(deta * deta + dphi * dphi)
                if dR < dRmin:
                    dRmin = dR
                    muon_jetBTag = j.btagDeepFlavB

            features = np.array([[
                muon.pt,
                muon.eta,
                muon.jetNDauCharged,
                muon.miniPFRelIso_chg,
                muon.miniPFRelIso_all - muon.miniPFRelIso_chg,
                muon.jetPtRelv2,
                muon_jetPtRatio,
                muon.pfRelIso03_all,
                muon_jetBTag,
                muon.sip3d,
                log(abs(muon.dxy)),
                log(abs(muon.dz)),
                muon.segmentComp,
            ]])

            dtest = xgb.DMatrix(features)
            for v in self.versions:
                mvaScore = self.bst_mu[v].predict(dtest)[0]
                WP = 0
                for wp in self.WPs[v]:
                    if mvaScore > wp:
                        WP += 1
                results["muonMVAs_" + v].append(mvaScore)
                results["muonWPs_" + v].append(WP)

        for v in self.versions:
            self.out.fillBranch("Electron_topLeptonMVA_" + v, results["electronMVAs_" + v])
            self.out.fillBranch("Electron_topLeptonWP_" + v, results["electronWPs_" + v])
            self.out.fillBranch("Muon_topLeptonMVA_" + v, results["muonMVAs_" + v])
            self.out.fillBranch("Muon_topLeptonWP_" + v, results["muonWPs_" + v])

        return True


def getLeptonMVAProducer(year):
    return lambda: TopLeptonMVAProducer(year)


topLeptonMVA2016 = getLeptonMVAProducer("UL2016")
# topLeptonMVA2016APV = getLeptonMVAProducer("UL2016_preVFP")
# topLeptonMVA2017 = getLeptonMVAProducer("UL2017")
# topLeptonMVA2018 = getLeptonMVAProducer("UL2018")
