import argparse
import subprocess
import sys
import os
import readline
import string
import nano_files_2016APV
from GFAL_GetROOTfiles import *


# set up an argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--n', dest='DATE')# Name tag for data, I use the day I submitted the CRAB jobs
### above is only option you need to set, 
### it will run everything 

### unless you set the option below
### ARGS.SELECTED to a name from the keys of the
### nano_files_2017.py dictionary e.g.  '2017_LFVStVecC' #'2017_ST_atW'
### Then it will run only this dataset
parser.add_argument('--s', dest = 'SELECTED', default= None) 

parser.add_argument('--y', dest='YEAR', default='2016APV')

### Do NOT set below options, they will be set for you for each dataset
parser.add_argument('--e', dest='ERA', default= None)
parser.add_argument('--d', dest = 'DATASET', default= None) 
parser.add_argument('--mod', dest = 'MCORDATA', default= None) 
parser.add_argument('--isd', dest = 'ISDATA', default= None) 
parser.add_argument('--dt', dest = 'DATATYPE', default= None) 
parser.add_argument('--l', dest = 'LETTER', default= None) 
parser.add_argument('--id', dest='ID', default= None)


ARGS = parser.parse_args()

SAMPLES = {}

if ARGS.YEAR == '2016APV':
  SAMPLES.update(nano_files_2016APV.mc2016APV_samples)
#   SAMPLES.update(nano_files_2016APV.data2016APV_samples)

dirname = 'CRABtasks' ## If we want to change this then we should make it an ARG so we can edit name is script below

os.system('mkdir '+ dirname )
print "make CRABtasks directory to store CRAB submit scripts"
published = True

SUBMIT_SCRIPT = '''                                                                                                                                       
#!/usr/bin/env python                                                                                                                                        

import os, subprocess                                                                                                                                                  
print "Now submitting your CRAB jobs to find the LFV Top selected events from our TOP nanoAOD samples"

'''


## list of keys we ran over to use for the CRAB submit script
ids = []

