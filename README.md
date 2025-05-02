# Carnet d'adresses Django

Une application web de gestion de contacts développée avec Django.

## Fonctionnalités

- Gestion complète des contacts (création, modification, suppression)
- Recherche de contacts
- Catégorisation des contacts (Favoris, Famille, Amis)
- Mode sombre/clair
- Interface responsive et moderne
- Gestion des images de profil
- Rappels d'anniversaire pour les favoris

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/votre-username/carnet-d-adresses.git
cd carnet-d-adresses
```

2. Créez un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :

```bash
pip install -r requirements.txt
```

4. Appliquez les migrations :

```bash
python manage.py migrate
```

5. Créez un superutilisateur :

```bash
python manage.py createsuperuser
```

6. Lancez le serveur de développement :

```bash
python manage.py runserver
```

## Structure du projet

```
carnet-d-adresses/
├── contactbook/          # Configuration du projet
├── contacts/            # Application principale
│   ├── migrations/      # Migrations de la base de données
│   ├── templates/       # Templates HTML
│   ├── static/          # Fichiers statiques
│   ├── models.py        # Modèles de données
│   ├── views.py         # Vues
│   └── urls.py          # URLs de l'application
├── static/              # Fichiers statiques globaux
└── manage.py            # Script de gestion Django
```

## Utilisation

1. Accédez à l'application via votre navigateur : http://127.0.0.1:8000/
2. Connectez-vous avec votre compte administrateur
3. Commencez à gérer vos contacts !

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
