# My Schedule Web App

A modern, offline-capable Progressive Web App (PWA) for viewing class schedules.

## Deployment Instructions

### 1. Upload to GitHub
1. Open your terminal in the project folder: `/home/giscard/IdeaProjects/schedule`
2. Initialize Git if you haven't already:
   ```bash
   git init
   git add .
   git commit -m "Initial commit with PWA setup"
   ```
3. Create a new repository on [GitHub](https://github.com/new).
4. Link your local repo to GitHub and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   git push -u origin main
   ```

### 2. Deploy to Netlify
1. Log in to [Netlify](https://app.netlify.com/).
2. Click **"Add new site"** > **"Import an existing project"**.
3. Select **GitHub** and authorize if necessary.
4. Choose the repository you just created.
5. In the build settings, leave the defaults (Netlify will use the `netlify.toml` file automatically, which tells it to serve `schedule.html` when someone visits the root URL `/`).
6. Click **Deploy site**.

Once deployed, you can add it to your mobile phone's home screen, and it will work like a native app (offline capable, full-screen, custom icon)!
