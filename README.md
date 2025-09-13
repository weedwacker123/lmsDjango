# EduCanvas - Learning Management System

A modern, Canvas-inspired Learning Management System built with Django, featuring video-based learning similar to YouTube.

## Features

- **User Authentication**: Role-based access control (Administrators and Students)
- **Video Content Management**: Upload, organize, and stream educational videos
- **Course Organization**: Categories, subjects, and grade levels
- **Professional UI**: Canvas/Coursera/Udemy-inspired interface
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Admin Dashboard**: Full content management capabilities

## Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite (development), PostgreSQL ready for production
- **Frontend**: HTML5, CSS3, JavaScript, Font Awesome icons
- **Video**: HTML5 video player with full controls
- **Authentication**: Django's built-in authentication system

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/educanvas-lms.git
   cd educanvas-lms
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python3 lms_core/manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   python3 lms_core/manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python3 lms_core/manage.py runserver
   ```

6. **Access the application**
   - Student Dashboard: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

### Deploy to Render.com (Free Tier)

1. **Push this repository to your GitHub account**

2. **Create a PostgreSQL Database (Free Tier)**
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" → "PostgreSQL"
   - Name: `educanvas-lms-db`
   - Database Name: `educanvas_lms`
   - User: `educanvas_user`
   - Select **Free** plan
   - Click "Create Database"
   - Copy the **Internal Database URL** (starts with `postgresql://`)

3. **Create a Web Service (Free Tier)**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: `educanvas-lms` (or your preferred name)
     - **Runtime**: Python 3
     - **Build Command**: `./build.sh`
     - **Start Command**: `./start.sh`
     - **Instance Type**: Select **Free** ($0/month)

4. **Set Environment Variables**
   - In the Web Service settings, add these environment variables:
     - `DATABASE_URL`: Paste the Internal Database URL from step 2
     - `SECRET_KEY`: Generate a secure key (you can use Django's `get_random_secret_key()`)
     - `DEBUG`: `False`

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (5-10 minutes)
   - Your app will be available at `https://your-app-name.onrender.com`

6. **Create Admin User**
   - In your Render dashboard, go to your web service
   - Click "Shell" tab
   - Run: `cd lms_core && python manage.py createsuperuser`
   - Follow the prompts to create your admin account

**Note**: Free tier services may spin down after 15 minutes of inactivity and take 30-60 seconds to restart.

## Project Structure

```
educanvas-lms/
├── lms_core/           # Main Django project
│   ├── lms_core/       # Project settings
│   └── manage.py       # Django management script
├── users/              # User authentication and roles
├── videos/             # Video content management
├── catalog/            # Categories, subjects, grade levels
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## User Roles

### Administrator
- Upload and manage video content
- Create and organize categories, subjects, and grade levels
- Manage user accounts
- Access admin dashboard

### Student
- Browse and watch videos
- Filter content by subject and grade level
- Access personalized dashboard
- View course progress

## Sample Data

The system includes sample data with:
- Multiple subjects (Math, Science, English, History)
- Various grade levels (6, 9, 10, 12)
- Sample video content
- Demo users for testing

## Development

### Adding New Features

1. Create new Django apps for major features
2. Update models in respective apps
3. Run migrations: `python3 lms_core/manage.py makemigrations && python3 lms_core/manage.py migrate`
4. Update admin.py to register new models
5. Create templates and views as needed

### Customizing the UI

- Main styles: `videos/static/css/main.css`
- Templates: `videos/templates/videos/`
- Static files: `videos/static/`

## Production Deployment

1. Set `DEBUG = False` in settings.py
2. Configure PostgreSQL database
3. Set up proper static file serving
4. Configure media file storage (AWS S3 recommended)
5. Set up proper domain and SSL

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please open an issue on GitHub or contact the development team.
