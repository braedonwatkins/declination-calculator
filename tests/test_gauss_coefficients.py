from src.modules.gauss_coefficients import gauss_coefficients


def test_gauss_coefficients():
    input_time = 2022.5
    epoch_time = 2020.0

    values = [
        {
            "index": "1_0",
            "g": -29404.5,
            "h": 0.0,
            "g_dot": 6.7,
            "h_dot": 0.0,
        },
        {
            "index": "1_1",
            "g": -1450.7,
            "h": 4652.9,
            "g_dot": 7.7,
            "h_dot": -25.1,
        },
        {
            "index": "2_0",
            "g": -2500.0,
            "h": 0.0,
            "g_dot": -11.5,
            "h_dot": 0.0,
        },
        {
            "index": "2_1",
            "g": 2982.0,
            "h": -2991.6,
            "g_dot": -7.1,
            "h_dot": -30.2,
        },
        {
            "index": "2_2",
            "g": 1676.8,
            "h": -734.8,
            "g_dot": -2.2,
            "h_dot": -23.9,
        },
    ]

    results = [
        {
            "index": "1_0",
            "gt": -29387.75,
            "ht": 0.0,
        },
        {
            "index": "1_1",
            "gt": -1431.45,
            "ht": 4590.15,
        },
        {
            "index": "2_0",
            "gt": -2528.75,
            "ht": 0.0,
        },
        {
            "index": "2_1",
            "gt": 2964.25,
            "ht": -3067.1,
        },
        {
            "index": "2_2",
            "gt": 1671.3,
            "ht": -794.55,
        },
    ]

    for i in range(len(values)):
        gt, ht = gauss_coefficients(
            values[i]["g"],
            values[i]["h"],
            values[i]["g_dot"],
            values[i]["h_dot"],
            input_time,
            epoch_time,
        )

        assert gt == results[i]["gt"] and ht == results[i]["ht"]
