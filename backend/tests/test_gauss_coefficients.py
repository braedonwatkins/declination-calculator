import pytest
from calc.gauss_coefficients import gauss_coefficients


test_data = [
    (
        {"g": -29404.5, "h": 0.0, "g_dot": 6.7, "h_dot": 0.0},
        {"gt": -29387.75, "ht": 0.0},
    ),
    (
        {"g": -1450.7, "h": 4652.9, "g_dot": 7.7, "h_dot": -25.1},
        {"gt": -1431.45, "ht": 4590.15},
    ),
    (
        {"g": -2500.0, "h": 0.0, "g_dot": -11.5, "h_dot": 0.0},
        {"gt": -2528.75, "ht": 0.0},
    ),
    (
        {"g": 2982.0, "h": -2991.6, "g_dot": -7.1, "h_dot": -30.2},
        {"gt": 2964.25, "ht": -3067.1},
    ),
    (
        {"g": 1676.8, "h": -734.8, "g_dot": -2.2, "h_dot": -23.9},
        {"gt": 1671.3, "ht": -794.55},
    ),
]


@pytest.mark.parametrize("inputs, expected", test_data)
def test_gauss_coefficients(inputs, expected):
    input_time = 2022.5
    epoch_time = 2020.0

    gt, ht = gauss_coefficients(
        inputs["g"],
        inputs["h"],
        inputs["g_dot"],
        inputs["h_dot"],
        input_time,
        epoch_time,
    )

    assert gt == expected["gt"]
    assert ht == expected["ht"]
