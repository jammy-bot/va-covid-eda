# Plotting COVID-19 in Virginia

---
|   VIZ   |


## Objectives
This visual exploration project developed as my geographic home region of south - eastern Virginia experienced a rise in the report of daily COVID-19 cases. I wondered how the numbers compared to other areas, such as the state's capital city of Richmond, which had experience earlier outbreaks.

I decided to investigate the data, using interactive plotting with Plotly Express. This approach would enable me to visualize data for multiple localities on a single figure, with the option to hover or drill - down for greater detail.

## The Dataset
### Virginia's public COVID-19 cases dataset

Data is sourced from the [Virginia Department of Health](https://www.vdh.virginia.gov/coronavirus/) (VDH). The particular copy of the dataset used in this repository was last updated July 30, 2020. VDH is, itself, a robust source of data and visualizations related to this health crisis. Their dataset continues to be updated regularly.

Each row in the dataset represents the overall count of COVID-19 cases, hospitalizations, deaths for each locality in Virginia by report date since reporting began for this dataset.

Column Name |	Description	| Type
--- | --- | ---
Report Date |	Date when the case, hospitalization, or death is published |	Date & Tim
FIPS |	5-digit code (51XXX) for the locality |	Plain Text
Locality |	Independent city or county in Virginia |	Plain Text
VDH Health District |	Health district name assigned by the Virginia Department of Health. There are 35 health districts in Virginia. |	Plain Text
Total Cases |	Total number of COVID-19 cases |	Number
Hospitalizations |	Total number of COVID-19 hospitalizations |	Number
Deaths |	Total number of COVID-19 deaths |	Number

For additional context and insight, I chose to integrate state population data.

### Population estimate data for Virginia localities

Data was sourced from University of Virginia's [Weldon Cooper Center for Public Service Demographics Research Group](https://demographics.coopercenter.org/virginia-population-estimates), published  on January 27, 2020.

Column Name |	Description
--- | ---
FIPS Code |	3-digit code (XXX) for the locality 	 	
Locality | Independent city or county in Virginia
April 1, 2010 Census| Official population, count from the 2010 Census
July 1, 2019 Estimate | Population approximation "based on a variety of observed administrative record data, such as births, deaths, school enrollment, and residential housing construction"

#### Data Preparation

Since data sources used are actively employed in the public presentation of state health information, they are usable as obtained. I read data into Pandas dataframes from CSV files. A few adjustments were required for my purposes:
* Converting and cleaning column names to
* Changing a few data types
* Dropping an unneeded `VDH Health District` feature

#### Visualization / Analysis

---
|   VIZ   |


Thanks to interactive plotting, my first visualization was capable of answering many of my questions. It is easy to see which localities lead the case count and a simple matter to view hover statistics for each line on the plot. Of course, since there are 133 localities, things do get a bit dense in places.

---
|   VIZ   |



I include 3 static plots in matplotlib (with no interactivity necessary), showing the localities with each of the highest total cases, hospitalizations, and deaths related to COVID-19 for the period under analysis. Fairfax far exceeds other localities, in each case. Of the Hampton Roads localities, only Virginia Beach is listed in the 10 for each of the three plots (Chesepeake is also in the top - 10, for hospitalizations).

---
|   VIZ   |



An animated plot of total cases over time, by locality, show Richmond cases seeming most likely to have resulted in death, through mid - July. It was then surpassed by Virginia Beach in both the number of deaths and in the total number of cases.

---
|   VIZ   |



A plot of deaths over time, by locality, indicates that COVID cases were less - likely to receive hospital treatment, in Norfolk, compared to Richmond. As the rate of death appears to slow toward the end of July, for Richmond, it appears to pick up pace in Virginia Beach. Meanwhile, the number of Virginia Beach hospitalizations appear well below that of Richmond.

---
|   VIZ   |



Animated scatter plots show cases growing more rapidly in Richmond at the start of our timeline, with Virginia Beach later overtaking the capital in daily deaths and total cases. While Virginia Beach leads in the number of hospitalizatons, at the beginning of our timeline, it is far surpassed by Richmond from the second week of May through July.

__Adding Population Data__

---
|   VIZ   |
