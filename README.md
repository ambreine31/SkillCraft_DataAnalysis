# SkillCraft_DataAnalysis
Analyse et development de modèles de prédiction sur le dataset SkillCraft, données des performances de joueurs StarCraft.
Dans notre jupyter notebook nous suivons les recommandations de l'article concernant le traitement des données et essayons 
de répondre à une de leur problématiques: Est ce que les données sur le cycle perception/action (PAC) des joueurs est un bon indicateur de l'expertise?
Nous testons 5 modèles avec et sans les données PAC et nous en concluons que les modèles contenant les donnés PAC sont toujours plus 
performants dans la prédiction de la league d'un joueur.
Dans l'article les chercheurs ont cependant du mal a construire un modèle qui distingue bien des catégories de leagues adjacentes en niveau.
Nous remarquons aussi cela avec nos modèles qui ont des valeurs r2 autour et 0.50. 
Cest pour cela aussi que notre application Flask, qui tente de prédire le niveau d'un joueur a partir de paramètres entrées dans un modèle de 
régression linéaire, n'est pas très performante par rapport aux résultats réels.
