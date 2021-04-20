import json
import pytest
from src.request_study import request_salud_digna,request_laboratorio_medico_polanco


def test_salud_digna():
    data = request_salud_digna(save=False)
    assert type(data) is str

def test_laboratorio_medico_polanco():
    data = request_laboratorio_medico_polanco(save=False)
    assert type(data) is str