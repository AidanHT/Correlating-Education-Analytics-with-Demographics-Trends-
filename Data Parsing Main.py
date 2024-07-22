import csv
import glob

def create_country_education_dict(filename): 

    country_education = {} 

    with open(filename, 'r') as file_in:
        file_in.readline() 

        for line in file_in:
            line = line.strip().split(';')
            
            country = line[0]
            year = int(line[2])
            mean_education_years = float(line[3])

            if country not in country_education and year >= 2015: 
                country_education[country] = {} 
                country_education[country][year] = mean_education_years
            elif year >= 2015: 
                country_education[country][year] = mean_education_years
                
    return country_education

def create_education_life_data(file_pointers, edu_dict): 
    
    country_data = {} 

    for filename in file_pointers:

        with open(filename, 'r') as file_in:
            reader = csv.DictReader(file_in)
            
            for line in reader:
                year = int(filename[:4]) 
                country = line['Country']
                health = round(float(line['Health (Life Expectancy)']), 5)

                if country not in country_data and country in edu_dict: 
                    country_data[country] = [] 

                if country in edu_dict:
                    education = edu_dict[country][year] 
                    country_data[country].append([health, education]) 
                    
    return country_data
        

def create_education_happiness_data(file_pointers, edu_dict): 
    
    country_data = {} 

    for filename in file_pointers:

        with open(filename, 'r') as file_in:
            reader = csv.DictReader(file_in)
            
            for line in reader:
                year = int(filename[:4]) 
                country = line['Country']
                happiness_score = round(float(line['Happiness Score']), 5)

                if year not in country_data: 
                    country_data[year] = [] 

                if country in edu_dict:
                    education = edu_dict[country][year] 
                    country_data[year].append([country, happiness_score, education]) 

    return country_data

def main(): 
    file_pointers = glob.glob('2*.csv') 

    country_education_dict = create_country_education_dict('Average Years of Education.csv')
    world_education_life_data = create_education_life_data(file_pointers, country_education_dict)
    world_education_happiness_data = create_education_happiness_data(file_pointers, country_education_dict)

#MAIN 
main()
