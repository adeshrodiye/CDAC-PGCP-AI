# Flask Blogging Website

A blog with categories, user registration/login, profile pages, and full CRUD for posts.

## Project structure

```
flask_blog/
├── app.py               # Main Flask app + all routes
├── models.py            # SQLAlchemy models (User, Post) + CATEGORIES list
├── seed.py               # Populates demo users + sample posts across all categories
├── requirements.txt      # Python dependencies
├── templates/
│   ├── base.html           # Shared layout, navbar, flash messages
│   ├── index.html           # Home page - hero, category tabs, featured + grid
│   ├── login.html            # Login form
│   ├── register.html         # Registration form
│   ├── post.html               # Single post view with cover image
│   ├── create_post.html        # Create / edit post form (category + image URL)
│   ├── profile.html             # User profile - avatar, bio, their posts
│   └── edit_profile.html        # Edit your own bio
└── static/
    └── style.css              # All styling (hero, badges, image cards, avatars)
```

## Setup

1. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. (Optional but recommended) Seed the database with demo users and ~15 sample
   posts spread across every category, so the home page isn't empty:
   ```
   python seed.py
   ```
   This creates a demo account you can log in with:
   - username: `alex_rivera`
   - password: `password123`

   (Two other demo users are created too: `priya_shah` and `maria_chen`, both
   with the same password.)

4. Run the app:
   ```
   python app.py
   ```

5. Open your browser at `http://127.0.0.1:5000`

## Features

- **Categories** — Technology, Travel, Food, Lifestyle, Business, Health.
  Filter posts from the home page's category tabs.
- **Attractive home page** — hero banner, a large featured post, and an
  image-grid of the rest, each tagged with a colored category badge.
- **Cover images** — authors can paste an image URL when writing a post; if
  they don't, a placeholder image is generated automatically so every post
  looks good.
- **User profile pages** — `/profile/<username>` shows an auto-generated
  avatar, bio, join date, and all of that user's posts. Logged-in users can
  edit their own bio.
- User registration with hashed passwords (Werkzeug)
- Login / logout with Flask-Login session management
- Create, edit, and delete blog posts (only by their author)
- Flash messages for feedback (success/error/info)
- Responsive design

## Notes / next steps

- Change `app.config['SECRET_KEY']` before deploying anywhere public.
- Swap SQLite for PostgreSQL/MySQL in production by changing `SQLALCHEMY_DATABASE_URI`.
- Add pagination, comments, or real image uploads as you extend it.
