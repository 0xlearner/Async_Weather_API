import sys
from datetime import timedelta
import json

import redis

from services.openweather_service import get_report


def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.ConnectionError:
        print("Connection Error!")
        sys.exit(1)


client = redis_connect()


def get_routes_from_cache(key: str) -> str:
    """Data from redis."""

    val = client.get(json.dumps(key))
    return val


def set_routes_to_cache(key: str, value: str) -> bool:
    """Data to redis."""

    state = client.setex(
        json.dumps(key),
        timedelta(hours=24),
        value=json.dumps(value),
    )
    return state


async def route_optima(city: str, state: str, country: str, units=None) -> dict:

    location = {
        "city": city.lower().strip(),
        "state": state,
        "country": country.lower().strip(),
        "units": units,
    }

    # First it looks for the data in redis cache
    in_cache = get_routes_from_cache(key=location)
    # print(data)
    # print(type(data))

    # If cache is found then serves the data from cache
    if in_cache:
        data = json.loads(in_cache.decode("utf-8"))
        print(data)
        print(type(data))
        data_dict = json.loads(data)
        # print(data_dict)
        # print(type(data_dict))
        data_dict["cache"] = True
        return data_dict

    else:
        # If cache is not found then sends request to the OpenWeather API
        data = await get_report(city, state, country, units)

        # This block sets saves the respose to redis and serves it directly
        data["cache"] = False
        data = json.dumps(data)
        state_res = set_routes_to_cache(key=location, value=data)

        if state_res is True:
            return json.loads(data)
        return data
