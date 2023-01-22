import requests
import json

import pytest

url='https://petstore.swagger.io/v2/pet'
header={'accept': 'application/json', 'Content-Type': 'application/json'}
input_pet={
    "id": 24,
    "category": {
      "id": 12,
      "name": "bob"
    },
    "name": "doggie",
    "photoUrls": [
      "string"
    ],
    "tags": [
      {
        "id": 12,
        "name": "Dog"
      }
    ],
    "status": "available"
  }

def test_add_pet():#тест на добавление питомца


  res = requests.post(url=url, headers=header, data=json.dumps(input_pet))
  res_json=json.loads(res.text)
  print(res.text)
  print(res.status_code)
  assert input_pet==res_json


def test_get_pet():# тест на проверку питомца с определенным id

  res = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

  print(res.text)
  print(res.status_code)
  print(type(res.json()))
  assert res.status_code == 200
  assert json.loads(res.text) == input_pet

def test_get_sold_list():#тест на получение списка проданных животных
  input_pet1 = {
    "id": 245,
    "category": {
      "id": 12,
      "name": "boblik"
    },
    "name": "cat",
    "photoUrls": [
      "string"
    ],
    "tags": [
      {
        "id": 12,
        "name": "Dog"
      }
    ],
    "status": "sold"
  }
  requests.post(url=url, headers=header, data=json.dumps(input_pet1))# предусловие, добавляем животное со статусом sold
  res = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'sold'})
  assert res.status_code == 200
  assert input_pet1 in (json.loads(res.text))# проверка заведомо добавленного животного,что он есь в этом списке
  print(list(json.loads(res.text)))
def test_delete_pet():#тест на удаление животного
   res = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
   out_del = {
     "code": 200,
     "type": "unknown",
     "message": "24"
   }
   assert json.loads(res.text) == out_del
   res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
   assert res_get.status_code == 404

def test_put():
    requests.post(url=url, headers=header, data=json.dumps(input_pet))#добавляем удаленное животное обратно
    update_pet = {
        "id": 24,
        "category": {
            "id": 12,
            "name": "murzik"
        },
        "name": "cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    res = requests.put(url=url, headers=header, data=json.dumps(update_pet))# обновляем данные
    res_json = json.loads(res.text)
    print(res.text)
    print(res.status_code)
    assert update_pet == res_json

