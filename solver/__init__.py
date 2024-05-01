import time

from problem.distribution_problem import Solution 


class Solver:
    def __init__(self, max_time_sec=10, verbose=1):
        # Initialiser tous les attributs
        self.max_time_sec = max_time_sec
        # Pour contrôler le chronomètre: 
        self._last_run_start = 0 
        self._last_run_end = 0
        # Niveau de détails pour la sortie console.
        # Interprétation:
        #  0: Aucune sortie
        #  1: Sortie minimale
        # 2: Sortie détaillée # >2: Niveau débogage 
        self.verbose = verbose
 

    def _prepare(self): 
        self._last_run_sec = 0
        self._last_run_start = time.time()

    
    def _continue(self):
        elapsedTime = time.time() - self._last_run_start
        if(elapsedTime <= self.max_time_sec):
            return True

        return False


    def _terminate(self):
        # Arrêter le chronomètre et calculer le temps utilisé
        self._last_run_end = time.time()
        self._last_run_sec = self._last_run_end - self._last_run_start


    def solve(self): 
        # Préparer l'exécution
        self._prepare()

        # Boucle d'exécution
        while(self._continue()):
            # TODO Coder la boucle d'exécution ici à la place de 
            pass 
        
        # Finaliser l'exécution
        self._terminate()
        # Retourner une solution
        # TODO Le code ci-dessous est un code temporaire 
        return Solution(0, [], [])
