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
