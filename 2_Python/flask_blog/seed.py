"""
Seed script - populates the database with demo users and a variety of
blog posts across every category, each with a placeholder cover image.

Run once after installing dependencies:
    python seed.py
"""

from datetime import datetime, timezone, timedelta
from werkzeug.security import generate_password_hash

from app import app
from models import db, User, Post, CATEGORIES

# username, email, password, bio
DEMO_USERS = [
    ("alex_rivera", "alex@example.com", "password123",
     "Tech writer and gadget enthusiast. I break things so you don't have to."),
    ("priya_shah", "priya@example.com", "password123",
     "Travel blogger, currently chasing sunsets across three continents."),
    ("maria_chen", "maria@example.com", "password123",
     "Home cook turned food blogger. Recipes that actually work on a weeknight."),
]

# (title, category, content, image_seed)
DEMO_POSTS = [
    ("10 AI Tools That Will Change How You Work in 2026", "Technology",
     "Artificial intelligence keeps reshaping the way we work, and this year's "
     "crop of tools is more capable than ever. From writing assistants to "
     "autonomous coding agents, here's a rundown of ten tools worth trying, "
     "what they're good at, and where they still fall short. We tested each "
     "one for a full week before writing this list, so these are honest, "
     "hands-on impressions rather than marketing copy.", "tech1"),
    ("Why Everyone Is Talking About Edge Computing", "Technology",
     "Edge computing moves processing closer to where data is generated instead "
     "of relying entirely on distant cloud servers. That means lower latency, "
     "less bandwidth usage, and new possibilities for real-time applications "
     "like autonomous vehicles and smart factories. We break down the basics "
     "and why it matters for the next decade of software.", "tech2"),
    ("A Beginner's Guide to Building Your First App", "Technology",
     "Building your first app can feel overwhelming, but it doesn't have to be. "
     "This guide walks through picking a simple idea, choosing a framework, "
     "and shipping a working version in a weekend. We focus on momentum over "
     "perfection, because a finished small project beats an abandoned big one.", "tech3"),

    ("48 Hours in Lisbon: The Perfect Weekend Itinerary", "Travel",
     "Lisbon rewards travelers who wander. This itinerary covers the pastel "
     "streets of Alfama, the miradouros with the best sunset views, and where "
     "to find pastÃ©is de nata that live up to the hype. We also cover how to "
     "get around without a car and where to eat like a local, not a tourist.", "travel1"),
    ("Backpacking Southeast Asia on a Budget", "Travel",
     "You don't need a huge budget to see Southeast Asia properly. This guide "
     "covers realistic daily costs across Vietnam, Thailand, and Cambodia, plus "
     "tips on overnight buses, street food safety, and how to avoid the most "
     "common tourist traps that drain your wallet fast.", "travel2"),
    ("Why Slow Travel Might Be the Best Trip You Ever Take", "Travel",
     "Instead of cramming ten cities into two weeks, slow travel means picking "
     "one place and really living there for a while. We share what changed "
     "when we spent a month in a single Italian village instead of rushing "
     "through five countries.", "travel3"),

    ("The 5-Ingredient Pasta Recipe You'll Make on Repeat", "Food",
     "Some of the best meals need almost nothing. This pasta recipe uses just "
     "five pantry ingredients and comes together in twenty minutes, making it "
     "the perfect weeknight fallback when you don't have the energy to cook "
     "something elaborate but still want something genuinely good.", "food1"),
    ("Meal Prep Sunday: A Full Week of Healthy Lunches", "Food",
     "Meal prepping doesn't have to mean bland chicken and rice every day. "
     "This plan covers five different lunches you can prep in about two hours "
     "on a Sunday, all built around simple swaps that keep things interesting "
     "through the whole work week.", "food2"),
    ("Baking Bread at Home: What I Wish I Knew Sooner", "Food",
     "My first loaves were dense, pale, and honestly a little sad. After a "
     "year of weekend baking experiments, here's what actually made the "
     "difference: hydration, patience, and a cheap kitchen scale that changed "
     "everything about my results.", "food3"),

    ("Digital Minimalism: What I Learned From a 30-Day Phone Detox", "Lifestyle",
     "I put my phone in a drawer for thirty days and kept a notebook instead. "
     "This is an honest account of the boredom, the withdrawal, and the "
     "surprising clarity that showed up around week two, along with the habits "
     "I kept after the experiment ended.", "life1"),
    ("Building a Morning Routine That Actually Sticks", "Lifestyle",
     "Most morning routine advice assumes you have an hour of free time before "
     "work, which isn't realistic for most people. Here's a version built "
     "around fifteen minutes, three habits, and zero willpower required.", "life2"),

    ("Bootstrapping a Startup Without Venture Capital", "Business",
     "Not every company needs a funding round to grow. This is a look at how "
     "we built a profitable small software business by staying lean, charging "
     "from day one, and reinvesting revenue instead of chasing investors.", "biz1"),
    ("Five Negotiation Tactics That Actually Work", "Business",
     "Negotiation isn't about being aggressive, it's about preparation. These "
     "five tactics come from real deals we've closed, along with the mistakes "
     "that nearly cost us the good outcomes.", "biz2"),

    ("Understanding Sleep Cycles and Why Consistency Beats Duration", "Health",
     "Getting eight hours doesn't matter much if that sleep is fragmented. "
     "We look at what sleep cycles actually do for your body and why going to "
     "bed at the same time every night might matter more than the total hours "
     "you log.", "health1"),
    ("A Realistic Guide to Starting Strength Training", "Health",
     "Strength training doesn't require a gym membership or hours of free "
     "time. This guide covers a simple three-day-a-week routine for beginners, "
     "with modifications for anyone starting from zero.", "health2"),
]


def run():
    with app.app_context():
        db.create_all()

        users = {}
        for username, email, password, bio in DEMO_USERS:
            existing = User.query.filter_by(username=username).first()
            if existing:
                users[username] = existing
                continue
            user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password),
                bio=bio
            )
            db.session.add(user)
            users[username] = user

        db.session.commit()

        author_cycle = list(users.values())
        base_date = datetime.now(timezone.utc) - timedelta(days=len(DEMO_POSTS))

        created = 0
        for i, (title, category, content, image_seed) in enumerate(DEMO_POSTS):
            if Post.query.filter_by(title=title).first():
                continue

            post = Post(
                title=title,
                content=content,
                category=category,
                image_url=f"https://picsum.photos/seed/{image_seed}/700/450",
                date_posted=base_date + timedelta(days=i, hours=i),
                author=author_cycle[i % len(author_cycle)]
            )
            db.session.add(post)
            created += 1

        db.session.commit()
        print(f"Seed complete. {len(users)} users ensured, {created} new posts added.")
        print(f"Categories in use: {', '.join(CATEGORIES)}")
        print("Demo login -> username: alex_rivera | password: password123")


if __name__ == '__main__':
    run()
