# Ensemble
set Distributeur;  # Ditributeurs
set Usine;  # Usines

# Parametres
param demande{Distributeur}; # demande par distributeurs
param cf_penurie{Distributeur}; # Cout fixe de pénurie par point de ditribution
param capacite{Usine}; # Capacoté par usine
param distance{Usine, Distributeur}; # distance entre les usines et points de distribution
param cf_livraison; # Cout fixe de livraison
param cv_transport; # Cout variable de transport par km
param prix_vente; # Prix de vente


# Variable de decision
var Ventes{Usine, Distributeur} integer >= 0; # Nombre d'unités livrées entre chaque usine et chaque point de distribution
var Penurie{Distributeur} binary; # 0 ou 1 si la demandeande est pas satisfaite ou pas


# Fonction objective
maximize Profit:
    sum {u in Usine, d in Distributeur} ((prix_vente*Ventes[u,d])-(cf_livraison + (cv_transport*distance[u,d])) * Ventes[u,d]) + sum {d in Distributeur} (Penurie[d] * cf_penurie[d]);

# Contraintes
subject to ContrainteCapacite {u in Usine}:
    sum {d in Distributeur} Ventes[u,d] <= capacite[u];

subject to ContrainteDemande {d in Distributeur}:
    sum {u in Usine} Ventes[u,d] <= demande[d];
    
subject to SatisfactionDemande {d in Distributeur}:
	  1 - (sum {u in Usine} Ventes[u,d] / demande[d]) <= Penurie[d]