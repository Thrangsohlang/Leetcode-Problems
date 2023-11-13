import pandas as pd

# Create the "Trips" DataFrame
trips_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'client_id': [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
    'driver_id': [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
    'city_id': [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
    'status': ['completed', 'cancelled_by_driver', 'completed', 'cancelled_by_client', 'completed', 'completed', 'completed', 'completed', 'completed', 'cancelled_by_driver'],
    'request_at': ['2013-10-01', '2013-10-01', '2013-10-01', '2013-10-01', '2013-10-02', '2013-10-02', '2013-10-02', '2013-10-03', '2013-10-03', '2013-10-03']
}

trips = pd.DataFrame(trips_data)

# Create the "Users" DataFrame
users_data = {
    'users_id': [1, 2, 3, 4, 10, 11, 12, 13],
    'banned': ['No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No'],
    'role': ['client', 'client', 'client', 'client', 'driver', 'driver', 'driver', 'driver']
}

users = pd.DataFrame(users_data)

#create a function to solve the problem
def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips['request_at'] = trips['request_at'].apply(pd.to_datetime)
    trips = trips[~(trips['request_at'] > '2013-10-03')]
    U = users.loc[users['banned'] == 'Yes', 'users_id'].tolist()

    for i in U:
        trips = trips.loc[(trips['client_id'] != i) & (trips['driver_id'] != i)]

    trips.sort_values(by='request_at', ascending=True, inplace=True)
    e = trips.groupby('request_at')
    t = trips.request_at.unique()

    cancellation = []
    for i in t:
        a = e.get_group(i)
        b = a[a['status'] != 'completed']
        
        if len(a) != 0:
            cancellation.append(round(len(b)/len(a),2))
        else:
            pass
    print(cancellation)
    if len(cancellation) != 0:
      return pd.DataFrame({'Day': t, 'Cancellation Rate': cancellation})
    else:
      return pd.DataFrame({'Day': [], 'Cancellation Rate': []})


print(trips_and_users(trips, users))