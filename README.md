# Todolist - Application de gestion des tâches
 
Ce projet est une application web de gestion des tâches (todolist) développée avec Django et utilisant Docker pour le déploiement, GitHub Container Registry (GHCR) pour héberger l’image Docker, et une base de données PostgreSQL fournie par Supabase.

## Fonctionnalités principales

- [x] Gestion des tâches : Visualiser, trier et filtrer les tâches sur une interface utilisateur dédiée.
- [x] API REST : Exposer des endpoints pour interagir avec les tâches via une API REST conforme à Django REST Framework.
- [x] Swagger UI : Documentation interactive de l’API accessible via Swagger UI.
- [x] Django : Interface admin pour gérer les tâches et utilisateurs via l’interface admin par défaut de Django.

## Prérequis

Avant de commencer, assurez-vous d’avoir installé les outils suivants sur votre machine :

- [x] Docker
- [x] Docker Compose
- [x] Git
- [x] Une base de données PostgreSQL

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/KevinDeBenedetti/team_todolist.git
cd team_todolist
```

### 2. Configurer la base de données

1.	Configurez une base de données PostgreSQL.
3.	Notez les informations de connexion à la base de données (nom de la base de données, utilisateur, mot de passe, hôte, et port).

### 3. Configuration des variables d’environnement

Créez un fichier .env dans le dossier `backend` du projet et ajoutez-y les variables d’environnement nécessaires pour votre projet, en remplaçant les valeurs avec les informations de votre base de données :

```bash
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=localhost, your-domain.com
CSRF_TRUSTED_ORIGINS=https://your-domain.com
DEFAULT_API_URL=https://your-domain.com/api/

POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=your_supabase_host
POSTGRES_PORT=5432
```

### 4. Lancer l'application

Démarrer les services avec Docker Compose

```bash
docker-compose up --build -d
```

Cela va démarrer les services suivants :

- L’application Django (via Gunicorn) pour servir les pages web et l’API.
- La base de données PostgreSQL hébergée sur Supabase.

### 5. Accéder à l’application

#### Visualiser et trier les tâches : 

Accédez à la page de gestion des tâches à l’URL suivante : http://localhost:4003/tasks/

#### Accéder à l’API REST : 

L’API REST est disponible à l’adresse suivante : http://localhost:4003/api/

#### Documentation Swagger UI :

La documentation interactive de l’API est accessible via Swagger UI : http://localhost:4003/swagger/

#### Interface d’administration Django :

Pour accéder à l’interface d’administration, connectez-vous avec vos identifiants admin : http://localhost:4003/admin/

## Documentation

- [x] [Todo List](https://kevindebenedetti.github.io/documentation/django/todolist/)
- [x] [API REST](http://localhost:4321/documentation/django/api-rest/)
- [x] [Variables d'environnement](https://kevindebenedetti.github.io/documentation/django/env/)
- [x] [Base de données](https://kevindebenedetti.github.io/documentation/django/database/)
