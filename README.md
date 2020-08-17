# Plotting COVID-19 in Virginia
* ## Virginia's public COVID-19 cases dataset

Data sourced from [Virginia Department of Health](https://www.vdh.virginia.gov/coronavirus/) (VDH)--last updated July 30, 2020.

Each row represents the overall count of COVID-19 cases, hospitalizations, deaths for each locality in Virginia by report date since reporting began for this dataset.

Column Name |	Description	| Type
--- | --- | ---
Report Date |	Date when the case, hospitalization, or death is published |	Date & Tim
FIPS |	5-digit code (51XXX) for the locality |	Plain Text
Locality |	Independent city or county in Virginia |	Plain Text
VDH Health District |	Health district name assigned by the Virginia Department of Health. There are 35 health districts in Virginia. |	Plain Text
Total Cases |	Total number of COVID-19 cases |	Number
Hospitalizations |	Total number of COVID-19 hospitalizations |	Number
Deaths |	Total number of COVID-19 deaths |	Number

* ## Population estimate data for Virginia localities

Data sourced from University of Virginia's [Weldon Cooper Center for Public Service Demographics Research Group](https://demographics.coopercenter.org/virginia-population-estimates), published  on January 27, 2020.

Column Name |	Description
--- | ---
FIPS Code |	3-digit code (XXX) for the locality 	 	
Locality | Independent city or county in Virginia
April 1, 2010 Census| Official population, count from the 2010 Census
July 1, 2019 Estimate | Population approximation "based on a variety of observed administrative record data, such as births, deaths, school enrollment, and residential housing construction"
