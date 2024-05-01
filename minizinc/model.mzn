enum Distributeur;
enum Usine;

% Parametres
array[Distributeur] of int: demande;

array[Usine] of int: capacite;

float : prix_vente;
float:  cf_livraison;
float:  cv_transport;

array[Usine, Distributeur] of float: distance ;

array[Distributeur] of float: cf_penurie;


% VARIABLES DÉCISIONS
array[Usine, Distributeur] of var 0..100000000: Ventes;
array[Distributeur] of var 0..1: Penurie;

% FONCTION OBJ
var float: Profit = sum(u in Usine, d in Distributeur) (
    (prix_vente * Ventes[u,d]) - (cf_livraison + cv_transport * distance[u,d]) * Ventes[u,d]) - sum(d in Distributeur) (Penurie[d] * cf_penurie[d]);

% CONTRAINTES
constraint forall(u in Usine) (
    sum(d in Distributeur) (Ventes[u,d]) <= capacite[u]);

constraint forall(d in Distributeur) (
    sum(u in Usine) (Ventes[u,d]) <= demande[d]);

constraint forall(d in Distributeur) (
    1 - (sum(u in Usine) (Ventes[u,d]) / demande[d]) <= Penurie[d]);

% SOLVE
solve maximize Profit;

% RÉSULTATS
output ["Profit = (Profit)\n"] ++
       ["Ventes = (Ventes)\n"] ++
       ["Penurie = (Penurie)\n"];