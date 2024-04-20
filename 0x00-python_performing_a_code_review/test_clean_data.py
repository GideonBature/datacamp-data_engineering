#!/usr/bin/env python3
"""unittest for clean_data.py
"""
# Testing setup
import pytest
import ipytest

ipytest.config.rewrite_asserts = True
__file__ = "notebook.ipynb"

@pytest.fixture()
def clean_smartphone_data():
    return prepare_smartphone_data("./data/smartphones.csv")
    
def test_nan_values(clean_smartphone_data):
    """
    Ensures no NaN values in critical columns.
    """
    
    assert clean_smartphone_data["battery_capacity"].isnull().sum() == 0
    assert clean_smartphone_data["os"].isnull().sum() == 0
    # Update 7: Corrected logical error by ensuring correct assertion syntax for checking NaN values.
