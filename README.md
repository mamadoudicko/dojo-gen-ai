# AI note taker

This project that use AI to take note from an audio recorder. It is based on Streamlit and OpenAI API.


## Use this project with Github Codespaces

You can use Github Codespaces to run the project. It will automatically install the dependencies and run the project.

### Usage
1. Cliquer sur le bouton vert "Code"
2. Sélectionner "Ouvrir avec Codespaces" ou le bouton plus à coté de `CodeSpaces`
3. Attendre que le projet soit prêt (ça peut prendre quelques minutes 🤐, ne pas hésiter à rafraichir la page au bout de 5 minutes)
## Installation sans Github Codespaces

1. Forker le projet
2. Installer les dépendances

- Backend
```bash
pip install -r requirements.txt
```

- Frontend
```bash
cd frontend
pnpm install
```

3. Lancer le projet

- Backend

```bash
python3 -m streamlit run 'streamlit_app.py'
```

- Frontend

```bash
cd frontend
pnpm start
```