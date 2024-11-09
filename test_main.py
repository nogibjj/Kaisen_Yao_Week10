"""
Test goes here

"""

import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


@pytest.fixture(scope="module")
def spark():
    """Create a test spark session"""
    spark = start_spark("TestApp")
    yield spark
    end_spark(spark)


def test_extract():
    """Test the extract function"""
    try:
        file_path = extract()
        assert os.path.exists(file_path) is True
    except Exception as e:
        print(f"Extract error: {e}")
        assert False


def test_load_data(spark):
    """Test the load data function"""
    try:
        # Make sure we have the data file
        extract()
        df = load_data(spark)
        assert df is not None
    except Exception as e:
        print(f"Load data error: {e}")
        assert False


def test_describe(spark):
    """Test the describe function"""
    df = load_data(spark)
    result = describe(df)
    assert result is None


def test_query(spark):
    """Test the query function"""
    df = load_data(spark)
    result = query(
        spark,
        df,
        """
        SELECT confederation,
               COUNT(*) as country_count,
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        """,
        "fifa",
    )
    assert result is None


def test_example_transform(spark):
    """Test the transform function"""
    df = load_data(spark)
    result = example_transform(df)
    assert result is None


if __name__ == "__main__":
    # Create a spark session for manual testing
    test_spark = start_spark("TestApp")
    try:
        test_extract()
        test_load_data(test_spark)
        test_describe(test_spark)
        test_query(test_spark)
        test_example_transform(test_spark)
        print("All tests passed!")
    finally:
        end_spark(test_spark)
