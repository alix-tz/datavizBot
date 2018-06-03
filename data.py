wordlinks = [
    ' ANALYZED VIA',
    ' CONTRASTED WITH',
    ' IN LIGHT OF',
    ' CORRELATED WITH',
    ' IN RELATION TO',
    ' MATCHED WITH',
    ' LINKED TO',
    ' RANKED AGAINST',
    ' MEASURED AGAINST',
    ' EVALUATED BY',
    ' SEEN THROUGH THE PRISM OF'
]

lightbgcolors = [
    '#800000',  # red
    '#003366',  # blue 1
    '#584937',  # gray 1
    '#f79433',  # light orange
    '#468499',  # light blue
    '#003366',  # blue 2
    '#725fdf',  # purple
    '#f9ca33',  # yellow
    '#476f01',  # olive green
    '#008b00',  # green
    '#8b4500',  # brown
    '#5e5e5e',  # gray 2
    '#5f6e44',  # brown-green
    '#ff0033'  # fushia
]

darkbgcolor = [
    '#4D0099',  # purple
    '#20b2aa',  # sea blue
    '#ff0033',  # fushia
    '#00fa9a',  # green-blue
    '#b0e0e6',  # sky blue
    '#ffff00',  # yellow 1
    '#f9ca33',  # yellow 2
    '#ffb733',  # orange
    '#00adff',  # blue
    '#f99372',  # pink
    '#725fdf',  # violet
    '#468499',  # darker blue
    '#ffffcc',  # almost white
    '#ff0033',  # red
    '#994d00',  # brown
    '#cbbeb5',  # gray
]

