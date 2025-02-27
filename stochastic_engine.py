# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:59:48 2018

@author: YSu
"""

############################################################################
# HISTORICAL WEATHER AND STREAMFLOW ANALYSIS

# Perform statistical analysis of historical meteorological data
# Note: this script ('calculatte_cov') only needs to be performed once; after
# that stochastic input generation can occur as many times as desired.
#import calculate_cov
############################################################################

############################################################################
# STOCHASTIC WEATHER AND STREAMFLOW GENERATION

# Specify a number of synthetic years to be simulated 
sim_years=200

# Generate synthetic weather (wind speed and temperature) records. 
import synthetic_temps_wind
synthetic_temps_wind.synthetic(sim_years)

# Generate synthetic streamflow records 
import synthetic_streamflows
#############################################################################
#
#############################################################################
# DAILY HYDROPOWER SIMULATION
#
# California Hydropower model (machine learning) 
import CA_hydropower
CA_hydropower.hydro(sim_years)

# Federal Columbia River Power System Model (mass balance in Matlab)
import os
import sys
FCRPS_Path=os.getcwd() + '\PNW_hydro\FCRPS'
Streamflow_Path = os.getcwd() + '\Synthetic_streamflows'
sys.path.append(FCRPS_Path)
sys.path.append(Streamflow_Path)
import Run_Matlab_Script

# Willamette US Army Corps of Engineers Hydropower model (mass balance)



# Zonal calculation of daily hydro
import PNW_hydro

#############################################################################
#
#############################################################################
## HOURLY WIND AND SOLAR POWER PRODUCTION
#
## WIND
# Specify installed capacity of wind power for each zone
PNW_cap = 6445
CAISO_cap = 4915

# Generate synthetic hourly wind power production time series for the BPA and
# CAISO zones for the entire simulation period
import wind_speed2_wind_power
wind_speed2_wind_power.wind_sim(sim_years,PNW_cap,CAISO_cap)

# SOLAR
# Specify installed capacity of wind power for each zone
CAISO_solar_cap = 9890

# Generate synthetic hourly solar power production time series for 
# the CAISO zone for the entire simulation period
import synthetic_solar
synthetic_solar.solar_sim(sim_years,CAISO_solar_cap)
##############################################################################
#
##############################################################################
# ELECTRICITY DEMAND AND TRANSMISSION PATH FLOWS

# Calculate daily peak and hourly electricity demand for each zone and daily 
# flows of electricity along each WECC path that exchanges electricity between
# core UC/ED model (CAISO, Mid-C markets) and other WECC zones

# NOTE: NEED TO ACCOUNT FOR PNW DEMAND CALCULATION IN FOLLOWING SCRIPT

import demand_pathflows
##############################################################################
#
##############################################################################
# NATURAL GAS PRICES

# NOTE: NEED SCRIPT HERE TO SIMULATE STOCHASTIC NATURAL GAS PRICES 
# *OR*
# ESTIMATE STATIC GAS PRICES FOR EACH ZONE

import numpy as np
ng = np.ones((sim_years*365,5))
ng[:,0] = ng[:,0]*4.47
ng[:,1] = ng[:,1]*4.47
ng[:,2] = ng[:,2]*4.66
ng[:,3] = ng[:,3]*4.66
ng[:,4] = ng[:,4]*5.13

import pandas as pd
NG = pd.DataFrame(ng)
NG.columns = ['SCE','SDGE','PGE_valley','PGE_bay','PNW']
NG.to_excel('Gas_prices/NG.xlsx')


##############################################################################





