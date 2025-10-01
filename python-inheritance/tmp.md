Explications détaillées du diagramme de packages HBnB

PresentationLayer
- Rôle : C'est la couche qui gère tout ce que voit ou fait l'utilisateur (l'interface, les appels API, etc).
- ServiceAPI : C'est l'interface (API) par laquelle l'utilisateur ou d'autres applications peuvent interagir avec notre appli.
- DisplayUserInfo() : Exemple de fonction qui pourrait afficher les infos d'un utilisateur sur un site ou une appli mobile.
- Note : Cette couche ne contient pas la logique métier, elle transmet juste les demandes.

BusinessLogicLayer
- Rôle : Ici se trouvent toutes les règles de gestion et les objets importants de l'appli.
- ModelClasses : C'est un regroupement des classes principales (modèles) qui décrivent les objets manipulés.
- UserEntity, PlaceEntity, ReviewEntity, AmenityEntity : Chacune représente une "chose" importante du système (utilisateur, logement, avis, équipement).
- ChangeEntities() : Exemple de fonction pour créer, modifier ou supprimer ces objets.
- Note : Cette couche reçoit les demandes de la couche présentation, applique les règles, puis demande à la couche persistance de sauvegarder ou lire les données.

PersistenceLayer
- Rôle : C'est la couche qui dialogue avec la base de données (où sont stockées les infos).
- DatabaseAccess : Interface qui permet d'accéder à la base (lire/écrire).
- ReadData() / WriteData() : Fonctions pour lire ou écrire dans la base.
- Note : Cette couche ne connaît rien à la logique métier : elle stocke et renvoie juste des données.

---

Relations entre les couches

- PresentationLayer --> BusinessLogicLayer :  
    - Utilise le "Facade Pattern" : la couche présentation ne connaît qu’un point d’entrée (la façade) pour la logique métier (c’est plus simple et sécurisé).
- BusinessLogicLayer --> PersistenceLayer :  
    - Fait les opérations de lecture/écriture dans la base via la couche persistance.

---

Résumé pour débutant

- Chaque couche a un rôle bien précis (présentation, logique, stockage).
- Les couches ne discutent qu’avec leur voisine directe (pas de saut d’une couche à l’autre).
- On utilise le "Facade Pattern" pour simplifier l’accès à la logique métier depuis la présentation.