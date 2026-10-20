import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

today = datetime.now()
week_ago = today - timedelta(days=7)


# format date in (YYYY-MM-DD); as needed by API
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

#hardcoded url with latitude and longitude for india
url = f"https://api.open-meteo.com/v1/forecast?latitude=23.81&longitude=86.44&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)



# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

#Calculate average temperature
df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2

print(df)

# ----------------------------------------------



# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], 'r-o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], 'b-o', label='Min Temp')
plt.plot(df['date'], df['avg_temp'], 'g-o', label='Avg temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Indian Weather - Past 7 Days')
plt.legend()
plt.grid(True, alpha=0.3)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()


#--------------------------------


#create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# save to csv
df.to_csv('data/india_weather.csv',index=False)
print("Data saved to data/india_weather.csv")