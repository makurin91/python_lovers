import requests
from faker import Faker

fake = Faker()


def create_user(name):
    url = 'https://reqres.in/api/users'
    body = {
        "name": f"{name}",
        "job": "leader"
    }
    response = requests.post(url=url, json=body)
    print(response.json())
    assert response.status_code == 201, f"Wrong status code {response.status_code}"
    user_id = response.json()['id']
    return name, user_id


def update_user(name, user_id):
    url = f'https://reqres.in/api/users/{user_id}'
    body = {
        "name": f"{name}",
        "job": "qa"
    }
    response = requests.put(url=url, json=body)
    print(response.json())
    assert response.status_code == 200, f"Wrong status code {response.status_code}"
    return user_id

def delete_user(user_id):
    url = f'https://reqres.in/api/users/{user_id}'
    response = requests.delete(url=url)
    # print(response.json())


if __name__ == "__main__":
    my_name = fake.name()
    name, id = create_user(my_name)
    id = update_user(name, id)
    delete_user(id)
