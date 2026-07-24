# UPU

## Flux

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
upu/bootstrap/app_bootstrap.py

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

upu/app.py

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
└── upu/
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
