# gsm

En travaux → branche declarative

## Flux

### Dossiers/fichiers principaux

bootstrap/ = initialisation

core/ = fondations de l’app

- config.py = params
- router.py = navigation, logique centrale

layouts/ = structure visuelle - Templates

views/ = écrans

app.py = assemblage déclaratif

### Simplifié

```bash
src/main.py
    ↓
AppBootstrap
    ↓
App
    ↓
MainLayout
    ↓
Router
    ↓
View
    ↓
Components
```

### Détaillé


```bash
uv run flet run
        |
        v
src/main.py
        |
        v
ft.run(AppBootstrap)
        |
        v
gsm/bootstrap/app_bootstrap.py

        |
        +--> charge Config
        |
        +--> initialise Services
        |
        +--> initialise Session
        |
        +--> configure ft.Page
        |
        +--> page.render(App)

        |
        v

gsm/app.py

        |
        v

App()

        |
        +--> Provider
        |
        +--> Theme
        |
        +--> Router
        |
        +--> Layout
        |
        +--> View courante
```

## Structure

```bash
src/
│
├── main.py                    # Entry point Flet
│
└── gsm/
    │
    ├── app.py                 # Racine déclarative de l'application
    │
    ├── bootstrap/
    │   └── app_bootstrap.py   # Initialisation de l'application
    │
    ├── core/
    │   ├── config.py          # Configuration globale
    │   ├── router.py          # Routes/navigation
    │   ├── session.py         # Session utilisateur
    │   └── theme.py           # Thème global
    │
    ├── providers/
    │   └── app_provider.py    # État global partagé
    │
    ├── services/
    │   ├── auth_service.py
    │   └── api_service.py
    │
    ├── layouts/
    │   └── main_layout.py
    │
    ├── views/
    │   ├── home.py
    │   ├── login.py
    │   └── settings.py
    │
    └── components/
        ├── header.py
        └── sidebar.py
```

## Mémo

### config.py VS settings.py

config.py :

- clés API
- constantes métier
- options de services
- paramètres de scraping
- chemins personnalisés
- règles internes

VS

settings.py :

- configuration de la base de données
- middleware
- applications installées
- routes statiques
- sécurité
- internationalisation
- logs
- templates
- cache
- email
- etc.

### Pour un lancement direct d'un fichier

```bash
pip install -e . 
```
