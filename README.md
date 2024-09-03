### **Titre du Projet : Déploiement d'une Application Web avec Docker et Docker Compose**

### **Objectif :**
Apprendre les bases de Docker et Docker Compose en déployant une simple application web multi-conteneurs.

### **Description :**
Dans ce projet, vous allez créer et déployer une application web en deux parties : un backend écrit en Python (Flask) et une base de données MySQL. Vous utiliserez Docker pour containeriser ces deux services et Docker Compose pour orchestrer leur déploiement.

### **Étapes du Projet :**

1. **Création du Backend (Flask) :**
   - Ecrivez un Dockerfile pour containeriser l'application Flask.
  
2. **Configuration de la Base de Données MySQL :**
   - Définissez un service MySQL dans Docker Compose avec un volume persistant pour stocker les données.
   - Assurez-vous que le service Flask se connecte à la base de données MySQL pour stocker et récupérer des informations.

3. **Création du Fichier Docker Compose :**
   - Créez un fichier `docker-compose.yml` pour définir les services Flask et MySQL.
   - Configurez les services pour qu'ils communiquent entre eux via un réseau Docker.

4. **Liaison entre Flask et MySQL :**
   - Modifiez le code Flask pour se connecter à la base de données MySQL, permettant ainsi de stocker et d'afficher des données simples (comme une liste de tâches ou un journal de messages).

5. **Lancement et Test de l'Application :**
   - Utilisez Docker Compose pour démarrer les services et assurez-vous que l'application fonctionne correctement.
   - Testez les fonctionnalités de votre application via votre navigateur ou des outils comme `curl` ou `Postman`.

6. **Documentation :**
   - Rédigez un fichier `README.md` expliquant les étapes pour démarrer l'application, y compris les commandes Docker et Docker Compose utilisées.
   - Incluez des instructions pour ajouter de nouvelles routes à Flask ou pour persister d'autres types de données.

### **Livrables :**
- Un dépôt GitHub contenant le code Flask, le Dockerfile, le fichier `docker-compose.yml` et le fichier `README.md`.

### **Points clés :**
- `/init-db` Route : Cette route initialise la base de données en créant la table messages si elle n'existe pas déjà.
- `/` Route : Cette route vérifie également que la table messages existe avant de tenter de récupérer les données.
- `/add-message` Route : Une route POST qui permet d'ajouter un message à la table messages.
#### **Instructions pour exécuter l'application :**
- Configurer la connexion MySQL : Remplacez localhost, your_username, your_password, et test_db par vos informations de connexion MySQL dans la fonction create_connection.
- Initialiser la base de données : Accédez à la route /init-db pour créer la table messages.
- Tester l'application : Obtenir les messages : Accédez à la route / pour récupérer les messages.

### **Compétences Apprises :**
- Création et utilisation de Dockerfiles.
- Compréhension de Docker Compose pour orchestrer des applications multi-conteneurs.
- Configuration et interaction avec des bases de données dans un environnement containerisé.
- Gestion des volumes pour la persistance des données dans Docker.
