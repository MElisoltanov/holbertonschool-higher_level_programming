# Projet : API RESTful | Intranet Holberton Toulouse, France

## Introduction

Dans le monde en constante évolution du développement logiciel, comprendre comment communiquer et transférer efficacement des données entre systèmes est essentiel. Ce projet explore le domaine des API RESTful, une pierre angulaire dans le monde des services web. L’architecture REST (Representational State Transfer) est un ensemble de contraintes qui garantit un système de communication évolutif, sans état et pouvant être mis en cache. Cette approche permet une intégration facile des services web, les rendant accessibles à un large éventail d’applications.

### Objectifs d’apprentissage :

1. **Bases de HTTP/HTTPS** : Comprendre les principes fondamentaux du protocole principal du web, comment se déroule le transfert de données, les méthodes impliquées et la différence entre les versions sécurisées et non sécurisées.
2. **Consommation d’API en ligne de commande** : Expérience pratique d’interaction avec des API à l’aide d’outils de base en ligne de commande, posant les bases pour des interactions plus avancées.
3. **Consommation d’API avec Python** : Améliorer vos compétences de récupération de données en utilisant les capacités de Python, permettant un traitement et une manipulation de données plus avancés.
4. **Développement d’API avec http.server** : Comprendre les bases de la création d’une API à partir de zéro en utilisant les modules intégrés de Python, pour poser des bases solides.
5. **Développement d’API avec Flask** : Approfondir le développement d’API avec le framework léger Flask, en se concentrant sur le routage, la gestion des données et l’évolutivité.
6. **Sécurité & Authentification des API** : Aborder l’aspect crucial de la sécurité, comprendre comment protéger le transfert de données et garantir que seuls les accès autorisés sont permis.
7. **Normes & Documentation d’API avec OpenAPI** : Conclure sur l’importance de maintenir une documentation standardisée, garantissant que les API soient utilisables, compréhensibles et maintenables.

### Importance :

À l’ère numérique interconnectée, les API RESTful jouent un rôle central dans l’intégration de différents systèmes. Elles servent d’intermédiaires, traduisant les requêtes en actions compréhensibles, récupérant des données ou déclenchant des procédures. Des plateformes de réseaux sociaux partageant des données avec des agences publicitaires aux systèmes industriels complexes communiquant pour l’automatisation, les API sont omniprésentes.

Développer une solide compréhension de la consommation, du développement, de la sécurisation et de la documentation de ces API vous dote d’un ensemble de compétences cruciales. C’est un mélange de compréhension des subtilités techniques et de la vision globale du design, garantissant une communication fluide et efficace dans le monde numérique.

### Schéma conceptuel d’une API REST

```
+-------+           +-------+           +---------+           +---------+
|       |  Requête  |       |  Traite   |         |  Récupère |         |
|       |   ----->  |       |  -------> |         |  Modifie  |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       | Réponse   |       |  Retour   |         |           |         |
+-------+           +-------+           +---------+           +---------+
    Client            Serveur Web         Serveur API           Base de données
```

**Composants** :

1. **Client** : Le demandeur du service, souvent un navigateur web ou une application.
2. **Serveur Web** : Gère la requête entrante, agit comme intermédiaire avant de la transmettre au serveur API.
3. **Serveur API** : La couche logique qui traite la requête, détermine quelles données ou actions sont nécessaires.
4. **Base de données** : Stocke les données que l’API peut récupérer ou modifier.

**Flux** :

1. Le client envoie une requête HTTP/HTTPS au serveur web.
2. Le serveur web, après routage et équilibrage de charge éventuels, transmet la requête au serveur API.
3. Le serveur API traite la requête, interagit avec la base de données si besoin.
4. Le serveur API retourne la réponse traitée au serveur web.
5. Le serveur web renvoie la réponse HTTP/HTTPS finale au client.

Ce schéma donne une vue d’ensemble du fonctionnement typique de la communication via une API RESTful. Dans des configurations plus simples, le serveur web et le serveur API peuvent être fusionnés. La séparation ici illustre les couches potentielles dans un environnement plus complexe ou évolutif.

