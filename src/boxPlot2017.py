import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
 
# Dataset:
Atacante = pd.DataFrame({ 'Posição' : np.repeat('Atacante', 83), 'minutos jogados': (316,
2153,
2189,
27,
2749,
1137,
1745,
2365,
1010,
816,
342,
378,
1885,
1987,
142,
2867,
14,
53,
180,
11,
2001,
2063,
690,
401,
2542,
453,
21,
2560,
1419,
984,
715,
258,
389,
639,
9,
2540,
1279,
45,
148,
2556,
421,
190,
362,
2169,
2246,
1960,
1511,
11,
472,
25,
1075,
317,
55,
2588,
2318,
1775,
1416,
65,
254,
3041,
1838,
1138,
150,
1824,
1801,
77,
523,
502,
2057,
2194,
1075,
2469,
1003,
2,
1281,
488,
2025,
1028,
1645,
2309,
2086,
2757,
1935) })
Lateral = pd.DataFrame({ 'Posição' : np.repeat('Lateral', 35), 'minutos jogados':  (2341,
798,
990,
1067,
1397,
1502,
1051,
543,
1980,
2325,
1547,
1985,
1690,
2623,
2509,
1186,
2249,
1713,
2857,
2664,
696,
1553,
1644,
90,
2057,
2210,
1820,
2545,
961,
1809,
2451,
2114,
752,
1594,
1349) })
Meia = pd.DataFrame({ 'Posição' : np.repeat('Meia', 138), 'minutos jogados': (1525,
2684,
1993,
1084,
395,
732,
882,
53,
89,
125,
974,
1201,
2368,
1801,
1424,
1439,
1920,
960,
8,
1966,
1895,
945,
1309,
806,
124,
853,
2121,
2332,
1366,
1702,
702,
650,
1777,
151,
237,
2419,
2321,
1204,
1948,
922,
1617,
1280,
868,
66,
2157,
2566,
757,
2613,
140,
820,
1574,
326,
2252,
887,
22,
1821,
385,
3035,
1203,
2269,
260,
45,
2441,
2189,
2582,
1004,
36,
270,
2262,
2605,
1058,
90,
2177,
2465,
2435,
1897,
2195,
507,
53,
1223,
176,
2604,
1085,
26,
53,
609,
1868,
777,
1938,
1994,
1,
362,
1564,
2137,
1554,
1,
871,
1848,
2253,
2509,
709,
545,
45,
153,
2828,
1395,
99,
438,
160,
261,
573,
1871,
1435,
967,
1,
637,
2276,
2965,
927,
755,
132,
492,
199,
2677,
2479,
2072,
1060,
1589,
906,
269,
250,
2043,
1073,
629,
1626,
52,
90,
731) 
})
Volante = pd.DataFrame({ 'Posição' : np.repeat('Volante', 20), 'minutos jogados': (298,
702,
833,
1218,
1588,
1704,
1795,
1813,
1841,
1902,
1920,
1949,
2028,
2073,
2234,
2242,
2569,
2700,
2960,
3057) })
Zagueiro = pd.DataFrame({ 'Posição' : np.repeat('Zagueiro', 115), 'minutos jogados': (892,
629,
2881,
459,
2150,
902,
1,
1455,
412,
1350,
528,
1727,
244,
1223,
2169,
1637,
852,
127,
2214,
482,
90,
543,
2020,
1,
374,
1110,
1167,
162,
211,
1325,
2176,
641,
450,
2499,
1411,
334,
128,
374,
1380,
1750,
3,
462,
2616,
1769,
165,
766,
1009,
2076,
1381,
2729,
436,
55,
1406,
2621,
2028,
1138,
2268,
44,
396,
403,
283,
1755,
1179,
880,
174,
1620,
1534,
1325,
1290,
480,
1052,
817,
2015,
526,
779,
1528,
1009,
2250,
1124,
2176,
1490,
760,
1795,
1069,
2961,
1415,
2425,
2616,
2970,
1843,
1503,
907,
2700,
1602,
2547,
3060,
1710,
2880,
2659,
1972,
2176,
1212,
1929,
1270,
2103,
1160,
676,
650,
1069,
2600,
2645,
2366,
2339,
2356,
2700) })
df=Zagueiro.append(Lateral).append(Volante).append(Meia).append(Atacante)

# boxplot
ax = sns.boxplot(x='Posição', y='minutos jogados', data=df)
# add stripplot
ax = sns.stripplot(x='Posição', y='minutos jogados', data=df, color="orange", jitter=0.2, size=2.5)

# add title
plt.title("Boxplot de numero de minutos jogados por posição na temporada 2017", loc="left")

# show the graph
plt.show()