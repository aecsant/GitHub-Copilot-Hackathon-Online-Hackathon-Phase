
import requests
import json

# Get the OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

# Define the function to get the weather forecast for a city
def get_weather_forecast(city):
  """Gets the current weather forecast for a city.

  Args:
    city: The name of the city to get the weather forecast for.

  Returns:
    A dictionary containing the weather forecast for the city.
  """

  # Build the URL for the OpenWeatherMap API request
  url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_KEY)

  # Make the API request
  response = requests.get(url)

  # Check the status code of the response
  if response.status_code != 200:
    raise Exception("Error getting weather forecast: {}".format(response.status_code))

  # Parse the JSON response
  data = json.loads(response.content)

  # Return the weather forecast
  return data

# Define the main function
def main():
  # Get the city name from the command line
  city = input("Enter the city name: ")

  # Get the weather forecast for the city
  weather_forecast = get_weather_forecast(city)

  # Print the weather forecast
  print("The weather forecast for {} is:".format(city))
  print(weather_forecast)

# Run the main function
if __name__ == "__main__":
  main()