---

## Tâches

### 0. Bases de HTTP/HTTPS

#### Contexte :

Le protocole HTTP (Hypertext Transfer Protocol) est la base de la communication de données sur le web. Il permet aux clients web (comme les navigateurs) de communiquer avec les serveurs web. HTTP a évolué et possède un pendant sécurisé appelé HTTPS (HTTP Secure). HTTPS fonctionne comme HTTP mais ajoute une couche de sécurité via le chiffrement SSL/TLS. Cette couche protège les données contre l’écoute et la falsification.

---

#### Objectif :

À la fin de cet exercice, vous devez être capable de :

1. Différencier HTTP et HTTPS.
2. Comprendre le fonctionnement de base et la structure des requêtes et réponses HTTP.
3. Reconnaître et expliquer les méthodes et codes de statut HTTP courants.

---

#### Ressources :

1. [Mozilla Developer Network (MDN) - Vue d’ensemble de HTTP](/rltoken/Vgwnt_j2iSEp7Hw7ENVR2w)
2. [Différence entre HTTP et HTTPS](/rltoken/ZM7mVhUBk2rRPkpsNh56HA)
3. [Liste des codes de statut HTTP](/rltoken/vAPbpS8hUG2BFS4RcGx1WQ)

---

#### Instructions :

1. **Différencier HTTP et HTTPS** :
     - Lisez les ressources fournies pour comprendre les différences entre HTTP et HTTPS.
     - Notez les principales différences, en vous concentrant sur les aspects de sécurité.
     - Optionnel : Utilisez un outil comme Wireshark pour observer le trafic HTTP et HTTPS (avec les autorisations nécessaires).

2. **Comprendre la structure HTTP** :
     - Visitez un site web simple, faites un clic droit et choisissez « Inspecter » ou « Inspecter l’élément ». Allez dans l’onglet « Réseau ».
     - Rechargez la page et observez la première requête. Cliquez dessus. Explorez la section « En-têtes » pour comprendre la structure des requêtes et réponses HTTP : méthodes, chemins, codes de statut, en-têtes, etc.

3. **Explorer les méthodes et codes de statut HTTP** :
     - À partir des ressources, faites une liste d’au moins quatre méthodes HTTP courantes et expliquez leur usage.
     - Faites une autre liste de cinq codes de statut HTTP courants. Pour chaque code, donnez une brève description et un scénario d’utilisation.

---

#### Astuces :

1. HTTP ne chiffre pas ses données, donc toute personne écoutant la communication peut voir le contenu. HTTPS ajoute une couche de chiffrement, rendant le contenu illisible pour les espions.
2. Le « s » dans « https » signifie « sécurisé ». Les sites traitant des données sensibles (banques, emails…) utilisent généralement HTTPS.
3. Chaque code de statut HTTP a un but précis. Ils sont regroupés par leur premier chiffre : `1xx` (information), `2xx` (succès), `3xx` (redirection), `4xx` (erreurs client), `5xx` (erreurs serveur).

---

#### Résultat attendu :

1. Un résumé expliquant les différences entre HTTP et HTTPS.
2. Un schéma ou un aperçu de la structure d’une requête et d’une réponse HTTP.
3. Listes des méthodes et codes de statut HTTP courants avec leur description et cas d’utilisation. Exemple :

     - Méthode : GET, Description : Récupère des données, Cas d’utilisation : Charger une page web ou récupérer des données d’une API.
     - Code : 404, Description : Non trouvé, Scénario : Quand une page ou ressource demandée n’existe pas sur le serveur.

---

### 1. Consommer des données d’une API avec des outils en ligne de commande (curl)

#### Contexte :

`curl` (Client URL) est un outil en ligne de commande permettant de transférer des données vers ou depuis un serveur réseau, via divers protocoles (HTTP, HTTPS, FTP…). Il est largement utilisé pour le débogage, les tests et l’interaction avec des services web RESTful et des API. Maîtriser `curl` permet de prototyper rapidement des requêtes API, diagnostiquer des problèmes serveur, etc., directement depuis le terminal.

