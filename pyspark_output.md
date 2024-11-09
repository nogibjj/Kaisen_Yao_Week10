The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is query data

The query is 
        SELECT confederation, 
               COUNT(*) as country_count, 
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        

The truncated output is: 

|    | confederation   |   country_count |   avg_gdp_share |
|---:|:----------------|----------------:|----------------:|
|  0 | CAF             |              50 |            0.05 |
|  1 | UEFA            |              46 |            0.85 |
|  2 | AFC             |              43 |            0.73 |
|  3 | CONCACAF        |              30 |            0.53 |
|  4 | OFC             |              12 |            0.01 |
|  5 | CONMEBOL        |              10 |            1.03 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is SELECT * FROM fifa WHERE confederation = 'UEFA' LIMIT 5

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  1 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  2 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  3 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  4 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is SELECT * FROM fifa WHERE confederation = 'UEFA' LIMIT 5

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  1 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  2 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  3 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  4 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is 
        SELECT confederation,
               COUNT(*) as country_count,
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        

The truncated output is: 

|    | confederation   |   country_count |   avg_gdp_share |
|---:|:----------------|----------------:|----------------:|
|  0 | CAF             |              50 |            0.05 |
|  1 | UEFA            |              46 |            0.85 |
|  2 | AFC             |              43 |            0.73 |
|  3 | CONCACAF        |              30 |            0.53 |
|  4 | OFC             |              12 |            0.01 |
|  5 | CONMEBOL        |              10 |            1.03 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is 
        SELECT confederation,
               COUNT(*) as country_count,
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        

The truncated output is: 

|    | confederation   |   country_count |   avg_gdp_share |
|---:|:----------------|----------------:|----------------:|
|  0 | CAF             |              50 |            0.05 |
|  1 | UEFA            |              46 |            0.85 |
|  2 | AFC             |              43 |            0.73 |
|  3 | CONCACAF        |              30 |            0.53 |
|  4 | OFC             |              12 |            0.01 |
|  5 | CONMEBOL        |              10 |            1.03 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is 
        SELECT confederation,
               COUNT(*) as country_count,
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        

The truncated output is: 

|    | confederation   |   country_count |   avg_gdp_share |
|---:|:----------------|----------------:|----------------:|
|  0 | CAF             |              50 |            0.05 |
|  1 | UEFA            |              46 |            0.85 |
|  2 | AFC             |              43 |            0.73 |
|  3 | CONCACAF        |              30 |            0.53 |
|  4 | OFC             |              12 |            0.01 |
|  5 | CONMEBOL        |              10 |            1.03 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is SELECT * FROM fifa WHERE confederation = 'UEFA' LIMIT 5

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  1 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  2 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  3 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  4 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is 
        SELECT confederation,
               COUNT(*) as country_count,
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        

The truncated output is: 

|    | confederation   |   country_count |   avg_gdp_share |
|---:|:----------------|----------------:|----------------:|
|  0 | CAF             |              50 |            0.05 |
|  1 | UEFA            |              46 |            0.85 |
|  2 | AFC             |              43 |            0.73 |
|  3 | CONCACAF        |              30 |            0.53 |
|  4 | OFC             |              12 |            0.01 |
|  5 | CONMEBOL        |              10 |            1.03 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is describe data

The truncated output is: 

|    | summary   | country     | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:----------|:------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | count     | 191         | 191             |         191        |          191        |           191        |
|  1 | mean      |             |                 |           0.522513 |            0.523037 |             0.520419 |
|  2 | stddev    |             |                 |           1.96033  |            1.44953  |             1.45759  |
|  3 | min       | Afghanistan | AFC             |           0        |            0        |             0        |
|  4 | max       | Zimbabwe    | UEFA            |          19.5      |           14.8      |            11.3      |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is query data

The query is 
        SELECT confederation,
               COUNT(*) as country_count,
               ROUND(AVG(gdp_weighted_share), 2) as avg_gdp_share
        FROM fifa
        GROUP BY confederation
        ORDER BY country_count DESC
        

The truncated output is: 

|    | confederation   |   country_count |   avg_gdp_share |
|---:|:----------------|----------------:|----------------:|
|  0 | CAF             |              50 |            0.05 |
|  1 | UEFA            |              46 |            0.85 |
|  2 | AFC             |              43 |            0.73 |
|  3 | CONCACAF        |              30 |            0.53 |
|  4 | OFC             |              12 |            0.01 |
|  5 | CONMEBOL        |              10 |            1.03 |

The operation is load data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 |

The operation is transform data

The truncated output is: 

|    | country        | confederation   |   population_share |   tv_audience_share |   gdp_weighted_share | region_category   |
|---:|:---------------|:----------------|-------------------:|--------------------:|---------------------:|:------------------|
|  0 | United States  | CONCACAF        |                4.5 |                 4.3 |                 11.3 | Americas          |
|  1 | Japan          | AFC             |                1.9 |                 4.9 |                  9.1 | Eurasia           |
|  2 | China          | AFC             |               19.5 |                14.8 |                  7.3 | Eurasia           |
|  3 | Germany        | UEFA            |                1.2 |                 2.9 |                  6.3 | Eurasia           |
|  4 | Brazil         | CONMEBOL        |                2.8 |                 7.1 |                  5.4 | Americas          |
|  5 | United Kingdom | UEFA            |                0.9 |                 2.1 |                  4.2 | Eurasia           |
|  6 | Italy          | UEFA            |                0.9 |                 2.1 |                  4   | Eurasia           |
|  7 | France         | UEFA            |                0.9 |                 2   |                  4   | Eurasia           |
|  8 | Russia         | UEFA            |                2.1 |                 3.1 |                  3.5 | Eurasia           |
|  9 | Spain          | UEFA            |                0.7 |                 1.8 |                  3.1 | Eurasia           |

