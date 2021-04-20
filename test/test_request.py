import json
import pytest
from src.request_study import request_salud_digna


def test_salud_digna():
    data = request_salud_digna(save=False)
    assert type(data) is str