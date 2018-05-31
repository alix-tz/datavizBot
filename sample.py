sample = {
    "1": {'x':[1,2,5,9,78,15,355,45,21,65,3,78,54,12, 21],
          'y':[45,78,98,6,45,78,54,78,65,54,5,21,41,63,54],
          'z':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
          'name':'name1'},
    "2": {'x':[45,78,965,878,456,456,653,87,541,20,325,542,652,42,78],
          'y':[4,5,87,96,1,2,42,10,22,32,54,2,45,21,11],
          'z':[5,78,6,45,8,1,9,3,79,5,86,65,4,87,29],
          'name':'name2'},
    "3": {'x':[48,35,65,78,98,65,32,54,21,41,52,84,65,87,36],
          'y':[1,2,3,7,8,9,4,5,6,10,12,13,15,17,18],
          'z': [45,78,9,65,7,2,45,35,87,9,65,3,26,12,45],
          'name':'name3'},
    "4": {'x':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
          'y':[45,54,21,23,65,3,21,45,65,78,98,65,32,12,45],
          'z':[9,78,5,8,6,3,4,8,9,2,1,4,7,5,6],
          'name':'name4'},
    "5": {'x':[98,78,98,87,54,78,98,65,45,78,98,65,45,78,98],
          'y':[88,77,99,44,55,33,66,22,11,44,22,55,66,88,99],
          'z':[55,78,98,65,32,45,7,54,6,98,21,4,5,35,4],
          'name':'name5'},
    "6": {'x':[258,1354,9865,845,2154,5787,965,3125,542,5687,9845,6545,6545,8646,6544],
          'y':[200,112,336,554,889,689,457,887,455,665,998,633,214,578,652],
          'z':[55,220,45,666,68,95,32,45,87,665,212,325,2,5,78],
          'name':'name6'},
    "7": {'x':[45,54,54,54,54,45,45,54,45,54,45,54,45,54,45],
          'y':[21,12,23,12,23,13,21,31,21,32,21,32,12,32,12],
          'z':[11,22,33,55,44,66,88,77,22,33,44,99,11,22,55],
          'name':'name7'},
    "8": {'x':[21,3,54,21,56,89,47,63,5,2,48,10,23,15,88],
          'y':[5,42,78,65,32,14,5,21,4,57,87,56,23,21,58],
          'z':[22,45,78,2,45,6,3,5,7,0,5,8,9,6,3],
          'name':'name8'},
    "9": {'x':[75,21,45,86,313,212,45,214,32,658,123,454,0,321,245],
          'y':[65,32,51,86,154,153,684,548,65,487,321,54,3,548,654],
          'z':[11,24,56,78,98,65,45,78,65,9,12,45,78,35,14],
          'name':'name9'}
}

othersample = {
    "1": {'x':[['xname'],[1,2,5,9,78,15,355,45,21,65,3,78,54,12, 21]],
          'y':[['yname'],[45,78,98,6,45,78,54,78,65,54,5,21,41,63,54]],
          'z':[['zname'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
          'name':'name1'},
    "2": {'x':[['xname'],[45,78,965,878,456,456,653,87,541,20,325,542,652,42,78]],
          'y':[['yname'],[4,5,87,96,1,2,42,10,22,32,54,2,45,21,11]],
          'z':[['zname'],[5,78,6,45,8,1,9,3,79,5,86,65,4,87,29]],
          'name':'name2'},
    "3": {'x':[['xname'],[48,35,65,78,98,65,32,54,21,41,52,84,65,87,36]],
          'y':[['yname'],[1,2,3,7,8,9,4,5,6,10,12,13,15,17,18]],
          'z': [['zname'],[45,78,9,65,7,2,45,35,87,9,65,3,26,12,45]],
          'name':'name3'},
    "4": {'x':[['xname'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
          'y':[['yname'],[45,54,21,23,65,3,21,45,65,78,98,65,32,12,45]],
          'z':[['zname'],[9,78,5,8,6,3,4,8,9,2,1,4,7,5,6]],
          'name':'name4'},
    "5": {'x':[['xname'],[98,78,98,87,54,78,98,65,45,78,98,65,45,78,98]],
          'y':[['yname'],[88,77,99,44,55,33,66,22,11,44,22,55,66,88,99]],
          'z':[['zname'],[55,78,98,65,32,45,7,54,6,98,21,4,5,35,4]],
          'name':'name5'},
    "6": {'x':[['xname'],[258,1354,9865,845,2154,5787,965,3125,542,5687,9845,6545,6545,8646,6544]],
          'y':[['yname'],[200,112,336,554,889,689,457,887,455,665,998,633,214,578,652]],
          'z':[['zname'],[55,220,45,666,68,95,32,45,87,665,212,325,2,5,78]],
          'name':'name6'},
    "7": {'x':[['xname'],[45,54,54,54,54,45,45,54,45,54,45,54,45,54,45]],
          'y':[['yname'],[21,12,23,12,23,13,21,31,21,32,21,32,12,32,12]],
          'z':[['zname'],[11,22,33,55,44,66,88,77,22,33,44,99,11,22,55]],
          'name':'name7'},
    "8": {'x':[['xname'],[21,3,54,21,56,89,47,63,5,2,48,10,23,15,88]],
          'y':[['yname'],[5,42,78,65,32,14,5,21,4,57,87,56,23,21,58]],
          'z':[['zname'],[22,45,78,2,45,6,3,5,7,0,5,8,9,6,3]],
          'name':'name8'},
    "9": {'x':[['xname'],[75,21,45,86,313,212,45,214,32,658,123,454,0,321,245]],
          'y':[['yname'],[65,32,51,86,154,153,684,548,65,487,321,54,3,548,654]],
          'z':[['zname'],[11,24,56,78,98,65,45,78,65,9,12,45,78,35,14]],
          'name':'name9'}
}

finalSample = {
  '1': {'x':[['Year'],[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960]],
        'y':[['Value in million US dollars for Belgium and Luxembourg\'s imports'],[430,429,460,513,537,586,645,708,626,696,785,846,900,895,,,,,,,,760,719,688,821,850,754,808,889,988,861,660,449,534,638,618,716,932,767,,,,,,,,,,1984,,1936,2528,2444,2405,2535,2830,3273,3432,3129,3442,3957]],
        'z':[['Total population in Belgium in tens of thousands'],[672,680,690,700,709,718,726,734,741,748,750,752,759,767,772,776,776,773,766,763,755,750,757,764,771,778,784,790,797,803,808,813,819,823,826,829,832,835,837,839,835,828,825,824,829,834,837,845,856,861,864,868,873,878,882,887,892,899,905,910,912]],
        'name':'Belgium\'s National Economy'},
        
}