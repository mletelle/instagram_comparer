# Instagram Comparer 📊

> Averiguá de forma sencilla quiénes no te siguen (o a quiénes no seguís) en Instagram.

---

## 1. ¿Qué hace este programa?

1. **Le pedís a Instagram** dos archivos (“followers” y “following”) que contienen tu lista de seguidos y seguidores.  
2. **Abrís el programa** → seleccionás esos archivos.  
3. El programa te muestra:  
   * 🔴 Usuarios a los que seguís **y NO te siguen** de vuelta.  
   * 🟢 Usuarios que te siguen **y VOS no seguís**.

---

## 2. Cómo obtener los archivos desde Instagram

1. **Desde el celular**  
   1. Abrí Instagram >  ☰  (Menú) > **Tu actividad**.  
   2. Elegí **Descargar tu información**.  
   3. Escribí tu e‑mail, tocá **Siguiente** y pedí **JSON** como formato.  
   4. Instagram te enviará un enlace por correo (puede tardar varios minutos).  
   5. Descargá el ZIP, descomprimilo y buscá dentro la carpeta **`followers_and_following`**.  
      * ***followers_1.json***  
      * ***following.json***

2. **Desde la web (PC)**  
   1. Entrá a [instagram.com](https://instagram.com) y logueate.  
   2. Click en tu avatar > **Configuración**.  
   3. **Privacidad y seguridad** > **Descargar datos**.  
   4. Ingresá tu e‑mail, elegí **JSON** y “Siguiente”.  
   5. Cuando llegue el correo, bajá el ZIP, descomprimilo y encontrá los mismos archivos:  
      `followers_and_following/followers_1.json` y `followers_and_following/following.json`.

> ⚠️ No renombres los archivos; el programa los detecta tal cual.

---

## 3. Opciones para usar la herramienta

### Opción A – ¡Sin instalar nada! (Windows)

1. Abrí la pestaña **Releases** en este repositorio(o desde `dist/instagram_comparer.exe`).  
2. Descargá **`instagram_comparer.exe`**.  
3. Hacé doble‑clic → se abrirá una ventana para elegir primero `followers_1.json` y luego `following.json`.  
4. Revisá los resultados que aparecen en pantalla.

### Opción B – Mac / Linux / Windows con Python

> Necesitás tener Python 3.9 o superior.  
> Si no lo tenés, podés descargarlo de <https://www.python.org/downloads/> y seguir el instalador (en Windows recordá marcar “Add Python to PATH”).

1. **Cloná o bajá** este repo  
   * Con Git:  
     ```bash
     git clone https://github.com/mletelle/instagram_comparer.git
     cd instagram_comparer
     ```  
   * Sin Git: descargá el ZIP (“Code” → “Download ZIP”), descomprimí y entrá a la carpeta.

2. **(Opcional, recomendado)** Creá entorno virtual  
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate

3. Instalá dependencias (por las dudas)
```bash
pip install -r requirements.txt
````
5. Ejecutá el programa
````bash
python -m comparar_instagram
````

## Preguntas frecuentes
- ¿Hace falta cuenta de desarrollador en Instagram?
No. Solo tu descarga de datos oficial.
- ¿Se envían mis datos a algún servidor?	
No. Todo corre localmente en tu computadora.
- ¿Por qué pide JSON y no CSV?	
Porque Instagram ofrece la información más completa en JSON.
- ¿Puedo borrar los archivos luego?
Sí, después de ejecutar podés eliminarlos.

## Contribuir
- Hacé un fork del repo.
- Crea tu rama: `git checkout -b feature/nueva-funcionalidad`
- Commit y push.
- Abrí un Pull Request. Toda mejora es bienvenida

## Licencia
Son un par de lineas en Python flaco. Usalo, modificá y compartí libremente.
