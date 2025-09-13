# 🆓 Render.com Free Tier Deployment Guide

This guide will help you deploy your Django LMS on Render.com's **completely free tier**.

## 📋 Prerequisites

- GitHub account with your code pushed
- Render.com account (free to create)

## 🚀 Step-by-Step Deployment

### Step 1: Create PostgreSQL Database (Free)

1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"PostgreSQL"**
3. Fill in the details:
   - **Name**: `educanvas-lms-db`
   - **Database Name**: `educanvas_lms`
   - **User**: `educanvas_user`
   - **Region**: Choose closest to you
   - **PostgreSQL Version**: Latest (default)
4. **Important**: Select **"Free"** plan ($0/month)
5. Click **"Create Database"**
6. Wait for database creation (2-3 minutes)
7. **Copy the "Internal Database URL"** - you'll need this later!

### Step 2: Create Web Service (Free)

1. Click **"New +"** → **"Web Service"**
2. Choose **"Build and deploy from a Git repository"**
3. Connect your GitHub account and select your repository
4. Configure the service:

   **Basic Settings:**
   - **Name**: `educanvas-lms` (or your preferred name)
   - **Runtime**: **Python 3**
   - **Region**: Same as your database
   - **Branch**: `main`

   **Build & Deploy:**
   - **Build Command**: `./build.sh`
   - **Start Command**: `./start.sh`

   **Instance Type:**
   - **IMPORTANT**: Select **"Free"** ($0/month, 512MB RAM, 0.1 CPU)

### Step 3: Set Environment Variables

In the **"Environment Variables"** section, add these:

1. **DATABASE_URL**
   - Value: Paste the Internal Database URL from Step 1
   - Example: `postgresql://user:password@host:port/database`

2. **SECRET_KEY**
   - Value: Generate a secure key (50+ random characters)
   - You can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

3. **DEBUG**
   - Value: `False`

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Watch the build logs (5-10 minutes for first deployment)
3. Wait for **"Your service is live"** message
4. Your app will be available at: `https://your-app-name.onrender.com`

### Step 5: Create Admin User

1. In your Render dashboard, go to your web service
2. Click the **"Shell"** tab
3. Run this command:
   ```bash
   cd lms_core && python manage.py createsuperuser
   ```
4. Enter username, email, and password when prompted

## 🎉 You're Live!

- **Student Dashboard**: `https://your-app-name.onrender.com/`
- **Admin Panel**: `https://your-app-name.onrender.com/admin/`

## ⚠️ Free Tier Limitations

- **Spin Down**: Service sleeps after 15 minutes of inactivity
- **Cold Start**: Takes 30-60 seconds to wake up
- **Database**: 1GB storage limit
- **Bandwidth**: 100GB/month

## 🔧 Troubleshooting

### Build Failed?
- Check build logs in Render dashboard
- Ensure `build.sh` and `start.sh` are executable
- Verify all files are pushed to GitHub

### Database Connection Issues?
- Double-check DATABASE_URL in environment variables
- Ensure database and web service are in same region
- Verify PostgreSQL database is running

### Static Files Not Loading?
- Check if `collectstatic` ran during build
- Verify WhiteNoise is in MIDDLEWARE settings

## 💡 Tips for Free Tier

1. **Keep it Active**: Visit your site regularly to prevent sleeping
2. **Monitor Usage**: Check Render dashboard for resource usage
3. **Optimize**: Free tier has limited resources, so optimize your queries

Your Django LMS is now running completely free on Render.com! 🚀
