from pydantic import BaseModel, ValidationError, Field
from typing import List


class Tag(BaseModel):
    id: int
    name: str


class City(BaseModel):
    id: int
    name: str
    population: int
    tags: List[Tag] = Field(alias='cityTags')


incoming_json = '''
{
    "id": 228,
    "name": "Kokshetau",
    "population": "123492",
    "cityTags": [
        {"id": 232, "name": "low-salary"},
        {"id": 101, "name": "good-environment"}
    ]
}
'''

try:
    city = City.parse_raw(incoming_json)
    tag = city.tags[1]

    print('\n', city.id, city.name, city.population, tag.name)
    print('\n', tag.dict(), tag.json())
    print('\n', city.json(by_alias=True, exclude={'id', 'population'}))

except ValidationError as e:
    print(e.json())