for key, item in SAMPLES.items() :
#    ARGS.DATASET = samp

    #if ARGS.SELECTED != None :
    #    if key != ARGS.SELECTED :
    #        continue
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ new MC or data sample $$$$$$$$$$$$$$$$$$$$$$$$$"  

    print key 
    print item
    print SAMPLES[key]


    dataset = item[0]

    ARGS.MCORDATA = item[1]

    if ARGS.MCORDATA == 'data':
       ARGS.ISDATA = True
    elif ARGS.MCORDATA == 'mc':
       ARGS.ISDATA = False



    ARGS.DATATYPE = item[2] # e.g. 'DoubleMu'
    if ARGS.MCORDATA == 'mc':
       ARGS.DATATYPE = key

    ARGS.ERA = 'UL2016_preVFP'

    ARGS.LETTER = item[4] # data section e.g.  B   

    splits = dataset[0].split('/')[-1]
    if len(dataset) > 1 :
        # if there is more than 1 file location or dataset in the let then look thorugh them all
        # if the first one ends in USER then it is a dataset name
        
        print splits
        if 'USER' in splits:
            ARGS.DATASET = [dataset[0]]
            published = True
            print "Dataset name was given so CRAB submission will use this to submit"
        elif '0000' in splits:
            ARGS.DATASET = [dataset[0]]
            published = False
            print "Dataset location was given so CRAB submission will use files in that location to submit"            
 
        print "WARNING: If any dataset has more than 1 input dataset or file location this script is only submitting the first, fix this soon..."
        if ( len(dataset) > 2  ):
            if 'USER' in splits:
               
                ARGS.DATASET = [ dataset[1]  , dataset[2]  ]
                published = False
                if '2017_TTZToQQ' in key :
                    ARGS.DATASET = [ dataset[1]  , dataset[2] , dataset[3]  ]
                ### if there is more than 1 dataset, eg. if there are extensions to the MC, 
                ### then usually, 1st in list is the dataset name
                ### 2nd entry is basically a duplicate, it is the file location of that same datset
                ### 3rd entry is the location of the extension files, usually asparker cms eos space bc we created those ourselves so they are unpublished
        if ( published == False and len(dataset) == 2   ):
           
            ARGS.DATASET = [ dataset[0]  , dataset[1]  ]


    elif  len(dataset)  == 1 :
        ARGS.DATASET =  [dataset[0]] 
        if ('USER' in splits) or ('NANOAODSIM' in splits) or ('NANOAOD' in splits):
            published = True
            print "Dataset name was given so CRAB submission will use this to submit"
        else:
            published = False
            print "Dataset location was given so CRAB submission will use files in that location to submit"

    elif len(dataset)  < 1 :    
        print "ERROR: No dataset name or file location given!!! "
    print "dataset or location :"
    print ARGS.DATASET

    idname = key #id0 +  id2
    ARGS.SELECTED = idname

    print idname



    # make a CRAB config file with template arguments
    CRAB_CFG = '''
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config
config = Configuration()

idname = '{SELECTED}'
dirname = 'CRABtasks'

config.section_("General")
config.General.requestName = '%s_%s' % ( '{DATE}', idname )
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script_%s.sh' % ( idname )
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script_%s.py' % ( idname), '../../scripts/haddnano.py']
config.JobType.sendPythonFolder = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxJobRuntimeMin = 100
'''

    if not published :
        if len(ARGS.DATASET) == 1 :
            print dataset
            print "getting files for unpublished submission : "
            ARGS.DATASET = GFAL_GetROOTfiles( dataset[0] )
        else :
           df = [] #None
           print ARGS.DATASET
           print len(ARGS.DATASET)

           for d in ARGS.DATASET:
               print d 
               tdf = GFAL_GetROOTfiles( d )
               df += tdf
           ARGS.DATASET = df
           print ARGS.DATASET
        ## Now that we have the input files, we can make the file input part of the CRAB cfg file         

        CRAB_CFG_UNPUB= '''
config.section_("Data")                                                                                                                             

filelist = {DATASET}
#for l in jobsLines:
#    filelist.append(str(l[:-1]))
#print filelist 
config.Data.userInputFiles = filelist
config.Data.splitting = 'FileBased'                                                                           
config.Data.unitsPerJob = 1  
'''

    if published:
        ARGS.DATASET = dataset[0]
        CRAB_CFG_PUB= '''                                                                                                                                         
config.section_("Data")                                                                                                                                       
config.Data.inputDataset = '{DATASET}'                                                                       

config.Data.splitting = 'FileBased'                                                                                                                                                                                        
config.Data.unitsPerJob = 1
'''


    CRAB_CFG3 = '''
#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.outLFNDirBase = '/store/user/%s/LFV_%s/%s' % ( 'jingyan', '{DATE}' ,idname )
config.Data.publication = False
config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
#config.Site.blacklist = ['T2_BE_UCL']

'''

    if published :
        CRAB_CFG = CRAB_CFG + CRAB_CFG_PUB +  CRAB_CFG3 
    else :    
        CRAB_CFG = CRAB_CFG + CRAB_CFG_UNPUB +  CRAB_CFG3 

    # open crabConfig.py, substitute into CRAB_CFG the arguments from ARGS, write it, run it, and remove it

    open('%s/crabConfig%s.py'% (dirname , idname ) , 'w').write(CRAB_CFG.format(**ARGS.__dict__))

    #open('crab_cfg_%s.py' % (idname), 'w').write(CRAB_CFG.format(**ARGS.__dict__))



    ### make the runPostProcessor.py script
    CRAB_SCRIPT0 = '''
#!/usr/bin/env python
    '''
    CRAB_SCRIPT1 = CRAB_SCRIPT0 + '''


import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *

# this takes care of converting the input files from CRAB

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.top.topLeptonMVAModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.top.lfvSignalModule import *

modulesList = []
# modulesList.append(lfvSignalProducer())
mvareader = topLeptonMVA2016APV
modulesList.append(mvareader())

cut = "((Sum$(Electron_pt>18 && abs(Electron_eta)<2.5 && Electron_sip3d<15) + Sum$(Muon_pt>18 && abs(Muon_eta)<2.4 && Muon_sip3d<15 && Muon_mediumId))>=2)"
cut += " && ((Sum$(Tau_pt>18 && abs(Tau_eta)<2.3 && Tau_idDeepTau2017v2p1VSe>=1 && Tau_idDeepTau2017v2p1VSmu>=1 && Tau_idDeepTau2017v2p1VSjet>=1 && Tau_decayMode!=5 && Tau_decayMode!=6))>=1)"

    '''
    CRAB_MC = '''
jmeCorrections = createJMECorrector(True, "{ERA}", "{LETTER}", "Total", "AK4PFchs") 
modulesList.append(jmeCorrections())   
modulesList.append(btagSFUL2016APV())  
    '''
    CRAB_DATA = '''
jmeCorrections = createJMECorrector(False, "{ERA}", "{LETTER}", "Total", "AK4PFchs") 
modulesList.append(jmeCorrections())                  
    '''
    CRAB_END = '''                                                                     
p = PostProcessor(".",
                  inputFiles(),
                  cut,
                  modules=modulesList,
                  provenance=True,
                  fwkJobReport=True,
                  jsonInput=runsAndLumis())

p.run()

print("DONE")

    '''

    if ARGS.ISDATA :
        CRAB_SCRIPT = CRAB_SCRIPT1 + CRAB_DATA + CRAB_END
    else :
        CRAB_SCRIPT = CRAB_SCRIPT1 + CRAB_MC + CRAB_END



    open('%s/crab_script_%s.py' % (dirname, idname), 'w').write(CRAB_SCRIPT.format(**ARGS.__dict__))


    BASH_SCRIPT = '''
#this is not mean to be run locally                                                                                                                          echo Check if TTY
if [ "`tty`" != "not a tty" ]; then
echo "YOU SHOULD NOT RUN THIS IN INTERACTIVE, IT DELETES YOUR LOCAL FILES"
else
echo "%%%%%%%%%%%%%%%%%  Running my nano CRAB  %%%%%%%%%%%%%%%%%%%%%%%%% "
echo "ENV..................................."
env
echo "VOMS"
voms-proxy-info -all
echo "CMSSW BASE, python path, pwd"
echo $CMSSW_BASE
echo $PYTHON_PATH
echo $PWD
rm -rf $CMSSW_BASE/lib/
rm -rf $CMSSW_BASE/src/
rm -rf $CMSSW_BASE/module/
rm -rf $CMSSW_BASE/python/
mv lib $CMSSW_BASE/lib
mv src $CMSSW_BASE/src
mv module $CMSSW_BASE/module
mv python $CMSSW_BASE/python

echo Found Proxy in: $X509_USER_PROXY


selected=('{SELECTED}')
py_command=('crab_script_')
py_command2=('.py')
echo "$py_command""$selected""$py_command2" $1
python "$py_command""$selected""$py_command2" $1


fi



    '''
    open('%s/crab_script_%s.sh' % (dirname, idname), 'w').write(BASH_SCRIPT.format(**ARGS.__dict__))

    ids.append(idname)

