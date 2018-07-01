import utils
import const

# https://openweathermap.org API key
api_key = "adeaa68b9d2f5a100919934788d350e0"

# Position weather station id
city_id_meyrin = "2659667"
city_id_geneva = "2660646"

# Aip return error/success
return_code_limitation = 429
return_code_success = 200

# Weather condition ids
# https://openweathermap.org/weather-conditions
condition_thunderstorm_id = "200"
condition_drizzle_id = "300"
condition_rain_id = "500"
condition_clear_sky_id = "800"
condition_mist_id = "701"
condition_clouds_level_id = {"800": 0, "801": 1, "802": 2, "803": 3, "804": 4}


# Check if it's raining
def is_raining_drizzle(weather_id: str):

    # Prevent error
    if len(weather_id) > 1:

        # Check if rain or drizzle
        # Check the first char eg: condition_rain_id => 500 -> 599 => 5
        if str(weather_id)[0] == condition_thunderstorm_id[0] or str(weather_id)[0] == condition_drizzle_id[0] or str(weather_id)[0] == condition_thunderstorm_id[0]:
            return True
    return False


# Check if the sky is clear
# If cloud
def is_cloudy(weather_id):

    # Check if key exist
    # Check if cloudy or if there is mist
    if str(weather_id) in condition_clouds_level_id:
        cloud_level = condition_clouds_level_id[str(weather_id)]
        if cloud_level == 4:
            return True
    return False


# Check if mist
def is_mist(weather_id):
    if str(weather_id) == condition_mist_id:
        return True
    return False


# Get current weather
def get_api_current_weather():

    # Check if the API return good value
    status, js = utils.http_get_request_json(route_current_weather_coordinates())
    if status:
        if "cod" in js:
            try:
                if int(js['cod']) == return_code_success:
                    return True, js
            except ValueError:
                return False, None
    return False, None


# Get forecast (5 days every 3h)
def get_api_forecast():

    # Check if the API return good value
    status, js = utils.http_get_request_json(route_forecast_coordinates())
    if status:
        if "cod" in js:
            try:
                if int(js['cod']) == return_code_success:
                    return True, js
            except ValueError:
                return False, None
    return False, None


    if int(js['cod']) == return_code_success:
        if status:
            return True, js
        else:
            return False, None
    else:
        return False, None


def get_degree_from_fahrenheit(fahrenheit: float):
    return (fahrenheit - 32) / 1.8


def get_degree_from_kelvin(kelvin: float):
    return kelvin - 273.15


# Openweathermap routes
def route_current_weather_city():
    return f"http://api.openweathermap.org/data/2.5/weather?id={city_id_geneva}&appid={api_key}"


def route_forecast_city():
    return f"http://api.openweathermap.org/data/2.5/forecast?id={city_id_geneva}&appid={api_key}"


def route_current_weather_coordinates():
    return f"http://api.openweathermap.org/data/2.5/weather?lat={str(const.lat)}&lon={str(const.lon)}&appid={api_key}"


def route_forecast_coordinates():
    return f"http://api.openweathermap.org/data/2.5/forecast?lat={str(const.lat)}&lon={str(const.lon)}&appid={api_key}"