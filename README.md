# Correlating-Education-Analytics-with-Demographics-Trends-
Calculating the average life expectancy and years of education of each country from 2015-2017 and  trends between the happiness score and the average years of education for each country in the data.

********************************************************************************************************************************************************************Description of Data

The data in the ‘Average Years of Education.csv’ file holds information about the education of over 150 countries around the world. This information is recorded in average years of education of citizens over the course of years from 1870-2017. This data provides information that could be useful for governments and educational institutions to find the trend of the average years of education over time. The ‘2015-2017 World Happiness Report.csv’ files all hold large amounts of data (for their respective years in 2015-2017) which are quantitative values for demographics in over 150 countries. Some demographics include the average level of happiness and average life expectancy of citizens in a country. This data provides information which can be utilized by governments and businesses to find trends and correlation between different factors. 


********************************************************************************************************************************************************************
Application and Data Structure 

The first application will calculate the average life expectancy and years of education of each country from 2015-2017. This average will then be displayed on a line graph that will present the trend of the average life expectancy and years of education. The use of the application will determine how life expectancy correlates to education. The usage of averaging the data over 3 years will allow for more accurate data resulting in a more accurate analysis. The data structure has the format:

General Ex. : {Country: [[average life expectancy, average years of education], [...], [...] ], Country: …}
Data Ex. : {'Switzerland': [[0.94143, 13.4], [0.86303, 13.4], [0.85813, 13.4]], …}

This data structure is formatted in a way that will allow for feasible mean calculations of the life expectancy and years of education over the 3 years based on the country. Keys in this dictionary are the countries with the values being a list of a list of the 2 values. This differentiate countries’ data and allow for simple iterations through the list to extract data for calculations and graphing. 

The second analysis application will be a triple line graph that will display trends between the happiness score and the average years of education for each country in the data. Each trendline will represent the trend of a year from 2015-2017. The use of this application will be to determine how happiness correlates to years of education and how it differs throughout 3 years. The data structure has the format:

General Ex. :{Year: [[Country, Average happiness level, Average years of education], …] Year: ...}. 
Data Ex. : {2015: [['Switzerland', 7.587, 13.4], ['Iceland', 7.561, 12.2], ['Denmark', 7.527, 12.5], …}

The values of happiness and education can be easily accessed in the dictionary. These values are also stored in a list so that the values can be easily plotted on a graph. All of these lists of data are stored in a list that has a value corresponding to its year which is its key. This creates distinction between the data of the years allowing for 3 trends on the line graph. 


********************************************************************************************************************************************************************
References

Sanchez, F. (n.d.). Average Years of Education.csv, years of world education by country,  Retrieved March 10, 2023. https://www.kaggle.com/datasets/fredericksalazar/average-years-of-schooling-since-1870-2017

Aché, M. (n.d.). 2015 World Happiness Report.csv, World Happiness Report up to 2022, Retrieved March 10, 2023. https://www.kaggle.com/datasets/mathurinache/world-happiness-report?select=2015.csv

Aché, M. (n.d.). 2016 World Happiness Report.csv, World Happiness Report up to 2022, Retrieved March 10, 2023. https://www.kaggle.com/datasets/mathurinache/world-happiness-report?select=2016.csv

Aché, M. (n.d.). 2017 World Happiness Report.csv, World Happiness Report up to 2022, Retrieved March 10, 2023. https://www.kaggle.com/datasets/mathurinache/world-happiness-report?select=2017.csv

