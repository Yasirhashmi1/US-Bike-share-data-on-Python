import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_DATA = ["all","january", "february", "march", "april", "may", "june"]

DAYS_DATA = ['all', 'monday', 'tuesday', 'wedneday', 'thursday', 'friday', 'saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid in 
    city_name = ""
    while city_name.lower() not in CITY_DATA:
        city_name = input('Which of these cities do you want to explore : Chicago, New York city or Washington? \n> ')
        if city_name.lower() in CITY_DATA:
            city= CITY_DATA[city_name.lower()]
        else:
            print('sorry please write a valid city name mentioned above:')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ""
    while month_name.lower() not in MONTHS_DATA:
        month_name = input('What month you would like to explore: all,january,february,march,april,may,june \n>')
        if month_name.lower() in MONTHS_DATA:
            month= month_name.lower()
        else:
            print('sorry, please enter a valid month mentioned above:')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ""
    while day_name.lower() not in DAYS_DATA:
        day_name = input('What day you would like to explore: all, monday, tuesday, wedneday, thursday,friday, saturday,sunday \n>')
        if day_name.lower() in DAYS_DATA:
            day= day_name.lower()
        else:
            print('sorry, please enter a valid day mentioned above:')
    
    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']
        month =  MONTHS.index(month)
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        DAYS = ['all', 'monday', 'tuesday', 'wedneday', 'thursday', 'friday', 'saturday','sunday']
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The month commonly used is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_days = df['day_of_week'].mode()[0]
    print("The day commonly used is :", most_common_days)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The start hours commonly used is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_Start_Station = df['Start Station'].mode()[0]
    print("The most start station used is :", most_Start_Station)


    # TO DO: display most commonly used end station
    most_End_Station = df['End Station'].mode()[0]
    print("The most end station used is :", most_End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Frequent_combination= (df['Start Station'] + df['End Station']).value_counts().idxmax()
    print("The most frequent combination used is :", Frequent_combination.split("||"))
    

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].sum()) / 3600
    total_travel_time = round(total_travel_time, 2)
    print('The total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean()) / 3600
    mean_travel_time = round(mean_travel_time, 2)
    print('The mean travel time is: ', mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types 
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    
    print()
    
    if city == 'chicago.csv' or city =='new_york_city.csv':
    # TO DO: Display counts of gender
        gender =df['Gender'].value_counts
        print(' the gender count is : ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('most earliest birth from the data : ', int(earliest_birth))
        print('most recent birth from the data : ', int(recent_birth))
        print('most common birth from the data : ', int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    """Displays raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        
        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()