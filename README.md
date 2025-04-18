# Unfollowers Instagram - Comparador de Seguidos/Seguidores 📊
[ 📑 [English Version]](https://github.com/mletelle/instagram_comparer/blob/main/README.en.md)
> Averiguá de forma sencilla quiénes no te siguen (o a quiénes no seguís) en Instagram.
> Todo corre en tu PC, por lo que no es baneable ni hay peligro de que roben tu informacion (saludos para las app de PlayStore)

---

## 1. ¿Qué hace este programa?

1. **Le pedís a Instagram** dos archivos (“followers” y “following”) que contienen tu lista de seguidos y seguidores.  
2. **Abrís el programa** → seleccionás esos archivos.  
3. El programa te muestra:  
   * Usuarios a los que seguís **y NO te siguen** de vuelta.  
   * Usuarios que te siguen **y VOS no seguís**.

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
   5. Instagram te envia un enlace por correo
   6. Descargá el ZIP, descomprimilo y buscá dentro la carpeta **`followers_and_following`**.  
      * ***followers_1.json***  
      * ***following.json***

> ⚠️ No renombres los archivos; el programa los detecta tal cual.

---

## 3. Opciones para usar la herramienta

### Opción A – Navegador sin instalar nada (Cualquier SO)
1. Descargá el archivo `index.html` (y la carpeta `scr/` si queres tener un loguito lindo)
2. Abri `index.html` (o arrastralo a tu navegador)
3. Listo, elegi primero `followers_1.json` y luego `following.json`.  
4. Revisá los link que te genera al perfil de cada persona.
5. Tuki

### Opción B – Ejecutable sin instalar nada (Windows)
1. Abrí la pestaña **Releases** en este repositorio
2. Tocá Assets y tenes 3 archivos para elegir
3. Descargá **`instagram_comparer.exe`** 
4. Presiona Ctrl + J para ver las descargas desde el navegador o anda a tu carpeta de descargas y hacé doble‑clic en el `.exe`
5. Si dice "Windows protegió su PC", tocá en "Mas informacion" y "Ejecutar de todas formas".
6. Se abrirá una ventana para elegir primero `followers_1.json` y luego `following.json`.  
7. Revisá los resultados que aparecen en pantalla. Tocá enter para salir.
8. Tuki

### Opción C: Script simple en Phyton 
1. Baja el archivo `comparar_instagram.py`
2. Tenes que tener `followers_1.json` y `following.json` en la misma carpeta que el **.py**
3. Corre el script: `python3 comparar_instagram.py`
4. Listo, te sale todo por consola ¯\_(ツ)_/¯

### Opción D (la manera mas divertida): Mac / Linux / Windows con Python
> Necesitás tener Python 3.9 o superior.  
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
   ````
3. Instalá dependencias (por las dudas)
```bash
pip install -r requirements.txt
````
5. Ejecutá el programa
````bash
python -m comparar_instagram
````
6. Tuki


## Preguntas frecuentes
- ¿Se envían mis datos a algún servidor?	
No. Todo corre localmente en tu computadora.
- ¿Corre peligro mi informacion o mi cuenta?
Ninguno, fijate el `comparar_instagram.py`, mas claro echale agua.
- ¿Seguro?
Si.
- ¿Por qué pide JSON y no CSV/HTML?	
Porque Instagram ofrece la información más completa en JSON. Y es mas facil ¯\_(ツ)_/¯
- ¿Puedo borrar los archivos luego?
Sí, después de ejecutar podés eliminarlos. Literamente no guarda nada, asi que borralo noma'.
- ¿Hace falta cuenta de desarrollador en Instagram?
No.


## Contribui
- Hacé un fork del repo.
- Crea tu rama: `git checkout -b feature/nueva-funcionalidad`
- Commit y push.
- Abrí un Pull Request

## Licencia
Son un par de lineas en Python flaco. Usalo, modificá y compartí libremente.
*Dos besitos porque tres es mucha plata*
