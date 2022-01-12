import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def use_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    
    while True:
        cities = ['chicago', 'new york city', 'washington'] 
        city = input('\n Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city in cities:
            print('\n {} is the city you will like to see data for'.format(city))
            break
        else:
            print('\n Wrong city selected')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filters = ['month', 'day', 'both', 'none']
        filtersans = input('\n Would you like to filter the data by month, day, both, or not at all? Type !"none" for no time filter.\n').lower()
        if filtersans in filters:
            print('\n The data will be filtered by {}.'.format(filtersans))
            break
        else:
            print('\n Make a correct selection')
    
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('\n What month would you like to use to filter the data? Type "all" for no month filter\n').lower()
        if month in months:
            print('\n Good!!')
            break
        else:
            print('\n Error! Please select months between january - june.')

    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thuursday', 'Friday', 'Saturday', 'Sunday']
        day = input('\n Select the day you will like to use to filter the data Type "All" for no day filter\n').title()
        if day in days:
            print('\nCorrect!!')
            break
        else:
            print('\nError! Please select a day of the week.')
        
        
        
    print('-'*40)
    return city, month, day 


def loading_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
        
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_statistics(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print('The most common month is',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print('The most common day of week is',common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()
    print('The most common Start Hour is', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Commonly Used Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('The most commonly used Start Station is',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print('The most commonly used End Station is',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    common_comb = df['combination'].mode()
    print('The most frequent combination of start station and end station trip is', common_comb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    minute,second = divmod(total_travel,60)
    hour,minute = divmod(minute,60)
    print('The total travel time:{}hours {}minutes {}seconds'.format(hour, minute, second))

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()
    minute,second = divmod(average_travel,60)
    if minute>60:
        hour,minute = divmod(minute,60)
        print('The average travel time:{}hours {}minutes {}seconds'.format(hour, minute, second))
    else:
        print('The average travel time:{}minutes {}seconds'.format(minute, second))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('The user types are:\n', user_types_counts)

    # TO DO: Display counts of gender
    if city == 'chicago'or city == 'new york city':
        gender_count = df['Gender'].value_counts()
        print('\nThe counts of all gender are:\n', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        print('\nThe oldest user was born in the year', earliest_year)
        most_recent_year = int(df['Birth Year'].max())
        print('The youngest user was born in the year', most_recent_year)
        common_year = int(df['Birth Year'].mode())
        print('The common birth year among the users was', common_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
    ''' 
    Displays the data set used for the analysis in steps of five rows based on users input
    
    Args:
    (dataframe) df 
    '''
    df = df.drop(columns = ['combination'], axis=1)
    view_data = input('\n5 rows of raw data is available, would you like to review the data?  yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc :-1])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        

def main():
    while True:
        city, month, day = use_filters()
        df = loading_data(city, month, day)

        time_statistics(df)
        station_statistics(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
	main()
