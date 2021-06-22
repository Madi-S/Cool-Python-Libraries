from pydantic import BaseModel, ValidationError, validator, root_validator


class UserWithoutPassword(BaseModel):
    name: str
    email: str

    @validator('name')
    def name_should_be_concise(cls, v: str) -> str:
        if len(v) >= 30:
            raise ValueError('Error must no more than 30 characters')
        return v

    @root_validator
    def fields_must_be_valid(cls, values):
        # Some validation logic with all values here
        # {'name': 'jack123Dragon', 'email': 'test@email.ru'}
        return values


class User(UserWithoutPassword):
    password: str


incoming_json = '''
{
    "name": "jack123Dragon",
    "email": "test@email.ru",
    "password": "someHash12389fsdlfjsdl12"
}
'''

try:
    user = UserWithoutPassword.parse_raw(incoming_json)
    print(user.json())
    # db.store(User.parse_raw(incoming_json))

except ValidationError as e:
    print(e.json())
