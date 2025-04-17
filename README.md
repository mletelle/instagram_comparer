# Instagram Comparer 📊

Pequeña utilidad en Python para comparar tus listas de **followers** y **following** exportadas desde Instagram y detectar quién no te sigue de vuelta (o viceversa).

## Instalación rápida

```bash
git clone https://github.com/tu-usuario/instagram_comparer.git
cd instagram_comparer
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> *Este proyecto no requiere dependencias externas; solo la librería estándar de Python.*

## Uso

```bash
python -m comparar_instagram
```

Al ejecutar, se abrirán dos diálogos para que selecciones `followers_1.json` y `following.json`.  
El programa mostrará:

- 🔴 Usuarios a los que **seguís** y **NO** te siguen.
- 🟢 Usuarios que **te siguen** y que **vos** no seguís.

### Ejecutable (Windows)

1. Instalar PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2. Generar el `.exe`:

    ```bash
    pyinstaller --onefile -n instagram_comparer comparar_instagram/cli.py
    ```

   El ejecutable quedará en `dist\instagram_comparer.exe`.  
   Doble clic o `instagram_comparer.exe` en consola y listo.

## Estructura del repo

```
instagram_comparer/
├── comparar_instagram/
│   ├── __init__.py
│   └── cli.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Licencia
MIT
# instagram_comparer