---

#### Objectif :

À la fin de cet exercice, vous devez être capable de :

1. Installer et utiliser `curl` en ligne de commande.
2. Construire et exécuter des requêtes API de base avec `curl`, y compris la gestion des en-têtes et l’inspection des résultats.
3. Interpréter les résultats des requêtes API courantes.

---

#### Ressources :

1. [curl - Everything curl](/rltoken/eFoZ3X1pF42IdfyzLC3M3A)
2. [Utiliser cURL pour interagir avec des API HTTP](/rltoken/ieEz_6p00Tv67oobkwYHTA)
3. API publique pour s’exercer : [JSONPlaceholder](/rltoken/Ut3d3Tzd0l_sH0evg3GiMg)

---

#### Instructions :

1. **Installation et utilisation basique de `curl`** :
     - Installez `curl` sur votre système (généralement disponible dans les dépôts Linux/Mac).
     - Vérifiez l’installation avec `curl --version`.
     - Utilisez `curl` pour récupérer le contenu d’une page web, ex : `curl http://example.com`.

2. **Récupérer des données d’une API** :
     - Utilisez `curl` pour obtenir les posts de JSONPlaceholder : `curl https://jsonplaceholder.typicode.com/posts`
     - Observez la sortie (un tableau JSON de posts).

3. **Utiliser les en-têtes et autres options avec `curl`** :
     - Récupérez uniquement les en-têtes avec `curl -I https://jsonplaceholder.typicode.com/posts`.
     - Faites une requête POST : `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`

---

#### Astuces :

1. L’option `-I` de `curl` récupère uniquement les en-têtes de la réponse.
2. L’option `-X` permet de spécifier la méthode HTTP (ex : `-X POST`).
3. L’option `-d` permet d’envoyer des données (souvent avec POST, PUT ou PATCH).
4. Pour formater la sortie JSON, utilisez un outil comme `jq`.

---

#### Résultat attendu :

1. `curl --version` affiche la version installée et les protocoles supportés.
2. Récupérer les posts de JSONPlaceholder affiche un JSON avec les attributs `userId`, `id`, `title`, `body`.
3. Récupérer uniquement les en-têtes affiche les codes de statut et les en-têtes.
4. Une requête POST retourne une réponse simulant la création d’un post (id `101`).

---

### 2. Consommer et traiter des données d’une API avec Python

#### Contexte :

Python, grâce à sa lisibilité et à son vaste écosystème de bibliothèques, est un choix populaire pour interagir avec des services web et des API. La bibliothèque `requests` simplifie la communication HTTP et permet d’envoyer des requêtes HTTP en Python. Une fois les données récupérées, les outils intégrés de Python facilitent leur manipulation.

---

#### Objectif :

À la fin de cet exercice, vous devez être capable de :

1. Utiliser la bibliothèque `requests` pour envoyer des requêtes HTTP et traiter les réponses.
2. Analyser et manipuler des données JSON en Python.
3. Convertir des données structurées dans d’autres formats, ex : CSV.

---

#### Ressources :

1. [Python Requests Library](/rltoken/QCrinim3JezLwyeCsxZVhA)
2. [Travailler avec des données JSON en Python](/rltoken/D18g-Gb-2p9zPrFcLFF1uw)
3. API publique : [JSONPlaceholder](/rltoken/Ut3d3Tzd0l_sH0evg3GiMg)

---

#### Instructions :

1. Si besoin, installez `requests` avec `pip install requests`.
2. Écrivez un script Python de base pour récupérer les posts de JSONPlaceholder avec `requests.get()`.

     - Créez une fonction `fetch_and_print_posts()` qui récupère tous les posts.
         - Affichez le code de statut de la réponse, ex : `Status Code: 200`
         - Si la requête réussit, analysez les données en JSON avec `.json()`.
         - Parcourez les données et affichez les titres de tous les posts.

     - Créez une fonction `fetch_and_save_posts()` qui récupère tous les posts.
         - Si la requête réussit, structurez les données dans une liste de dictionnaires (`id`, `title`, `body`).
         - Utilisez le module `csv` pour écrire ces données dans un fichier `posts.csv`.

