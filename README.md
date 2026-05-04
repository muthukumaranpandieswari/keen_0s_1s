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

### Deploy with Render using GitHub Actions

A GitHub Actions workflow is included at `.github/workflows/deploy.yml`.

1. Create a Render account and a new Web Service.
2. Connect the service to this GitHub repository.
3. Add these GitHub repository secrets:
   - `RENDER_API_KEY`
   - `RENDER_SERVICE_ID`
4. Push to `main` and GitHub Actions will trigger deployment.

To push changes to GitHub:

```powershell
cd "c:\Users\praveena\OneDrive\Desktop\Ai\keen_0s_1s"
git add .
git commit -m "Add Render deployment workflow"
git push origin main
```

> Note: GitHub Pages cannot host a Django backend directly. The workflow above deploys the repo to Render, which supports Python/Django web apps.
