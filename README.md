# Plotting COVID-19 in Virginia Localities

![Histogram rug of hospitalizations per 1,000 population, by locality (excerpt)](/images/histogram-rug.png)
_Histogram rug of hospitalizations per 1,000 population, by locality (excerpt)_

## Overview and Motivation
Effective July 1, 2020, the state of Virginia entered the third phase of the “Forward Virginia” plan to gradually ease restrictions in place for COVID-19. On July 28, additional restrictions were imposed on restaurants and bars in the Hampton Roads area of southeastern Virginia (Schneider, Gregory S. (July 28, 2020). "Virginia governor adds restrictions in Hampton Roads region after surge in Coronavirus cases". The Washington Post. Retrieved July 28, 2020.). This project was inspired out of an interest in comparing the severity of later outbreaks, in southeaster Virginia with the number and proportion of cases in other areas of the state. In other words, in areas where the cases, hospitalizations, or deaths were decreasing, were they higher or lower than in lately restricted areas?

This is project not a predictive analysis, instead serving comparative analysis for a limited subset of relevant data over particular time frames.

## Objectives
To gauge how the Hampton Roads numbers compare to other areas of Virginia, such as the state's capital city of Richmond, this study primarily investigates the data using interactive plotting with Plotly Express. This approach enables visualization of data for multiple localities on a single figure, with the option to hover or drill - down for greater detail (see published notebooks).

## The Dataset
![Plot image of the United States, with Virginia colored red and all other states in light gray with white borders.](/images/va-plot.png)
_Virginia highlighted on a map of the United States._


### Virginia's public COVID-19 cases dataset

