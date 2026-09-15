import pandas as pd


def test_sales_file_exists():
    sales = pd.read_csv("data/sample_sales.csv")

    assert len(sales) > 0
    assert "sale_id" in sales.columns
    assert "employee_id" in sales.columns


def test_weather_schema():
    weather = pd.read_json("data/weather.json")

    expected_columns = {
        "date",
        "location",
        "temperature",
        "rainfall"
    }

    assert expected_columns.issubset(set(weather.columns))


def test_changed_weather_schema():
    weather = pd.read_json("data/weather_changed.json")

    # Simulate handling the API change
    weather = weather.rename(
        columns={
            "temp": "temperature",
            "rain": "rainfall"
        }
    )

    assert "temperature" in weather.columns
    assert "rainfall" in weather.columns