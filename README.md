# sci_djangui
Simulation de rentabilité des investissements immobiliers entre amis

---

# Projet de Calcul de Rentabilité pour SCI

Ce projet vise à faciliter le calcul de rentabilité pour une SCI en fournissant une interface conviviale pour les utilisateurs. Il utilise Python comme langage de programmation et le framework Streamlit pour créer une interface web interactive.

## Fonctionnalités

- **Calcul de Rentabilité :** Permet aux utilisateurs d'entrer les détails financiers de leur investissement immobilier et de calculer la rentabilité nette.

- **Graphiques Dynamiques :** Affiche des graphiques interactifs pour visualiser la répartition des coûts, les flux de trésorerie, etc.

## Installation

1. Clônez le dépôt :

   ```bash
   git clone https://github.com/nuentsa/sci_djangui.git
   ```

2. Accédez au répertoire du projet :

   ```bash
   cd sci_djangui
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Exécutez l'application Streamlit :

   ```bash
   streamlit run app.py
   ```

2. Ouvrez votre navigateur et accédez à l'URL indiquée par Streamlit (généralement http://localhost:8501).

3. Remplissez les champs requis pour effectuer le calcul de rentabilité.

4. Explorez les graphiques et résultats générés.

## Structure du Projet

- **Accueil.py :** Le script principal contenant le code Streamlit pour l'interface utilisateur.

- **serializer.py :** Module contenant les fonctions de sauvegarde et restauration des simulations.

- **pages/ :** Les differentes pages de l'application.

- **requirements.txt :** Fichier spécifiant les dépendances Python nécessaires pour le projet.

## Contribuer

Si vous souhaitez contribuer au projet, veuillez suivre ces étapes :

1. Fork le projet.
2. Créez une nouvelle branche (`git checkout -b feature/nouvelle-fonctionnalite`).
3. Committez vos modifications (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`).
5. Ouvrez une Pull Request.


## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
