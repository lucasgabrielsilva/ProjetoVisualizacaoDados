import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
 
# Dataset:
Atacante = pd.DataFrame({ 'Posição' : np.repeat('Atacante', 67), 'minutos jogados': (68,
827,
454,
702,
58,
2735,
871,
1103,
580,
913,
2167,
781,
2047,
758,
1060,
219,
35,
2948,
823,
862,
2689,
1641,
1267,
86,
2633,
2396,
1031,
222,
1833,
2536,
1804,
271,
94,
1963,
2816,
2566,
258,
1754,
264,
2244,
577,
45,
159,
1590,
449,
655,
31,
1721,
810,
1867,
2488,
2289,
1793,
1370,
484,
2384,
877,
818,
510,
601,
2252,
2368,
11,
2422,
2378,
728,
818) })
Lateral = pd.DataFrame({ 'Posição' : np.repeat('Lateral', 29), 'minutos jogados': (157,
2828,
1725,
810,
2969,
2773,
1832,
1170,
2208,
1008,
2721,
2072,
360,
2140,
153,
403,
2354,
2701,
308,
1650,
2697,
1367,
2194,
1195,
238,
360,
3049,
3060,
1062) })
Meia = pd.DataFrame({ 'Posição' : np.repeat('Meia', 129), 'minutos jogados': (1730,
2850,
2428,
2726,
1531,
582,
825,
462,
261,
428,
353,
2821,
2290,
3000,
249,
62,
96,
1714,
2750,
1236,
1181,
1657,
208,
543,
961,
2864,
2221,
480,
642,
1970,
841,
2784,
655,
2753,
2183,
1188,
1533,
352,
1503,
2,
93,
1865,
2536,
2508,
766,
125,
282,
1662,
645,
341,
370,
272,
1496,
982,
2172,
2620,
2804,
2644,
1501,
523,
1920,
2522,
1485,
823,
1885,
1909,
2339,
1724,
570,
998,
1107,
1213,
2259,
2666,
1943,
1522,
1611,
158,
1569,
2608,
1895,
1111,
143,
430,
2049,
2424,
1286,
1497,
2328,
1366,
1701,
49,
69,
985,
2777,
609,
681,
2747,
1418,
1633,
143,
688,
2784,
1031,
2494,
914,
1293,
1820,
974,
2428,
1230,
594,
902,
856,
110,
144,
2183,
1522,
2825,
1594,
2603,
1984,
1790,
253,
1347,
1875,
830,
1604,
422)
})
Volante = pd.DataFrame({ 'Posição' : np.repeat('Volante', 15), 'minutos jogados': (1093,
998,
2530,
131,
29,
1001,
1833,
385,
2579,
714,
968,
2621,
91,
3053,
2857) })
Zagueiro = pd.DataFrame({ 'Posição' : np.repeat('Zagueiro', 107), 'minutos jogados': (12,
17,
28,
90,
90,
92,
97,
101,
105,
126,
178,
220,
254,
260,
273,
312,
332,
348,
360,
418,
446,
515,
534,
535,
568,
582,
606,
630,
713,
770,
782,
785,
834,
863,
896,
900,
900,
927,
935,
960,
966,
1005,
1009,
1043,
1060,
1080,
1085,
1103,
1141,
1145,
1260,
1295,
1315,
1322,
1334,
1392,
1430,
1430,
1485,
1488,
1516,
1521,
1557,
1566,
1567,
1571,
1583,
1632,
1696,
1710,
1770,
1771,
1789,
1875,
1935,
1967,
1980,
2037,
2074,
2197,
2203,
2218,
2290,
2295,
2298,
2321,
2347,
2400,
2438,
2440,
2557,
2570,
2584,
2604,
2610,
2650,
2687,
2706,
2744,
2745,
2750,
2773,
2806,
2910,
2921,
2925,
3060) })
df=Zagueiro.append(Lateral).append(Volante).append(Meia).append(Atacante)

# boxplot
ax = sns.boxplot(x='Posição', y='minutos jogados', data=df)
# add stripplot
ax = sns.stripplot(x='Posição', y='minutos jogados', data=df, color="orange", jitter=0.2, size=2.5)

# add title
plt.title("Boxplot de numero de minutos jogados por posição na temporada 2018", loc="left")

# show the graph
plt.show()