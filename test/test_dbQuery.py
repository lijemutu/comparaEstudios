import pytest
from src.Models.Products import GetMatchedStudies


def test_products_by_Id():
    studies = GetMatchedStudies(StudyId=100)
    assert len(studies)==2