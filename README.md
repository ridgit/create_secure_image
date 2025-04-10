# Secure serverless function

The pipeline we have implemented provides an initial layer of security at the design stage of serverless functions. This process automates the creation of Docker images, which are then used by a serverless function manager for deployment.
At this stage, a security check is performed to detect potential vulnerabilities in the source code of the functions, particularly those developed in Python.

<details>
<summary>🇫🇷 Version Française</summary>

# Fonction serverless sécurisée

Le pipeline mis en place assure une première couche de sécurité dès l'étape de conception des fonctions serverless. Ce processus automatise la création des images Docker, utilisées par un gestionnaire de fonctions serverless pour le déploiement. À ce stade, une vérification de sécurité est effectuée pour détecter les potentielles vulnérabilités dans le code source des fonctions, notamment celles développées en Python.

## Instructions d'utilisation ou de test du projet

Pour utiliser ou tester ce projet, procédez ainsi :

### ✅ Étape 1 : Nouveau dépôt
- Créez-vous un nouveau repository sur GitHub.

### ✅ Étape 2 : Fonctions Python
- Placez vos fonctions Python dans un dossier du repository créé.

### ✅ Étape 3 : Workflow GitHub Actions
- Créez le dossier `.github/workflows/` dans votre repository.
- Créez un fichier `workflow_name.yml` à l'intérieur.

### ✅ Étape 4 : Télécharger le workflow
- Téléchargez le fichier via :

```bash
wget https://raw.githubusercontent.com/ridgit/create_secure_image/refs/heads/main/.github/workflows/pworkflow.yml
```

- Copiez ce contenu dans votre fichier `workflow_name.yml`.

### ✅ Étape 5 : Personnaliser le workflow
- Éditez le fichier `workflow_name.yml` en définissant précisément le chemin d'accès à votre projet à analyser.

Les captures suivantes montrent les lignes à modifier pour spécifier votre chemin projet :

- ![Capture 1](images/gitguardian.png)
- ![Capture 2](images/bandit.png)
- ![Capture 3](images/dockerim.png)

### ✅ Étape 6 : Sécuriser les accès Docker Hub

Modifiez également ce fichier en indiquant vos informations d'accès à votre repository Docker Hub (ou tout autre hébergement Docker) via les secrets GitHub, comme montré ici :

- ![Configuration Secrets](images/login.png)

## Résultats

Le workflow GitHub Actions sera automatiquement déclenché, exécutant ainsi une série de vérifications de sécurité sur votre projet. Si aucune vulnérabilité n’est détectée, une image Docker sera créée et poussée dans le registre Docker que vous aurez spécifié. Sinon, rendez-vous dans l’onglet GitHub Actions pour visualiser un résumé détaillé des problèmes détectés, accompagné des recommandations pour les résoudre.

---

</details>

<details>
<summary>🇬🇧 English Version</summary>

##  Project Usage or Testing Instructions

To use or test this project, follow these steps:

### ✅ Step 1: Create a New Repository
- Create a new repository on GitHub.

### ✅ Step 2: Add Python Functions
- Place your Python functions into a folder within the newly created repository.

### ✅ Step 3: Set Up GitHub Actions Workflow
- Create a folder named `.github/workflows/` in your repository.
- Create a file named `workflow_name.yml` inside this folder.

### ✅ Step 4: Download the Workflow
- Download the workflow file using:

```bash
wget https://raw.githubusercontent.com/ridgit/create_secure_image/refs/heads/main/.github/workflows/pworkflow.yml
```

- Paste the downloaded content into your previously created `workflow_name.yml` file.

### ✅ Step 5: Customize the Workflow
- Edit the `workflow_name.yml` file by specifying the exact path to your project folder you want to analyze.

The following screenshots show the lines you need to adjust to specify your project's path:

- ![Screenshot 1](images/gitguardian.png)
- ![Screenshot 2](images/bandit.png)
- ![Screenshot 3](images/dockerim.png)

### ✅ Step 6: Secure Docker Hub Access

Also, update this file by securely specifying your Docker Hub repository access credentials (or other Docker registry) via GitHub secrets as shown here:

- ![Secrets Configuration](images/login.png)

##  Results

The GitHub Actions workflow will automatically trigger, running a series of security checks on your project. If no vulnerabilities are found, a Docker image will be created and pushed to the specified Docker registry. Otherwise, visit the GitHub Actions tab for a detailed summary of issues found and recommendations for resolving them.

---

</details>

