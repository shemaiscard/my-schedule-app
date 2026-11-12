# My Schedule App

**Live demo:** [zeschedule.netlify.app](https://zeschedule.netlify.app/)

A class timetable and assignment tracker for students, built as an installable web app. The weekly schedule opens even without a connection, and assignments sync through Supabase so everyone sees the same list.

## Features

- **Weekly timetable** from Monday to Friday
- **Shared assignments:** add a title and due date, delete it when done. Assignments are stored in a Supabase table
- **Notifications:** the browser can alert you when a new assignment is added (Notifications API, after you allow it)
- **Offline:** a service worker caches the app, so the timetable loads without internet
- **Installable** on a phone or desktop home screen

## Tech stack

| Part | Technology |
| --- | --- |
| Front end | HTML5, CSS3 (Grid and Flexbox), vanilla JavaScript |
| Data | Supabase (`assignments` table) |
| App | Service worker, web manifest, Notifications API |
| Testing | Playwright smoke test (`test_script.py`) |
| Hosting | Netlify (`/` serves `schedule.html`) |

## Run locally

```bash
git clone https://github.com/shemaiscard/my-schedule-app.git
cd my-schedule-app
python3 -m http.server 8000
```

Open <http://localhost:8000/schedule.html>. A local server is needed for the service worker and notifications.

## License

MIT License
