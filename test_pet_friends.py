from api import PetFriends
from settings import valid_email,valid_password
import pytest
pf = PetFriends()

"""
    Позитивные тест-кейсы.
"""

def test_get_api_key_for_valid_user(email = valid_email,password = valid_password):
    status,result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter = ''):
    _,auth_key = pf.get_api_key(valid_email,valid_password)

    status,result = pf.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(result['pets'])>0
#pet_photo = 'images/mech_voin_molnii_22101.jpg'
def test_add_new_pet(pet_name = 'Барсик1',pet_type = 'Sibirean',pet_age = '3',pet_photo = 'images/1.txt'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(0,auth_key, pet_name, pet_type, pet_age,pet_photo)
    assert status == 200
    assert result['name'] == pet_name

def test_delete_pet( filter = ''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    st,res = pf.get_list_of_pets( auth_key, filter)
    auth_key = {'key': 'bgfb5gnfnd'}
    l = len(res['pets'])
    if l > 0:
        pet_id = res['pets'][0]['id']
        st1,res1 = pf.delete_pet( auth_key, pet_id)
        assert st1 == 200
    else:
        raise Exception("There is no pets")

def test_update_pet_info( filter = '',pet_name = 'Мурзик1',pet_type = 'Angora',pet_age = 5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    st, res = pf.get_list_of_pets(auth_key, filter)
    l = len(res['pets'])
    if l > 0:
        pet_id = res['pets'][0]['id']
        pet_id = 'segwr3lnoi'
        st1, res1 = pf.update_pet_info(auth_key, pet_id,pet_name,pet_type,pet_age)
        q= len(res1)
        assert st1 == 200
        assert res1['name'] == pet_name
    else:
        raise Exception("There is no pets")

def test_add_new_pet_without_photo(pet_name = 'Барсик2',pet_type = 'Sphinx',pet_age = 3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_without_photo(0,auth_key, pet_name, pet_type, pet_age)
    assert status == 200
    assert result['name'] == pet_name

def test_update_pet_photo_info(filter = '',pet_photo = 'images/mech_voin_molnii_22101.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    st, res = pf.get_list_of_pets(auth_key, filter)
    l = len(res['pets'])
    if l > 0:
        pet_id = res['pets'][0]['id']
        status, result = pf.update_pet_photo_info(0,auth_key,pet_id,pet_photo)
        assert status == 200
        assert result['id'] == pet_id
    else:
        raise Exception("There is no pets")

"""
    Негативные тест-кейсы.
"""
def test_get_api_key_for_invalid_user(email = 'paveltsybenko111@yandex.ru',password = 'fgfguiki'):
    status,result = pf.get_api_key(email,password)
    assert status == 403

def test_get_list_of_pets_with_invalid_api_key(filter='',auth_key = {'key':'gwrg6rehet9sdlmf'}):
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403

# В ответе сервер возвращает код статуса - 500
def test_get_list_of_pets_with_wrong_filter():
    _,auth_key = pf.get_api_key(valid_email, valid_password)
    status,result = pf.get_list_of_pets(auth_key, 'not_my_pets')
    assert status == 500

def test_add_new_pet_with_wrong_photo_format(pet_name = 'Termi',pet_type = 'T-1',pet_age = '3',pet_photo = 'images/24L5.gif'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    st,res = pf.post_new_pet(0,auth_key,pet_name ,pet_type,pet_age,pet_photo)
    assert st == 500

def test_add_new_pet_only_with_name(pet_name = 'Termi1',pet_type = 'T-1',pet_age = '3',pet_photo = 'images/24L5.gif'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    st,res = pf.post_new_pet(1,auth_key,pet_name ,pet_type,pet_age,pet_photo)
    assert st == 400

def test_add_new_pet_only_with_type(pet_name = 'Termi1',pet_type = 'T-1',pet_age = '3',pet_photo = 'images/24L5.gif'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    st,res = pf.post_new_pet(2,auth_key,pet_name ,pet_type,pet_age,pet_photo)
    assert st == 400

def test_add_new_pet_without_photo_without_name(pet_name = 'Барсик2',pet_type = 'Sphinx',pet_age = 3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_without_photo(1,auth_key, pet_name, pet_type, pet_age)
    assert status == 400

def test_add_new_pet_without_photo_without_type(pet_name = 'Барсик2',pet_type = 'Sphinx',pet_age = 3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_without_photo(2,auth_key, pet_name, pet_type, pet_age)
    assert status == 400

def test_add_new_pet_without_photo_without_pet_age(pet_name = 'Барсик2',pet_type = 'Sphinx',pet_age = 3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_without_photo(3,auth_key, pet_name, pet_type, pet_age)
    assert status == 400

def test_update_pet_photo_info_no_data(filter = '',pet_photo = 'images/mech_voin_molnii_22101.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    st, res = pf.get_list_of_pets(auth_key, filter)
    l = len(res['pets'])
    if l > 0:
        pet_id = res['pets'][0]['id']
        status, result = pf.update_pet_photo_info(1, auth_key, pet_id, pet_photo)
        assert status == 400
    else:
        raise Exception("There is no pets")






