import time
import pandas as pd
import numpy as np

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = validation_check("Which city (chicago, new york city, washington) will you chose?\n", 'city')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = validation_check("Which month(all, january, february, ... , june) will you chose?\n", 'month')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = validation_check("Which day (all, monday, tuesday, ... sunday) will you chose?\n", 'day')


    print('-'*40)
    return city, month, day

def validation_check(input_string, input_type):
    while True:
        get_input = input(input_string).lower()
        try:
            if get_input in cities and input_type == 'city':
                break
            elif get_input in months and input_type == 'month':
                break
            elif get_input in days and input_type == 'day':
                break
            else:
                if input_type == 'city':
                    print("Invalid city!")
                if input_type == 'month':
                    print("Invalid month!")
                if input_type == 'day':
                    print("Invalid day!")
        except ValueError:
            print('Invalid input!, please input a correct value: ')

    return get_input

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
    df = pd.read_csv(CITY_DATA[city])

    # Converting
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting moth to a new column
    df['month'] = df['Start Time'].dt.month

    # Extract day to a new column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is: ', popular_month)

   
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', popular_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_time = df['hour'].mode()[0]
    print('The most common start time: ', popular_start_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station is:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station is:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    group = df.groupby(['Start Station', 'End Station'])
    popular_combination = group.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of start station and end station trip:\n', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time is: {} seconds'.format(total_time))
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Mean travel time is: {} seconds'.format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print(user_counts)
    print()

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth is:', df['Birth Year'].min())
        print('Most recent year of birth is:', df['Birth Year'].max())
        print('Most common year of birth is:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
