import pytest

from utils.funcions import good_time, hide_card, load_json, five_operations, main_function


def test_load_json():
    assert type(load_json()) == list

def test_good_time():
    assert good_time("2019-12-08T22:46:21.935582") == "08-12-2019"
    assert good_time("2018-09-12T21:27:25.241689") == "12-09-2018"

def test_hide_card():
    assert hide_card("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert hide_card("Счет 90424923579946435907") == "Счет **5907"

def test_five_operations(coll):
    assert five_operations(coll) == ['2019-12-08T22:46:21.935582',
                                            '2019-12-07T06:17:14.634890',
                                            '2019-11-19T09:22:25.899614',
                                            '2019-11-13T17:38:04.800051',
                                            '2019-11-05T12:04:13.781725']
