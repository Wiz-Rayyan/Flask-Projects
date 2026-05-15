## Overview

I have build a **Flask blog application** with the following features:

- User authentication (register, login, logout)
- Create, read, update, and delete blog posts
- SQLite database (using Flask-SQLAlchemy)
- Password hashing (Flask-Bcrypt)
- User sessions (Flask-Login)
- Bootstrap 5 for frontend styling
- Flash messages for user feedback

This is a beginner level app that demonstrates core Flask concepts.

---

## File Structure

```
flask_blog/
├── app.py                 # Application entry point
├── models.py              # Database models (User, Post)
├── forms.py               # WTForms classes
├── routes.py              # Route handlers
├── config.py              # Configuration settings
├── requirements.txt       # Dependencies
├── instance/
│   └── site.db            # SQLite database (auto-created)
└── templates/
    ├── base.html          # Layout template
    ├── index.html         # Homepage with all posts
    ├── register.html      # Registration page
    ├── login.html         # Login page
    ├── create_post.html   # Create new post
    ├── update_post.html   # Edit post
    └── post_detail.html   # View single post
```

---

pip install --upgrade flask-login