dataset = {
    '1': {
        'x':[["Year"],[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960]],
        'y':[["Value in hundreds of million US dollars for Belgium and Luxembourg's imports"],[4.3,4.3,4.6,5.1,5.4,5.9,6.5,7.1,6.3,7.0,7.9,8.5,9.0,9.0,0,0,0,0,0,0,0,7.6,7.2,6.9,8.2,8.5,7.5,8.1,8.9,9.9,8.6,6.6,4.5,5.3,6.4,6.2,7.2,9.3,7.7,0,0,0,0,0,0,0,0,0,19.8,0,19.4,25.3,24.4,24.1,25.4,28.3,32.7,34.3,31.3,34.4,39.6]],
        'z':[["Total population in Belgium in hundreds of thousands"],[67,68,69,70,71,72,73,73,74,75,75,75,76,77,77,78,78,77,77,76,76,75,76,76,77,78,78,79,80,80,81,81,82,82,83,83,83,84,84,84,84,83,83,82,83,83,84,85,86,86,86,87,87,88,88,89,89,90,91,91,91]],
        'name':"BELGIUM'S NATIONAL ECONOMY",
        'tags':['#Belgique', '#Belgium']
    },
    '2': {
        'x':[["Year"],[1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]],
        'y':[["Rate of unemployed women between age 25 and 49 in France (%)"],[3.68,4.1,4.43,4.45,4.75,5.13,5.95,6.3,6.4,7.15,7.8,8.3,9.1,9.25,9.1,8.73,8.78,9.6,10.15,10.83,10.43,10.8,10.88,10.75,10.48,9.28,8.53,8.1,8.65,8.85,8.83,8.45,7.6,7.03,8.2,8.35,8.58,8.93,9.18,9.23,9.15,9.05,8.78]],
        'z':[["Rate of unemployed men and women from age 15 in France (%)"],[3.3,3.63,4.1,4.28,4.78,5.1,6.03,6.58,6.88,8.05,8.53,8.6,8.73,8.4,7.85,7.63,7.8,8.65,9.65,10.25,9.68,10.13,10.3,9.88,9.58,8.18,7.4,7.53,8.13,8.5,8.5,8.45,7.65,7.08,8.73,8.88,8.83,9.4,9.93,9.93,10.03,9.75,9.1]],
        'name':"UNEMPLOYMENT RATES IN FRANCE",
        'tags':['#chomage', '#unemployment']
    },
    '3': {
        'x':[["Year"],[1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004]],
        'y':[["Homicide with and without firearm in Australia (per 100000 people)"],[1.824,1.836,1.482,1.792,2.139,2.112,1.397,1.435,1.615,1.854,1.398,1.703,1.783,1.764,1.845,1.593,1.965,1.387,1.465,1.618,1.576,1.434,1.565,1.176,1.079,1.361,0.845,1.326,1.034,1.446,1.046,1.211,1.202,1.142,0.91,1.04,1.354,1.471,1.3,1.298,1.399,1.327,1.319,1.525,1.485,1.473,1.345,1.54,1.354,1.501,1.422,1.325,1.382,1.581,1.247,1.521,1.748,1.643,1.871,1.766,1.609,2.021,1.898,1.768,1.802,1.898,1.9,1.899,1.899,1.898,2,1.998,2.002,2.4,1.898,2,1.9,2,1.671,1.609,1.803,1.703,1.738,1.525,1.815,1.647,1.599,1.615,1.523,1.31]],
        'z':[["Suicide with and without firearm in Australia (per 100000 people)"],[13.198,11.673,10.16,9.902,10.514,11.865,11.383,9.569,10.521,11.237,11.786,11.74,11.969,12.329,12.277,14.592,12.672,11.465,11.916,12.37,11.76,11.64,10.547,10.814,11.208,10.398,8.776,8.272,7.132,7.387,7.671,9.806,9.843,9.56,9.775,9.293,9.558,10.641,10.879,10.783,10.282,10.832,12.137,12.263,11.088,10.627,11.84,13.675,15.679,14.508,14.779,13.992,15.069,12.716,12.248,12.401,13.3,12.215,11.315,11.419,10.999,10.717,11.034,11.101,11.601,10.895,11.197,11.703,11.199,11.002,11.604,12.404,13.798,13.302,13.399,12.499,12.7,13.701,13.098,11.7,12.599,13.004,14.699,14.301,13.098,12.301,12.6,11.802,11.1,10.427]],
        'name':"VIOLENT DEATHS IN AUSTRALIA",
        'tags':['#Australia', '#death']
    },
    '4': {
        'x':[["Year"],[1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]],
        'y':[["Extent of ice in North America and Greenland in april (in million km²)"],[14.30,12.16,13.12,14.41,13.61,13.65,13.39,14.19,15.08,11.99,13.03,13.64,14.79,13.27,12.93,14.82,13.62,12.45,13.97,13.03,11.88,12.46,13.47,12.68,12.40,12.78,12.29,12.96,14.41,13.87,14.63,12.23,12.70,12.58,13.09,13.62,13.44,12.52,12.22,12.23,12.94,14.26,13.73,11.02,14.11,12.27,14.81,13.79,12.62,12.43,13.58]],
        'z':[["Extent of ice in North America and Greenland in october (in million km²)"],[8.08,7.43,0,8.68,9.14,9.19,7.78,9.45,8.46,8.51,7.48,7.87,6.36,6.46,8.17,7.41,8.07,7.97,7.97,8.73,6.39,7.20,7.63,7.67,8.35,8.37,7.81,6.93,7.85,9.11,8.45,7.66,7.79,8.26,8.02,9.76,7.78,8.74,7.34,8.57,7.87,7.93,9.46,8.16,7.87,8.78,8.16,8.74,8.73,9.47,9.12]],
        'name':"NORTH AMERICA AND GREENLAND SNOW COVERAGE",
        'tags':['#climate', '#snow']
    },
    '5': {
        'x':[["Year"],[1896,1900,1904,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]],
        'y':[["Winning times for the olympic men's 400m final"],[54.20,49.40,49.20,50.00,48.20,49.60,47.60,47.80,46.20,46.50,46.20,45.90,46.70,44.90,45.10,43.80,44.70,44.30,44.60,44.30,43.90,43.50,43.50,43.85,44.00, 43.75,43.94, 43.03]],
        'z':[["Total of olympic medals won by Great Britain"],[7,30,2,147,41,43,34,20,16,14,23,11,24,20,18,13,18,13,21,37,24,20,15,28,30,47,65,67]],
        'name':"OLYMPIC WINNING TIMES AND MEDAL COUNTS",
        'tags':['#OlympicGames', '#400m', '#GreatBritain']
    },
    '6': {
        'x':[["Year"],[1893,1897,1901,1909,1913,1921,1923,1929,1933,1945,1953,1961,1963,1969,1974,1977,1981,1989,1993,2001,2009,2018]],
        'y':[["POTUS's height (in cm)"],[180,170,178,182,180,183,178,182,189,175,179,185,192,180,183,174,185,180,189,182,185,192]],
        'z':[["POTUS's age at time of election"],[56,54,43,52,57,56,51,55,51,61,63,44,55,56,61,53,70,65,47,55,48,72]],
        'name':"PERSONAL INFORMATION ON PRESIDENT OF THE US",
        'tags':['#POTUS']
    },
    '7': {
        'x':[["Year"],[1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]],
        'y':[["Minimum hourly wage in France (current euros)"],[0.11891,0.11891,0.152449,0.152449,0.152449,0.185226,0.192086,0.192086,0.212209,0.22753,0.244147,0.250016,0.257639,0.275933,0.286604,0.294227,0.306423,0.320143,0.338437,0.469543,0.498508,0.55339,0.600649,0.693643,0.827798,1.029031,1.202823,1.362894,1.533637,1.724198,1.971166,2.254721,2.76695,3.093191,3.472789,3.713658,3.969772,4.103928,4.244181,4.384434,4.55975,4.869222,4.978985,5.192414,5.309799,5.421087,5.637565,5.779342,6.011065,6.131499,6.207724,6.405908,6.67,6.83,7.19,7.61,8.03,8.27,8.44,8.71,8.86,9.0,9.22,9.43]],
        'z':[["Minimum hourly wage in the US (current dollars)"],[0.4,0.75,0.75,0.75,0.75,0.75,0.75,1.0,1.0,1.0,1.0,1.0,1.15,1.15,1.25,1.25,1.25,1.25,1.4,1.6,1.6,1.6,1.6,1.6,1.6,2.1,2.3,2.3,2.65,2.9,3.1,3.35,3.35,3.35,3.35,3.35,3.35,3.35,3.35,3.35,3.35,3.8,4.25,4.25,4.25,4.25,4.25,4.75,5.15,5.15,5.15,5.15,5.15,5.15,5.15,5.15,5.15,5.15,5.85,6.55,7.25,7.25,7.25,7.25]],
        'name':"MINIMUM WAGE IN FRANCE AND IN THE US",
        'tags':['#money', '#MinimumWage']
    },
    '8': {
        'x':[["Year"], [1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]],
        'y':[["Average monthly rainfall in Chile (in mm)"],[58.63,59.21,46.44,64.1,57.4,51.09,49.5,42.33,39.98,47.36,49.31,48.33,55.64,68.85,59.93,48.67,46.78,59.1,58.89,57.77,56.66,55.79,48.43,48.88,51.82,56.45,55.96,50.72,55.2,57.77,48.33,60.85,57.02,52.26,58.23,51.94,57.78,58.4,55.85,61.65,59.72,53.12,48.41,56.49,61.73,53.77,55.67,54.87,56.95,60.6,56.1,43.57,66.22,52.82,55.99,46.31,51.09,51.83,49.78,46.59,53.2,40.84,55.88,42.98,60.17,53.17,51.13,47.67,52.13,51.51,54.29,62.23,53.45,50.54,57.19,54.34,63.14,55.1,58.42,64.68,57.19,61.7,49.11,54.66,54.02,58.7,57.52,43.21,49.63,53.95,54.89,58.12,55.68,54.24,49.82,45.32,62.65,41.85,46.03,55.04,52.65,65.28,48.08,47.96,55.92,60.16,39.57,53.35,51.19,46.06,48.74,48.78,46.21,46.4,50.08]],
        'z':[["Average yearly temperature in Chile (in °C)"],[9.03,8.44,8.37,8.64,8.3,8.22,7.87,8.07,7.88,8.09,8.02,8.45,8.55,8.03,8.3,8.35,8.55,8.38,8.84,8.73,8.2,8.44,8.09,8.6,8.42,8.48,8.54,8.31,8.52,8.53,8.24,8.46,8.22,8.04,8.1,8.07,7.92,7.73,8.15,8.14,8.4,8.31,8.72,8.86,8.92,8.36,8.45,8.19,8.37,8.07,8.61,8.82,8.56,8.13,8.04,8.24,8.54,8.51,8.27,8.56,8.1,8.63,8.23,8.08,8.29,8.06,8.06,8.45,8.38,8.2,7.66,8.07,7.92,7.87,7.96,7.86,8.49,8.54,8.39,8.42,8.47,8.45,8.63,7.91,8.54,8.32,8.82,8.13,8.42,8.34,8.16,8.21,8.43,8.45,8.26,8.31,8.71,8.9,8.45,8,8.24,8.09,8.5,8.73,8.32,8.6,7.89,8.66,8.48,8.11,8.43,8.56,8.6,8.47,8.86]],
        'name':"YEARLY AVERAGE WEATHER IN CHILE",
        'tags':['#weather', '#Chile']
    },
    '9':{
        'x':[["Year"],[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998]],
        'y':[["Number of earthquakes per year of magnitude 7.0 or greater"],[13,14,8,10,16,26,32,27,18,32,36,24,22,23,22,18,25,21,21,14,8,11,14,23,18,17,19,20,22,19,13,26,13,14,22,24,21,22,26,21,23,24,27,41,31,27,35,26,28,36,39,21,17,22,17,19,15,34,10,15,22,18,15,20,15,22,19,16,30,27,29,23,20,16,21,21,25,16,18,15,18,14,10,15,8,15,6,11,8,7,13,10,23,16,15,25,22,20,16]],
        'z':[["Number of significant volcano eruptions per year"],[4,2,8,1,1,2,1,4,0,2,1,5,2,3,3,0,2,3,2,5,2,0,0,2,1,0,1,2,6,2,4,1,2,3,0,0,1,2,2,2,3,2,0,2,5,0,3,3,3,1,2,4,3,7,3,2,1,4,2,0,1,1,2,7,3,1,4,4,3,2,1,5,2,4,6,3,3,4,3,4,2,4,4,4,2,1,4,3,3,0,5,5,4,5,4,1,4,4,1]],
        'name':"IMPORTANT NATURAL CATASTROPHIES IN THE WORLD",
        'tags':['#volcano', '#earthquake']
    },
    '10':{
        'x':[["Year"],[1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]],
        'y':[["Annual visitor count for Yosemite National Park (in hundreds of thousands)"],[0.054,0.071,0.089,0.132,0.136,0.125,0.109,0.137,0.151,0.335,0.334,0.345,0.335,0.584,0.689,0.915,1.005,1.300,1.059,2.092,2.742,4.904,4.606,4.613,4.586,4.619,4.983,2.961,3.094,3.723,4.312,4.815,4.433,4.666,5.068,5.979,3.198,1.167,1.205,2.906,6.405,7.776,7.459,8.084,8.210,8.584,9.740,9.692,10.080,9.842,11.142,11.387,11.393,10.615,11.504,12.271,15.055,14.734,15.470,16.354,18.171,22.383,22.811,22.913,22.772,23.422,21.903,22.543,22.746,25.374,26.824,23.926,25.693,23.508,24.903,25.169,24.156,24.575,27.385,28.320,28.767,31.523,32.167,33.082,31.249,34.231,38.195,38.396,39.621,39.584,40.462,36.700,36.571,34.936,34.009,33.687,33.619,33.787,32.809,33.041,32.426,35.034,34.315,37.375,39.014,39.514,38.534,36.912,38.826,41.502,50.289]],
        'z':[["Annual visitor count for Mesa Verde National Park (in hundreds of thousands)"],[0.000,0.000,0.001,0.002,0.003,0.002,0.002,0.003,0.005,0.007,0.014,0.022,0.021,0.023,0.029,0.030,0.043,0.052,0.071,0.090,0.114,0.119,0.168,0.145,0.167,0.180,0.158,0.162,0.215,0.218,0.256,0.282,0.309,0.322,0.364,0.424,0.130,0.046,0.056,0.130,0.398,0.530,0.594,0.780,0.882,0.993,1.057,1.361,1.503,1.613,1.868,1.939,2.013,2.174,2.257,2.277,2.622,3.253,3.444,3.783,4.234,4.350,4.498,5.138,5.272,5.185,5.463,4.829,4.454,6.145,6.751,6.637,6.531,4.737,5.393,5.886,6.030,6.041,5.169,6.563,6.589,7.286,7.722,6.000,6.114,6.781,7.421,6.661,6.850,6.638,6.174,6.277,6.046,6.357,4.523,5.134,4.064,4.386,4.468,4.983,5.572,5.411,5.514,5.504,5.597,5.723,4.889,4.602,5.016,5.473,5.835]],
        'name':"AMERICAN NATIONAL PARK VISITOR COUNTS",
        'tags':['#NationalParks', '#Yosemite', '#MesaVerde']
    },
    '11':{
        'x':[["Year"],[1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]],
        'y':[["Number of video game copies sold in the world in tens of million units"],[1.138,3.577,2.886,1.679,5.036,5.394,3.707,2.174,4.722,7.345,4.939,3.223,7.616,4.598,7.917,8.811,19.915,20.098,25.647,25.127,20.156,33.147,39.552,35.785,41.931,45.994,52.104,61.113,67.89,66.73,60.045,51.599,36.354,36.811,33.705,26.444]],
        'z':[["Number of PC video game copies sold in the world in tens of million units"],[0,0,0,0,0,0.003,0,0,0.003,0,0,0,1.269,0,2.86,0.548,1.223,2.18,1.964,2.138,1.809,5.639,5.806,5.503,4.902,6.833,7.751,5.834,4.021,4.006,1.985,3.144,2.19,3.238,2.891,6.026]],
        'name':"VIDEO GAMES GLOBAL SALES",
        'tags':['#videogames']
    }
}