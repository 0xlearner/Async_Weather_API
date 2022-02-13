import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# weather_data = dict.fromkeys([loc.city], f"{report}")
# print(weather_data)
# multiple values #
# redis_client.mset(weather_data)
