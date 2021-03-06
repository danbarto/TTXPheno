import os

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    results_directory   = "/afs/hephy.at/data/rschoefbeck02/TopEFT/results/" #for analysis results and cache files
    tmp_directory       = "/afs/hephy.at/data/rschoefbeck02/TTXPheno_tmp/" #for on-the-fly tmp stuff
    skim_output_directory      = "/afs/hephy.at/data/rschoefbeck02/TTXPheno/skims/" # where you want the flat ntuples to go
    plot_directory      = "/afs/hephy.at/user/r/rschoefbeck/www/TTXPheno/"  # where the plots go

if os.environ['USER'] in ['dspitzbart', 'dspitzba']:
    tmp_directory       = "/afs/hephy.at/data/dspitzbart01/Top_tmp/"
    skim_directory      = "/afs/hephy.at/data/dspitzbart01/TTXPheno/skims/"
    skim_output_directory = "/afs/hephy.at/data/dspitzbart01/TTXPheno/skims/"
    plot_directory      = "/afs/hephy.at/user/d/dspitzbart/www/TTXPheno/"