Exemple d’utilisation :

```bash
$ cat main_02_requests.py
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()
fetch_and_save_posts()

$ python3 main_02_requests.py 
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
...
```

---

#### Astuces :

1. `requests.get()` retourne un objet Response, avec les propriétés `status_code`, `headers`, et la méthode `json()`.
2. Les compréhensions de liste sont utiles pour transformer les données JSON en liste de dictionnaires.
3. `csv.DictWriter` permet d’écrire facilement des dictionnaires dans un fichier CSV.

---

#### Résultat attendu :

1. Le script affiche un code de statut `200` pour une requête GET réussie.
2. Les titres des posts sont affichés.
3. Un fichier CSV est généré avec les colonnes `id`, `title`, `body`.

---

### 3. Développer une API simple avec Python et le module `http.server`

#### Contexte :

Le module `http.server` de la bibliothèque standard Python fournit des classes de base pour implémenter des serveurs web. Il n’est pas destiné à la production, mais il est utile pour comprendre les bases de la programmation web sans dépendances externes.

---

#### Objectif :

À la fin de cet exercice, vous devez être capable de :

1. Mettre en place un serveur web de base avec `http.server`.
2. Gérer différents types de requêtes HTTP (GET, POST, etc.).
3. Servir des données JSON en réponse à des endpoints spécifiques.

---

#### Ressources :

1. [Documentation Python : http.server — Serveurs HTTP](/rltoken/PancDHec9OiEVMRM-oyk0w)
2. [Exemple simple d’utilisation de http.server](/rltoken/BiyipvyreiKqOAWzWOuamg)

---

#### Instructions :

1. **Mettre en place un serveur HTTP de base** :
     - Utilisez le module `http.server` pour créer un serveur HTTP simple. Créez une sous-classe de `http.server.BaseHTTPRequestHandler`.
     - Implémentez la méthode `do_GET` pour gérer les requêtes GET. Envoyez une réponse texte simple : « Bonjour, ceci est une API simple ! ».
     - Lancez le serveur sur le port 8000 et testez-le via `http://localhost:8000` ou `curl`.

2. **Servir des données JSON** :
     - Modifiez `do_GET` pour servir des données JSON sur l’endpoint `/data`.
     - Retournez : `{"name": "John", "age": 30, "city": "New York"}`
     - Assurez-vous de définir le bon en-tête `Content-Type: application/json`.

3. **Gérer différents endpoints** :
     - Ajoutez un endpoint `/status` qui retourne `OK`.
     - Gérez les erreurs : pour un endpoint non défini, retournez un statut 404 avec un message approprié.

---

#### Astuces :

1. Utilisez `send_response`, `send_header` et `end_headers` pour envoyer les en-têtes HTTP.
2. Pour servir du JSON, convertissez un dictionnaire Python en chaîne JSON avec le module `json`.
3. Utilisez `self.path` pour router les requêtes selon l’URL.

---

#### Résultat attendu :

1. Sur `http://localhost:8000`, le texte : « Bonjour, ceci est une API simple ! ».
2. Sur `/data`, une réponse JSON : `{"name": "John", "age": 30, "city": "New York"}`
3. Sur `/info`, par exemple : `{"version": "1.0", "description": "Une API simple avec http.server"}`
4. Tout autre endpoint non défini retourne un 404 avec « Endpoint not found ».

---

### 4. Développer une API simple avec Python et Flask

#### Contexte :

Flask est un framework web léger pour Python, populaire pour créer des applications web et des API RESTful de petite à moyenne taille. Son approche minimaliste et modulaire en fait un excellent choix pour débuter le développement web sans la complexité de frameworks plus lourds.

---

#### Objectif :

À la fin de cet exercice, vous devez être capable de :

