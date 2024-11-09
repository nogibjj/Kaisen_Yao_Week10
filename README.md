# Kaisen Yao IDS 706 Week 10 - FIFA Data Analysis with PySpark

[![CI](https://github.com/nogibjj/Kaisen_Yao_IDS706_Week10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Kaisen_Yao_IDS706_Week10/actions/workflows/cicd.yml)

## PySpark Data Processing
This project demonstrates the use of PySpark for processing and analyzing FIFA country audience data. The main objectives include performing Spark SQL queries and data transformations to gain insights about global football viewership patterns, confederation distributions, and economic impacts.

### Dataset
The project uses FIFA countries audience dataset from FiveThirtyEight, which includes:
- Country names
- Confederation affiliations  
- Population share
- TV audience share
- GDP weighted share

### Key Features
1. Data extraction from source
2. Basic statistical analysis  
3. Confederation-based grouping and analysis
4. Regional categorization transformation
5. PySpark SQL queries

### Getting Started
1. Open codespaces
2. Wait for environment to be installed
3. Run: `python main.py`
4. Check results in: [Pyspark Output Data/Summary](pyspark_output.md)

### Code Quality
Run these commands to maintain code quality:
1. Format code: `make format`
2. Lint code: `make lint` 
3. Test code: `make test`

### Data Processing Flow
1. **Extract**: Download FIFA dataset using `extract()`
2. **Initialize**: Start Spark session via `start_spark()`
3. **Load**: Load FIFA data into DataFrame using `load_data()`
4. **Analyze**: Generate descriptive statistics via `describe()`
5. **Query**: Execute Spark SQL queries using `query()`
6. **Transform**: Perform regional categorization via `example_transform()`
7. **Cleanup**: End Spark session using `end_spark()`

### Example Output
After running the analysis, you'll get insights such as:
1. Basic statistics about population shares and TV audience distribution
2. Confederation-wise country counts and average GDP shares
3. Regional categorization (Eurasia, Americas, Others)

## References
1. [Python Ruff Template](https://github.com/nogibjj/python-ruff-template)
2. [FiveThirtyEight FIFA Dataset](https://github.com/fivethirtyeight/data/blob/master/fifa)
3. [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)