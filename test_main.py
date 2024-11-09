"""
Tests for FIFA data analysis functions
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
    """Fixture for creating and managing Spark session"""
    spark = start_spark("TestFIFA")
    yield spark
    end_spark(spark)


def test_extract():
    """Test data extraction"""
    file_path = extract()
    assert os.path.exists(file_path) is True


def test_load_data(spark):
    """Test data loading"""
    df = load_data(spark)
    assert df is not None
    # Additional test to verify schema
    assert "country" in df.columns
    assert "confederation" in df.columns


def test_describe(spark):
    """Test describe function"""
    df = load_data(spark)
    result = describe(df)
    assert result is None


def test_query(spark):
    """Test query function"""
    df = load_data(spark)
    result = query(
        spark, df, "SELECT * FROM fifa WHERE confederation = 'UEFA' LIMIT 5", "fifa"
    )
    assert result is None


def test_example_transform(spark):
    """Test transformation function"""
    df = load_data(spark)
    result = example_transform(df)
    assert result is None


if __name__ == "__main__":
    """Run tests manually"""
    spark = start_spark("TestFIFA")
    try:
        test_extract()
        test_load_data(spark)
        test_describe(spark)
        test_query(spark)
        test_example_transform(spark)
        print("All tests passed!")
    finally:
        end_spark(spark)