Data is sourced from the [Virginia Department of Health](https://www.vdh.virginia.gov/coronavirus/) (VDH). The particular copy of the dataset used in this repository was last updated July 30, 2020. VDH is, itself, a robust source of data and visualizations related to this health crisis. Their dataset continues to be updated regularly.

Each row in the dataset represents the overall count of COVID-19 cases, hospitalizations, deaths for each locality in Virginia by report date since reporting began for this dataset.

Column Name |	Description	| Type
--- | --- | ---
Report Date |	Date when the case, hospitalization, or death is published |	Date & Time
FIPS |	5-digit code (51XXX) for the locality |	Plain Text
Locality |	Independent city or county in Virginia |	Plain Text
VDH Health District |	Health district name assigned by the Virginia Department of Health. There are 35 health districts in Virginia. |	Plain Text
Total Cases |	Total number of COVID-19 cases |	Number
Hospitalizations |	Total number of COVID-19 hospitalizations |	Number
Deaths |	Total number of COVID-19 deaths |	Number

State population data has been integrated, for additional context and insight.

### Population estimate data for Virginia localities

Data was sourced from University of Virginia's [Weldon Cooper Center for Public Service Demographics Research Group](https://demographics.coopercenter.org/virginia-population-estimates), published  on January 27, 2020.

Column Name |	Description
--- | ---
FIPS Code |	3-digit code (XXX) for the locality 	 	
Locality | Independent city or county in Virginia
April 1, 2010 Census| Official population, count from the 2010 Census
July 1, 2019 Estimate | Population approximation "based on a variety of observed administrative record data, such as births, deaths, school enrollment, and residential housing construction"

#### Data Preparation

Since data sources used are actively employed in the public presentation of state health information, they are usable as obtained. Data is read data into Pandas dataframes from CSV files, with a few adjustments required:
* Converting and cleaning column names to
* Changing a few data types
* Dropping an unneeded `VDH Health District` feature

#### Visualization / Analysis

![Cases by Locality](/images/va-viz.png)
_Static capture, from interactive Plotly Express line plot_

Thanks to interactive plotting, the first visualization was capable of answering many of the raised questions (link to interactive version in the [Featured Notebooks](#featured-notebooks) section, below). It is easy to see (in the interactive plot) which localities lead the case count and a simple matter to view hover statistics for each line on the plot. Of course, since there are 133 localities, things do get a bit dense in places.

![Hospitalizations by Locality](/images/static-hosp.png)
Static bar plot of 10  highest locality hospitalization counts



Static plots in matplotlib (with no interactivity necessary), show the localities with each of the highest total cases, hospitalizations, and deaths related to COVID-19 for the period under analysis. Fairfax far exceeds other localities, in each case. Of the Hampton Roads localities, only Virginia Beach is listed in the 10 for each of the three plots (Chesapeake is also in the top - 10, for hospitalizations).

![Total cases over time, by Locality](/images/july-01-total-cases-bar.png)
Static image of animated bar plot, cases by locality


An animated plot of total cases over time, by locality, shows Richmond cases seeming most likely to have resulted in death, through mid - July (link to interactive version in the [Featured Notebooks](#featured-notebooks) section, below). It was then surpassed by Virginia Beach in both the number of deaths and in the total number of cases.

![Select locality deaths, July 30](/images/july-30-deaths-bar.png)
From animated bar plot, deaths by locality, July 30



A plot of deaths over time, by locality, indicates that COVID cases were less - likely to receive hospital treatment, in Norfolk, compared to Richmond (link to interactive version in the [Featured Notebooks](#featured-notebooks) section, below). As the rate of death appears to slow toward the end of July, for Richmond, it appears to pick up pace in Virginia Beach. Meanwhile, the number of Virginia Beach hospitalizations appear well below that of Richmond.

![Select locality deaths, July 01](/images/july-01-scatter.png)
July 01 deaths by locality, from animated scatter plot


Animated scatter plots show cases growing more rapidly in Richmond at the start of our timeline, with Virginia Beach later overtaking the capital in daily deaths and total cases (link to interactive version in the [Featured Notebooks](#featured-notebooks) section, below). While Virginia Beach leads in the number of hospitalizations, at the beginning of our timeline, it is far surpassed by Richmond from the second week of May through July.

__Adding Population Data__

![Select locality deaths, July 01](/images/july-30-scatter-1k-deaths-hosps.png)
July 30 cases & deaths against hospitalizations

Features engineering for the project involved merging dataframes on the Federal Information Processing Standard (FIPS) codes, present in both source datasets. This required additional preparation for population data. A data subset was read into Pandas, county FIPS codes were padded with leading zeros and prepended with the two - digit, Virginia state code. In addition, the codes were converted from floats to integers, unneeded columns and rows were dropped, and column names were cleaned. Finally, the dataframes were merged, the duplicate FIPS code column was removed, and new features were created to reflect each of the statistical columns per 1,000 population.


Additional visualizations include interactive histogram plots (link to interactive version in the [Featured Notebooks](#featured-notebooks) section, below), in which we observe long tails to the right due to both the presence of localities with relatively low populations (making each of their cases more significant as a fraction of population) and to the number of records (daily) for each of those localities. To our original question, regarding comparison of Hampton Roads community pandemic statistics to those of the capital city: visualizations show a significantly greater number of cases in Norfolk and Virginia Beach, by the end of our timeline; however, hospitalizations and deaths in Richmond exceed those of each of the SE Virginia localities, both in raw numbers and per 1,000 of their respective population estimates.


## [Featured Notebooks](#featured-notebooks)

| __Notebook__                    | __Hyperlink__                                                                                                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                             |                                                                                                                                                                                                                  |
| Filename                    | va-covid-OSE.ipynb                                                                                                                                                                                               |
| Description                 | Obtain, scrub, and explore with static plots.                                                                                                                                                                    |
| Repository Location         | notebooks: [va-covid-OSE.ipynb](https://github.com/jammy-bot/va-covid-eda/blob/master/notebooks/va-covid-OSE.ipynb)                                                                                              |
| Interactive Notebook (external) | [On Deepnote](https://deepnote.com/publish/88b331b8-1da7-4162-b03d-d16463702b37-0801ab15-6074-4988-a65a-cba1bb0d7e95) |
|                             |                                                                                                                                                                                                                  |
| __Notebook__                    | __Hyperlink__                                                                                                                                                                                                        |
| Filename                    | va-covid-limited-explore..ipynb                                                                                                                                                                                  |
| Description                 | Explore locality statistics and interactively plot for localities of interest.                                                                                                                                   |
| Repository Location         | notebooks: [va-covid-limited-explore..ipynb](https://github.com/jammy-bot/va-covid-eda/blob/master/notebooks/va-covid-limited-explore..ipynb)                                                                    |
| Interactive Notebook (external) | [On Deepnote](https://deepnote.com/publish/88b331b8-1da7-4162-b03d-d16463702b37-af082b87-366e-4389-9d4c-20348d170836) |
|                             |                                                                                                                                                                                                                  |
| __Notebook__                    | __Hyperlink__                                                                                                                                                                                                        |
| Filename                    | va-covid-merge-explore.ipynb                                                                                                                                                                                     |
| Description                 | Explore against population data.                                                                                                                                                                                 |
| Repository Location         | notebooks: [va-covid-merge-explore.ipynb](https://github.com/jammy-bot/va-covid-eda/blob/master/notebooks/va-covid-merge-explore.ipynb)                                                                          |
| Interactive Notebook (external) | [On Deepnote](https://deepnote.com/publish/88b331b8-1da7-4162-b03d-d16463702b37-fce29a9a-d9e3-4cec-b658-3026702010cc) |
|                             |                                                                                                                                                                                                                  |
| __Notebook__                    | __Hyperlink__                                                                                                                                                                                                        |
| Filename                    | va\_covid\_plots.ipynb                                                                                                                                                                                           |
| Description                 | Single notebook, complete project (pre - notebook segmentation)                                                                                                                                                  |
| Repository Location         | [va\_covid\_plots.ipynb](https://github.com/jammy-bot/va-covid-eda/blob/master/va_covid_plots.ipynb)                                                                                                             |
|                             | not externally published                                                                                                                                                                                         |

## Technologies
* Python
    - Matplotlib
    - Numpy
    - OS
    - Pandas
    - Pickle
    - Plotly Express
* Sqlite3
* Jupyter Notebooks