1. Mettre en place une application Flask et lancer un serveur de développement.
2. Définir et gérer des routes avec Flask pour répondre à différents endpoints.
3. Servir des données JSON avec Flask.
4. Comprendre les bases de la gestion des requêtes et des réponses dans Flask.
5. Gérer les requêtes POST pour ajouter de nouvelles données à l’API.

---

#### Ressources :

- [Documentation officielle Flask](/rltoken/lVatvIXp28JXebe-Qms1Gw) (commencez par la section « A Minimal Application »)

---

#### Instructions :

1. **Installer Flask** :
     - `pip install Flask`
     - Créez un fichier Python et importez Flask : `from flask import Flask`
     - Instanciez l’application : `app = Flask(__name__)`

2. **Créer votre premier endpoint** :
     - Définissez une route pour `/` et une fonction associée qui retourne « Bienvenue sur l’API Flask ! ».
     - Lancez le serveur avec : `if __name__ == "__main__": app.run()`
     - Visitez `http://localhost:5000` ou utilisez `curl`.

3. **Servir des données JSON** :
     - Importez `jsonify` : `from flask import jsonify`
     - Créez une route `/data` qui retourne la liste des usernames stockés dans l’API (stockés dans un dictionnaire en mémoire).
     - Exemple : `users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}`

     > **NOTE :** N’incluez pas de données de test lors du push de votre code.

4. **Étendre votre API** :
     - Ajoutez d’autres endpoints :
         - `/status` : retourne `OK`.
         - `/users/<username>` : retourne l’objet complet correspondant au username.

5. **Gérer les requêtes POST** :
     - Importez `request` : `from flask import request`
     - Créez une route `/add_user` acceptant les POST.
         1. Analysez les données JSON reçues.
         2. Ajoutez l’utilisateur au dictionnaire `users` avec `username` comme clé.
         3. Retournez un message de confirmation avec les données de l’utilisateur.

---

#### Tester votre code :

Utilisez la CLI Flask pour lancer le serveur :

```bash
$ flask --app task_04_flask.py run
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

> Utilisez `curl` ou un script Python pour tester votre API.

---

#### Astuces :

1. Les routes Flask sont définies avec le décorateur `@app.route()`.
2. Pour du contenu dynamique, Flask permet d’ajouter des variables dans la route (`<variable_name>`).
3. `jsonify()` transforme un dictionnaire ou une liste Python en réponse JSON.
4. Le serveur de développement Flask recharge automatiquement le code lors des modifications.

---

#### Résultat attendu :

- Accéder à `http://localhost:5000` affiche : `"Bienvenue sur l’API Flask !"`
- Accéder à `/data` retourne la liste des usernames, ex : `["jane", "john"]`
- `/status` retourne : `"OK"`
- `/users/jane` retourne l’objet complet de l’utilisateur `jane`
- `/users/john` idem pour `john`
- Si l’utilisateur n’existe pas : `{"error": "User not found"}`
- POST sur `/add_user` ajoute l’utilisateur et retourne un code 201 avec confirmation et données.
- POST sans username retourne une erreur 400 : `{"error":"Username is required"}`

---

### 5. Sécurité et techniques d’authentification d’API

#### Contexte :

La sécurité des API est primordiale, surtout lorsqu’elles sont exposées à Internet. Les risques incluent l’accès non autorisé, la falsification de données, les attaques par déni de service… Une méthode fondamentale de sécurisation est l’authentification et l’autorisation, pour garantir que seuls les utilisateurs autorisés accèdent à certaines ressources.

---

#### Objectif :

À la fin de cet exercice, vous devez être capable de :

1. Comprendre l’importance de la sécurité des API.
2. Implémenter une authentification basique avec Flask.
3. Mettre en place une authentification par jeton (JWT).
4. Différencier authentification et autorisation.

---

#### Ressources :

1. [Flask-HTTPAuth](/rltoken/88vjjCBJYisW22vWIm1p4A)
2. [Flask-JWT-Extended](/rltoken/-KgyiHhniaqRQMh7WRIItA)
3. [Introduction aux JSON Web Tokens](/rltoken/UOJ__DgwD0OtPKgy_Ox-Pg)

