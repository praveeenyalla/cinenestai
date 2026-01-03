import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# --- MongoDB Connection ---
MONGO_URI = os.getenv("MONGO_URI")

client = None
db = None

# Initialize collections at module level
user_collection = None
content_collection = None
history_collection = None
admins_collection = None
user_analytics_collection = None

if not MONGO_URI:
    MONGO_URI = "mongodb://localhost:27017" 

try:
    client = MongoClient(MONGO_URI)
    db = client.get_database("ott_database")
    
    # Update global collections
    user_collection = db["users"]
    content_collection = db["content"]
    history_collection = db["history"]
    admins_collection = db["admins"]
    user_analytics_collection = db["user_analytics_data"]
    
    print("✅ Connected to MongoDB")
except Exception as e:
    print(f"❌ Failed to connect to MongoDB: {e}")

# --- PostgreSQL Connection (Optional) ---
# We generally use MongoDB, but leave this placeholder for general SQL needs if preferred.
PG_DATABASE_URL = os.getenv("DATABASE_URL")
pg_conn = None

if PG_DATABASE_URL:
    try:
        import psycopg2
        pg_conn = psycopg2.connect(PG_DATABASE_URL)
        print("✅ Connected to PostgreSQL")
    except ImportError:
        print("⚠️ psycopg2 not installed. PostgreSQL support limited.")
    except Exception as e:
        print(f"❌ Failed to connect to PostgreSQL: {e}")

def get_db():
    return db

def get_pg_conn():
    return pg_conn
