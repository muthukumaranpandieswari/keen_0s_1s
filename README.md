# keen_0s_1s

A Django website for hosting updates with a white-background landing page and no login screen.

## Features

- Front page branding: `keen_to_basic_0s_1s`
- Clean, modern CSS with hover and glassy card effects
- No login required on first load
- Django frontend and Python backend

## Run locally

```powershell
& "c:\Users\praveena\OneDrive\Desktop\Ai\.venv\Scripts\python.exe" manage.py migrate
& "c:\Users\praveena\OneDrive\Desktop\Ai\.venv\Scripts\python.exe" manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Deployment

This repository is already linked to GitHub at `https://github.com/muthukumaranpandieswari/keen_0s_1s.git`.

To push changes to GitHub:

```powershell
cd "c:\Users\praveena\OneDrive\Desktop\Ai\keen_0s_1s"
git add .
git commit -m "Add Django freelancing updates website"
git push origin main
```

> Note: GitHub Pages does not host Django apps directly. For full deployment, use a Python-capable host like Render, Railway, or PythonAnywhere and connect it to this GitHub repo.
