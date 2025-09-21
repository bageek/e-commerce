# Django E-Commerce Deployment Guide

## Quick Deploy Options

### Option 1: Railway (Recommended - Easiest)
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Connect your GitHub repository
5. Railway will automatically detect Django and deploy
6. Add environment variables in Railway dashboard:
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `localhost,127.0.0.1,.railway.app`

### Option 2: Render (Free Tier Available)
1. Go to [Render.com](https://render.com)
2. Sign up and connect GitHub
3. Click "New Web Service"
4. Connect your repository
5. Configure:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ecom.wsgi:application`
6. Add environment variables:
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `localhost,127.0.0.1,.render.com`

### Option 3: Heroku (Paid)
1. Install Heroku CLI
2. Run: `heroku create your-app-name`
3. Run: `heroku config:set SECRET_KEY=your-secret-key`
4. Run: `heroku config:set DEBUG=False`
5. Run: `git push heroku main`

## Generate Secret Key
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Local Testing Before Deploy
```bash
# Install dependencies
pip install -r requirements.txt

# Test static files collection
python manage.py collectstatic --no-input

# Test migrations
python manage.py migrate

# Test with production settings
export DEBUG=False
export SECRET_KEY=your-test-secret-key
python manage.py runserver
```

## What's Fixed
✅ Static files now work with WhiteNoise
✅ Production-ready settings
✅ Environment variables support
✅ Database configuration for cloud hosting
✅ Security headers enabled
✅ Build script for deployment

## Troubleshooting
- If static files don't load: Check that `STATIC_ROOT` is set and `python manage.py collectstatic` runs
- If database errors: Ensure `DATABASE_URL` is set by hosting platform
- If 500 errors: Check logs in hosting platform dashboard
