# Воинов Константин, 14  когорта - Дипломный проект, часть 2: Инженер по тестированию плюс
import send_request
def get_track_number_of_order():
    track_number = send_request.post_new_order() # save request due a creating new order
    return track_number.json()["track"] # save track-number

def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = send_request.get_order_info(track_number) #save request's result on getting track-number's info
    assert get_response.status_code == 200 # check that response status code = 200