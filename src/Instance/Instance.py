class Instance:
    def __init__(self,N_OFs_total,contraintes,OFs,date):
        self.N_OFs_total=N_OFs_total #nombre d'OF admissible a la journee ciblé
        self.contraintes=contraintes
        self.OFs=OFs
        self.date=date