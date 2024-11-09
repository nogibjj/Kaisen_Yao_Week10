"""
Main cli or app entry point for FIFA data analysis
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    """Main function for FIFA data analysis"""

    # extract data from source
    extract()

    # start spark session
    spark = start_spark("FIFA Analysis")

    # load data into dataframe
    df = load_data(spark)

    # get basic statistics
    describe(df)

    # execute example query
    query(
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

    # perform example transformation
    example_transform(df)

    # end spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
