from grafo import Grafo
from grafo import guardar_grafo

# Generamos grafo de mallas con 30 nodos
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(5, 6)
guardar_grafo(grafo_malla_30, "malla_30_nodos")

# Generamos grafo de mallas con 100 nodos
grafo_malla_100 = Grafo(dirigido=False)
grafo_malla_100.grafo_malla(10, 10)
guardar_grafo(grafo_malla_100, "malla_100_nodos")

# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "malla_500_nodos")





# Generamos grafo Erdös y Rényi con 30 nodos y 220 aristas
grafo_erdos_30_220 = Grafo(dirigido=False)
grafo_erdos_30_220.grafo_erdos_renyi(30, 220)
guardar_grafo(grafo_erdos_30_220, "erdos_y_renyi_30")

# Generamos grafo Erdös y Rényi con 100 nodos y 450 aristas
grafo_erdos_100_450 = Grafo(dirigido=False)
grafo_erdos_100_450.grafo_erdos_renyi(100, 450)
guardar_grafo(grafo_erdos_100_450, "erdos_y_renyi_100")

# Generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
guardar_grafo(grafo_erdos_500_2500, "erdos_y_renyi_500")




# generamos grafo con modelo de Gilbert 30 nodos y probabilidad 0.4
grafo_gilbert_30_04 = Grafo(dirigido=False)
grafo_gilbert_30_04.grafo_gilbert(30, 0.4)
guardar_grafo(grafo_gilbert_30_04, "gilbert_30")

# generamos grafo con modelo de Gilbert 100 nodos y probabilidad 0.35
grafo_gilbert_100_035 = Grafo(dirigido=False)
grafo_gilbert_100_035.grafo_gilbert(100, 0.35)
guardar_grafo(grafo_gilbert_100_035, "gilbert_100")

# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.01
grafo_gilbert_500_001 = Grafo(dirigido=False)
grafo_gilbert_500_001.grafo_gilbert(500, 0.01)
guardar_grafo(grafo_gilbert_500_001, "gilbert_500")




# generamos grafo con modelo geográfico simple con 30 nodos y r=0.5
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(30, 0.5)
guardar_grafo(grafo_geografico_30_05, "geografico_30")

# generamos grafo con modelo geográfico simple con 100 nodos y r=0.3
grafo_geografico_100_03 = Grafo(dirigido=False)
grafo_geografico_100_03.grafo_geografico(100, 0.3)
guardar_grafo(grafo_geografico_100_03, "geografico_100")
# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.1)
guardar_grafo(grafo_geografico_500_01, "geografico_500")




# generamos grafo con modelo Barabási-Albert con 30 nodos y grado 10
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(30, 10, False, False)
guardar_grafo(grafo_babarasi_30_10, "babarasi_30")

# generamos grafo con modelo Barabási-Albert con 100 nodos y grado 9
grafo_babarasi_100_09 = Grafo(dirigido=False)
grafo_babarasi_100_09.grafo_barabasi_albert(100, 9)
guardar_grafo(grafo_babarasi_100_09, "babarasi_100")

# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 8
grafo_babarasi_500_8 = Grafo(dirigido=False)
grafo_babarasi_500_8.grafo_barabasi_albert(500, 8)
guardar_grafo(grafo_babarasi_500_8, "babarasi_500")




# generamos grafo con modelo Dorogovtsev-Mendes con 30 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30)
guardar_grafo(grafo_dorogovtsev_mendes_30, "dorogovtsev_mendes_30")

# generamos grafo con modelo Dorogovtsev-Mendes con 100 nodos
grafo_dorogovtsev_mendes_100 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_100.dorogovtsev_mendes(100)
guardar_grafo(grafo_dorogovtsev_mendes_100, "dorogovtsev_mendes_100")

# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "dorogovtsev_mendes_500")