---

#### Instructions :

##### Authentification basique :

1. **Installer Flask-HTTPAuth** :
     - `pip install Flask-HTTPAuth`

2. **Mettre en place l’authentification HTTP basique** :
     - Créez une liste d’utilisateurs et mots de passe hachés.
     - Utilisez `werkzeug.security` pour le hachage et la vérification.

3. **Protéger des routes avec l’authentification basique** :
     - Utilisez le décorateur `@auth.login_required`.

---

##### Authentification par jeton (JWT) :

1. **Installer Flask-JWT-Extended** :
     - `pip install Flask-JWT-Extended`

2. **Mettre en place l’authentification JWT** :
     - Utilisez une clé secrète pour générer/valider les jetons.
     - Créez une route `/login` qui accepte les identifiants et retourne un jeton JWT.

3. **Protéger des routes avec JWT** :
     - Utilisez le décorateur `@jwt_required()`.

4. **Contrôle d’accès par rôle** :
     - Ajoutez des rôles (`admin`, `user`) à vos utilisateurs.
     - Créez des routes accessibles uniquement à certains rôles.
     - Vérifiez que le rôle de l’utilisateur correspond à celui requis.

---

#### Astuces :

- Pour l’authentification basique, stockez les mots de passe avec `generate_password_hash` et vérifiez-les avec `check_password_hash`.
- Ajoutez les rôles dans la charge utile du jeton JWT.
- Utilisez une clé secrète forte pour JWT.
- Utilisez `get_jwt_identity()` pour récupérer les infos utilisateur du jeton.

---

#### Spécifications de l’API :

##### Données utilisateur :

```python
users = {
        "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
        "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
```

##### Endpoints :

1. **Authentification basique** :
     - **Route protégée** :
         - URL : `/basic-protected`
         - Méthode : `GET`
         - Retourne : `"Basic Auth: Access Granted"` si authentification valide.
         - Authentification : Basique

2. **Authentification JWT** :
     - **Login** :
         - URL : `/login`
         - Méthode : `POST`
         - Accepte : JSON avec `username` et `password`
         - Retourne : jeton JWT si identifiants valides

         Exemple requête :

         ```json
         {
                 "username": "user1",
                 "password": "password"
         }
         ```

         Exemple réponse :

         ```json
         {
                 "access_token": "<JWT_TOKEN>"
         }
         ```

     - **Route protégée JWT** :
         - URL : `/jwt-protected`
         - Méthode : `GET`
         - Retourne : `"JWT Auth: Access Granted"` si jeton valide.
         - Authentification : JWT

     - **Route protégée par rôle** :
         - URL : `/admin-only`
         - Méthode : `GET`
         - Retourne : `"Admin Access: Granted"` si l’utilisateur est admin.
         - Authentification : JWT + contrôle de rôle

---

#### Résultat attendu :

1. Accès à `/basic-protected` sans identifiants : `401 Unauthorized`.
2. Accès à `/basic-protected` avec identifiants valides : `"Basic Auth: Access Granted"`.
3. POST `/login` avec identifiants valides : retourne un jeton JWT.
4. Accès à `/jwt-protected` sans ou avec jeton invalide : `401 Unauthorized`.
5. Accès à `/jwt-protected` avec jeton valide : `"JWT Auth: Access Granted"`.
6. Accès à `/admin-only` avec jeton non-admin : `403 Forbidden` + `{"error": "Admin access required"}`
7. Accès à `/admin-only` avec jeton admin : `"Admin Access: Granted"`

---

#### Note importante :

Toutes les erreurs d’authentification doivent retourner un code `401 Unauthorized`, y compris pour jeton manquant, invalide, expiré ou mal formé. Utilisez les décorateurs de Flask-JWT-Extended pour gérer ces erreurs.

Exemple :

```python
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
        return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
        return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
        return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
        return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
        return jsonify({"error": "Fresh token required"}), 401
```
