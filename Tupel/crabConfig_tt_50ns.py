from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'test2_50ns_20160509_centralpowheg10'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'simple_run_76X_cfg.py'
#config.JobType.scriptExe = 'job_crab.sh'
#config.JobType.outputFiles=['events_presys.lhe']
config.JobType.inputFiles = ['Summer15_25nsV7_DATA.db','Summer15_25nsV7_MC.db','Summer15_25nsV7_DATA_Uncertainty_AK4PFchs.txt']

config.section_("Data")

config.Data.inputDataset = '/TT_TuneEE5C_13TeV-powheg-herwigpp/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
#config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits= -1
#config.Data.outLFN = '/store/caf/user/efe/ntupel/t012j_5f_ckm_NLO_FXFX/crab_seed_4500_' # or '/store/group/<subdir>'
config.Data.outLFNDirBase = '/store/group/phys_top/bbilin/n-tupel/25ns_pf_reduced_20160509/'
config.Data.publication = False
#config.Data.outputDatasetTag = 'TTJets_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9-v2'
config.Data.outputDatasetTag = 'TT_TuneEE5C_13TeV-powheg-herwigpp_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1'
#config.Data.primaryDataset='CRAB_PrivateMC'
config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ["T2_US_Nebraska"]

