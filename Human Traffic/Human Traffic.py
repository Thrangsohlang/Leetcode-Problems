import pandas as pd


#Create data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'visit_date': ['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04', '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-09'],
    'people': [10, 109, 150, 99, 145, 1455, 199, 188]
}

stadium = pd.DataFrame(data)

#Defining a function to solve the problem

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium.sort_values(by = 'visit_date',ascending = True, inplace = True)
    stadium['visit_date'] = pd.to_datetime(stadium['visit_date'])
    s = stadium[stadium['people'] >= 100]
    d = []
    count = 1
    for i in range(1,len(s)):
      if (s['id'].iloc[i] == s['id'].iloc[i-1] + 1):
        count += 1
      else:
        count = 1
      
      if count >= 3:
        d.append((s['id'].iloc[i-2], s['visit_date'].iloc[i-2], s['people'].iloc[i-2]))
        d.append((s['id'].iloc[i-1], s['visit_date'].iloc[i-1], s['people'].iloc[i-1]))
        d.append((s['id'].iloc[i], s['visit_date'].iloc[i], s['people'].iloc[i]))
    df = pd.DataFrame(d, columns = ['id', 'visit_date', 'people'])
    df = df.drop_duplicates(subset = ['id'])
    return df