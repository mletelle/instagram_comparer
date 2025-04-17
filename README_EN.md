# Unfollowers Instagram – Followers/Following Comparator 📊

> Quickly find out who doesn’t follow you back (or whom you don’t follow) on Instagram.

> Everything runs locally on your PC—no bans, no risk of data theft (unlike some Play Store apps).

---

## 1. What does this program do?

1. **Ask Instagram** for two files (“followers” and “following”) that contain your lists.  
2. **Run the program** → pick those files.  
3. It shows you:  
   * 🔴 Accounts you follow **that do NOT follow you back**.  
   * 🟢 Accounts that follow you **but YOU don’t follow back**.

---

## 2. How to get the files from Instagram

1. **From the mobile app**  
   1. Open Instagram >  ☰  (Menu) > **Your activity**.  
   2. Tap **Download your information**.  
   3. Enter your e‑mail, tap **Next**, choose **JSON**.  
   4. Instagram will e‑mail a link (may take a few minutes).  
   5. Download the ZIP, unzip it and look for **`followers_and_following`**:  
      * ***followers_1.json***  
      * ***following.json***

2. **From the web (desktop)**  
   1. Go to [instagram.com](https://instagram.com) and log in.  
   2. Click your avatar > **Settings**.  
   3. **Privacy & Security** > **Download Data**.  
   4. Enter your e‑mail, choose **JSON**, click **Next**.  
   5. When the e‑mail arrives, download the ZIP, unzip it and locate:  
      `followers_and_following/followers_1.json` and `followers_and_following/following.json`.

> ⚠️ Do **not** rename the files; the program expects exactly those names.

---

## 3. Ways to use the tool

### Option A – No install needed (Windows)

1. Open the **Releases** tab in this repository.  
2. Under **Assets** you’ll see three files—click `instagram_comparer.exe`.  
3. Download **`instagram_comparer.exe`** to any folder.  
4. Double‑click it in Explorer or press **Ctrl + J** to see your downloads.  
5. If Windows shows “Protected your PC”, click **More info** → **Run anyway**.  
6. A window pops up: select `followers_1.json`, then `following.json`.  
7. Read the results, press **Enter** to exit.

### Option B – Mac / Linux / Windows with Python

> Requires Python 3.9 or newer.  
> Get it from <https://www.python.org/downloads/> (check “Add Python to PATH” on Windows).

1. **Clone or download** this repo  
   * With Git:  
     ```bash
     git clone https://github.com/mletelle/instagram_comparer.git
     cd instagram_comparer
     ```  
   * Without Git: click **Code → Download ZIP**, unzip, enter the folder.

2. **(Optional, recommended)** Create a virtual environment  
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate````
3. Instalá dependencias (por las dudas)
```bash
pip install -r requirements.txt
````
5. Ejecutá el programa
````bash
python -m comparar_instagram
````
## FAQ
- Do I need an Instagram developer account?
No. Just your official data download.
- Are my files uploaded anywhere?
No. Everything runs locally on your computer.
- Why JSON and not CSV?
Instagram’s most complete format is JSON.
- Can I delete the files afterwards?
Yes, you can remove them once you’re done.

## Contributing
1. Fork the repo.
2. Create a branch: git checkout -b feature/new-feature.
3. Commit & push.
4. Open a Pull Request—contributions are welcome!

## License
Just a few lines of Python, mate. Use, modify, and share freely.
