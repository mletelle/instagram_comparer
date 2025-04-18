# Instagram Unfollowers – Followers/Following Comparator 📊  
[📑 [Versión en Español]](https://github.com/mletelle/instagram_comparer/blob/main/README.md)

> Easily find out who doesn’t follow you (or whom you don’t follow) on Instagram.  
> Everything runs locally on your computer — so no bans, no logins, no sketchy data theft (hi PlayStore apps 👋).

---

## 1. What does this program do?

1. **You request your data from Instagram** — specifically two files: “followers” and “following”.
2. **You open the tool** → select those files.
3. The program shows you:  
   * Users you follow **who DON’T follow you back**  
   * Users who follow you **that YOU don’t follow**

---

## 2. How to get the data from Instagram

1. **From your phone**  
   1. Open Instagram > ☰ (Menu) > **Your activity**  
   2. Choose **Download your information**  
   3. Enter your email, tap **Next**, and request **JSON** format  
   4. Instagram will send you a link via email (this may take a few minutes)  
   5. Download the ZIP, extract it, and find the folder: **`followers_and_following`**  
      * `followers_1.json`  
      * `following.json`

2. **From a web browser (PC)**  
   1. Go to [instagram.com](https://instagram.com) and log in  
   2. Click your avatar > **Settings**  
   3. Go to **Privacy and security** > **Download data**  
   4. Enter your email, choose **JSON**, then click “Next”  
   5. Instagram will send you a link  
   6. Download the ZIP, extract it, and find the folder: **`followers_and_following`**  
      * `followers_1.json`  
      * `following.json`

> ⚠️ Do not rename the files — the tool expects those exact names.

---

## 3. How to use this tool

### Option A – Browser only, no install (Any OS)

1. Download `index.html` (and the `src/` folder if you want a cute logo)  
2. Open `index.html` in your browser (or drag it into a new tab)  
3. Select `followers_1.json` and then `following.json`  
4. Browse the generated profile links  
5. Boom 

---

### Option B – Standalone EXE (Windows only, no install)

1. Go to the **Releases** tab of this repository  
2. Under Assets, choose the file `instagram_comparer.exe`  
3. Download it  
4. Press Ctrl+J to open Downloads or go to your Downloads folder and double-click the file  
5. If you get “Windows protected your PC”, click **More info** → **Run anyway**  
6. Select `followers_1.json`, then `following.json`  
7. Results will be shown in the console — press Enter to exit  
8. Boom 

---

### Option C – Python script

1. Download `comparar_instagram.py`  
2. Make sure `followers_1.json` and `following.json` are in the same folder as the **.py**  
3. Run it:  
   `python3 comparar_instagram.py`  
4. That’s it — it all prints to the terminal ¯\\\_(ツ)_/¯

---

### Option D (the most fun): Python + Terminal (Mac / Linux / Windows)

> Requires Python 3.9 or newer

1. **Clone or download** this repo  
   * With Git:  
     ```bash
     git clone https://github.com/mletelle/instagram_comparer.git
     cd instagram_comparer
     ```
   * Without Git: click **Code → Download ZIP**, unzip and open the folder

2. *(Optional but recommended)* Create a virtual environment  
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate
3. Install dependencies (just in case):
````bash
pip install -r requirements.txt
````
4. Run the program
````bash
python -m comparar_instagram
````

##FAQ
- Does this send my data anywhere?
Nope. It’s all local on your device.
- Is there any risk to my Instagram account?
None. Check the comparar_instagram.py file yourself — it’s as transparent as it gets.
- Seriously?
Yes.
- Why JSON and not CSV/HTML?
Instagram gives more detailed info in JSON. Plus, it’s easier to parse ¯\_(ツ)_/¯
- Can I delete the files afterward?
Absolutely. The tool doesn’t store anything. Run → done → delete.
- Do I need a developer account or API key?
No.

##Contributing
1. Fork the repo
2. Create your branch: git checkout -b feature/my-cool-feature
3. Commit + push
4. Open a Pull Request 🚀

##License
It’s just a few lines of Python and HTML, mate.
Use it, remix it, and share it freely.
Two kisses ‘cause three is too expensive.
