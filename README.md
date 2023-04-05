# World-Bank-Data-on-Climate-Change
#This second assignment will focus on exploring statistics and trends in more detail. You
are expected to produce a two page report conforming to the guidelines set out below.
This time you will be exploring public data from the World Bank, and specically
country-by-country indicators related to climate change: https://data.worldbank.org/
topic/climate-change. There are a range of indicators relevant to climate change, for
example access to electricity, agricultural activity, urban population, etc.
Your goal is to:
• Ingest and manipulate the data using pandas dataframes. Your program should
include a function which takes a lename as argument, reads a dataframe in World-
bank format and returns two dataframes: one with years as columns and one with
countries as columns. Do not forget to clean the transposed dataframe.
• Explore the statistical properties of a few indicators, that are of interest to you, and
cross-compare between individual countries and/or the whole world (you do not
have to do all the countries, just a few will do) and produce appropriate summary
statistics. You can also use aggregated data for regions and other categories. You
are expected to use the .describe() method to explore your data and two other
statistical methods.
• Explore and understand any correlations (or lack of) between indicators (e.g. popu-
lation growth and energy consumption). Does this vary between country, have any
correlations or trends changed with time?
• You are expected to use your initiative and \tell a story" with the data. You should
use appropriate visualisation (hint: time series could be useful) and provide a text
narrative to communicate and explain your ndings. Details of the implementation
and the coding do not belong in such a report. Your boss wants to see results and
interpretation. What are the key ndings?
• You will be assessed on the overall quality of the report, good use of visualisation
tools and good use of the methods and tools available for dataframes. See mark
scheme for details. Good reports often combine information from graphs to draw
conclusions or follow up on insights/questions from one graph with another graph.
Coding quality marks are given for
• Adherence to the PEP-8 guidelines.
• Well structured and commented program following the good programming style
guide. Good use of functions. No spaghetti code please.
• Good use of your repository with repeat commits.
This assignment does intentionally not specify which data sets to choose. Some ideas,
denitely not exhaustive. You may nd more interesting combinations.
• CO2 production vs. GDP (energy eciency)
1
• Arable land vs. land covered by forests (deforestation)
• Electric power consumption, access to electricity, overall energy use and CO2 emis-
sion.
• Agricultural and non-agricultural methane production. How does it link to other
parameters like poverty headcount, energy consumption, access to electricity?
• How does this look for countries in dierent phases of development? Countries in
dierent parts of the world?
• Numbers per capita (e.g., GDP/head) are often useful.
Format guidelines for the report.
• It should be no more than two A4 pages plus a title page (PDF format please) with
1.5 cm margins all around.
• The minimum font size should be 11 pt, with the exception of gure labels, footnotes
and references. Text in graphs should still be large enough to be readable.
• The report should have a clear title and short abstract and an introductory para-
graph explaining the topic.
• The title page should contain:
{ The title.
{ Your name.
{ A short abstract.
{ Link to your github repository. (Please insert it selecting Link from the insert
tab. That makes it clickable.)
{ Links to non-Worldbank data you were using, if applicable.
{ No table of content. No need for a short report.
How to make the most out of two pages?
• The default margin size in Word is larger than 1.5 cm. It can be changed Layout
tab, select Margins.
• You can divide a page into columns in Word: go to the Layout tab. Select Columns
and the number of columns.
• The line spacing can be reduced to 4 pt, but not to less. Design tab, select
Paragraph spacing and Compact.
• Some fonts use less space than others { but do not overdo it.
• You can use portrait or landscape format Layout 􀀀! Orientation. Whatever
works best.
• One can make text 
ow around gures.
2
What data can I use?
Your report needs to use Worldbank data. Additional les can be used (e.g. sales of
electric vehicles not included in the Worldbank data). You can make use of Worldbank
data not included in the collection, of course.
What modules can I use?
• Use of a minimum number of functions from pyplot and statistical tools from the
lecture (numpy, scipy) is expected (see mark sheet).
• Functions from other modules can be used in addition. The lecture material provides
sucient tools for the assignments, but sometimes you'll nd functions in other
modules doing something special.
What to submit?
• PDF le of report. PDFs are preferred because they avoid potential format problems
(dierent defaults on dierent systems). The report should be uploaded as is and
not be wrapped into a zip le or similar.
• Your program as python le. Notebooks are depreciated.
• Do not upload data les. Worldbank les do not need to be referenced. Links to
other data suce.
• Repositories: Repositories are a tool to dierent store versions of programming code.
We expect repeat commits for full marks. Other material can also be committed,
but that is optional. Include your github link in your title page.
