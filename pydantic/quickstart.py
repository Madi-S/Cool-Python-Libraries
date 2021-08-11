from pydantic import BaseModel, ValidationError


class City(BaseModel):
    id: int
    name: str
    population: int


incoming_json = '''
{
    "id": 228,
    "name": "Kokshetau",
    "population": "123492"
}
'''

city = City.parse_raw(incoming_json)
print(city)
print(city.id, city.name, city.population)


invalid_json = '''
{
    "id": 1337,
    "name": "Moscow",
    "population": "16 million"
}
'''

try:
    moscow = City.parse_raw(invalid_json)
    print(moscow)
except ValidationError as e:
    print('Error when parsing city JSON:', e.json())
    # send via `jsonify(e.json())`
