import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # df['race'].unique() tipo um select distinct
    race_count = df.groupby('race').size()   #similar a um select race, count(race) group by....

    # What is the average age of men?
    filtro = df['sex'] == 'Male'
    average_age_men = round(df[filtro]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    filtro = df['education'] == 'Bachelors'
    total_education = df['education'].count()
    total_bachelors = df[filtro]['education'].count()

    percentage_bachelors = (total_bachelors / total_education) * 100


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))].count()
    total_higher_education_rich = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].count()

    lower_education = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) == False)].count()
    total_lower_education_rich = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) == False) & (df['salary'] == '>50K')].count()

    # percentage with salary >50K
    higher_education_rich = (total_higher_education_rich['education'] / higher_education['education']) * 100
    lower_education_rich = (total_lower_education_rich['education'] / lower_education['education']) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['hours-per-week'].count()
    num_min_workers_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]['hours-per-week'].count()

    rich_percentage = (num_min_workers_rich / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = ( df[df['salary'] == '>50K']['native-country'].value_counts().idxmax() )
    highest_earning_country_percentage = ( df[df['salary'] == '>50K']['native-country'].value_counts().max() /
                                           df['native-country'].value_counts().max() ) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax())

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation,
        'df': df
    }