subprocess.call('cp PSet.py %s/PSet.py' % (dirname), shell=True)
subprocess.call('cd %s' % (dirname), shell=True)
subprocess.call('ln -s $CMSSW_BASE/src/PhysicsTools/NanoAODTools/scripts/haddnano.py .', shell=True)

sublist = []
for aid in ids :
    ARGS.ID = aid
#idname%s = '%s'
    subCommand = '''                                                                                                                                         
print " Submitting CRAB job for dataset : %s "                                                                                              
subprocess.call('crab submit -c crabConfig%s.py' , shell=True)                                                                            
subprocess.call('echo "crab submit -c crabConfig%s.py" ' , shell=True)                                       
#print "As you submit CRAB jobs REMOVE THESE FILES to prevent your space from filling : "

#subprocess.call( 'find ./crab_hists_%s_%s -name "*.tgz"  '   , shell=True)


'''% (aid, aid, aid, ARGS.DATE ,  aid)
 
    sublist.append(subCommand)   
    SUBMIT_SCRIPT += subCommand
#print sublist    

#for s in sublist :
#    SUBMIT_SCRIPT += subCommand

open('%s/crab_submitter_%s_%s.py' % (dirname,ARGS.YEAR,ARGS.DATE), 'w').write(SUBMIT_SCRIPT.format(**ARGS.__dict__))
print "You have successfully created CRAB submit scripts =D"
print "now you need to submit your jobs"
print "get a grid proxy by doing : "
print "voms-proxy-init --voms cms"
print "then cd to the CRABtasks directory and run:"
print "python crab_submitter.py"
print "That script will contain commands to run all of the scripts you just created..."


SUBMIT_SCRIPT = '''                                                                                                                                       
#!/usr/bin/env python                                                                                                                                        
import os, subprocess                                                                                                                                                  
print "Now checking the status of your CRAB jobs"
'''
 
sublist = []
for aid in ids :
    ARGS.ID = aid
#idname%s = '%s'
    subCommand = '''                                                                                                                                                                                                                                    
print " Checking CRAB job status for dataset : %s "

subprocess.call('crab status -d ./crab_{DATE}_%s' , shell=True)                                                                            
subprocess.call('echo "crab status -d  ./crab_{DATE}_%s" ' , shell=True)                                       

#print "As you submit CRAB jobs REMOVE THESE FILES to prevent your space from filling : "

#subprocess.call( 'find ./crab_hists_%s_%s -name "*.tgz"  '   , shell=True)

'''% (aid, aid, aid, ARGS.DATE ,  aid)

    sublist.append(subCommand)
    SUBMIT_SCRIPT += subCommand
#print sublist    

#for s in sublist :
#    SUBMIT_SCRIPT += subCommand
open('%s/crab_status_%s_%s.py' % (dirname,ARGS.YEAR,ARGS.DATE), 'w').write(SUBMIT_SCRIPT.format(**ARGS.__dict__))



SUBMIT_SCRIPT = '''                                                                                                                                       
#!/usr/bin/env python                                                                                                                                        
import os, subprocess                                                                                                                                                  
print "Now checking the status of your CRAB jobs"
'''

sublist = []
for aid in ids :
    ARGS.ID = aid
#idname%s = '%s'
    subCommand = '''                                                                                                                                                                                                                                    
print " Checking CRAB job status for dataset : %s "

subprocess.call('crab resubmit crab_{DATE}_%s' , shell=True)                                                                            
subprocess.call('echo "crab resubmit crab_{DATE}_%s" ' , shell=True)                                       

#print "As you submit CRAB jobs REMOVE THESE FILES to prevent your space from filling : "

#subprocess.call( 'find ./crab_hists_%s_%s -name "*.tgz"  '   , shell=True)

'''% (aid, aid, aid, ARGS.DATE ,  aid)

    sublist.append(subCommand)
    SUBMIT_SCRIPT += subCommand
#print sublist    

#for s in sublist :
#    SUBMIT_SCRIPT += subCommand
open('%s/crab_sub_%s_%s.py' % (dirname,ARGS.YEAR,ARGS.DATE), 'w').write(SUBMIT_SCRIPT.format(**ARGS.__dict__))
