import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"
    def get_api_key(self,email,password):
        headers = {
            'email' : email,
            'password':password

        }

        res = requests.get(self.base_url+'api/key',headers = headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status,result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key':auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets',headers=headers,params=filter)

        status = res.status_code
        result =''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet(self,mode:int, auth_key, name,animal_type,age,pet_photo):

        if mode == 0:
            data1 = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        elif mode == 1:
            data1 = MultipartEncoder(
            fields={
                'name': name
            })
        else:
            data1 = MultipartEncoder(
            fields={
                'animal_type': animal_type
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data1.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data = data1)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        headers = {'auth_key': auth_key['key']}
        s = f'api/pets/{pet_id}'
        res = requests.delete(self.base_url+s,headers=headers)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id,name,animal_type : str,age):
        headers = {'auth_key': auth_key['key']}
        s = f'api/pets/{pet_id}'

        data = {'name':name,'animal_type':animal_type,'age':age}


        res = requests.put(self.base_url + s, headers=headers,data = data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_pet_without_photo(self,mode:int, auth_key, name, animal_type, age):
        if mode == 0:
            data1 = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': str(age)
            })
        elif mode == 1:
            data1 = MultipartEncoder(fields={'animal_type': animal_type,'age': str(age)})
        elif mode == 2:
            data1 = MultipartEncoder(fields={'name': name,'age': str(age)})
        else:
            data1 = MultipartEncoder(fields={'name': name,'animal_type': animal_type})

        headers = {'auth_key': auth_key['key'],'Content-Type': data1.content_type}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data1)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def update_pet_photo_info(self,mode:int, auth_key, pet_id,pet_photo):
        if mode == 0:
            data1 = MultipartEncoder(fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
        else:
            data1 = MultipartEncoder(fields={})
        headers = {'auth_key': auth_key['key'],'Content-Type': data1.content_type}
        s = f'api/pets/set_photo/{pet_id}'
        res = requests.post(self.base_url + s, headers=headers, data=data1)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

