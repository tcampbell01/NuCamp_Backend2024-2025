import random
import string
import hashlib
import secrets
from faker import Faker
import psycopg2
from psycopg2.extras import execute_batch

# Constants
USER_COUNT = 50
COURSE_COUNT = 20
ENROLLMENT_COUNT = 100
FEEDBACK_COUNT = 200
GROUP_COUNT = 10  
USER_GROUP_COUNT = 100
USER_COURSE_CONTENT_COUNT = 100
USER_COURSE_COUNT = 100
COURSE_CREATOR_COUNT = 5


# PostgreSQL connection parameters
HOST = 'localhost'  # Use 'localhost' instead of 'pg_container'
PORT = 5432
USER = 'postgres'
PASSWORD = ''  # Leave it empty if no password is set in docker-compose.yml
DB_NAME = 'teacher_community'  # Database name

# Establish connection to the PostgreSQL database
conn = psycopg2.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    dbname=DB_NAME
)

cur = conn.cursor()

# Initialize Faker instance
fake = Faker()

def random_passhash():
    """Generate a hashed password"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&',
            k=random.randint(8, 15)  # Password length between 8 and 15
        )
    )
    salt = secrets.token_hex(16)
    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def insert_course_creator():
    """Insert random course creators into the database"""
    print("Inserting course creators...")
    creators = []
    for _ in range(5):  # Assuming we want 5 course creators
        creators.append((
            fake.name(),
            fake.email(),
            fake.phone_number(),
            fake.address(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.country(),
            fake.date_this_decade()
        ))
    
    execute_batch(cur, """
        INSERT INTO course_creator_id (creator_name, creator_email, creator_phone_number, 
            creator_address, creator_city, creator_state, creator_zip_code, 
            creator_country, creator_created_on) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, creators)
    conn.commit()
    print("Course creators inserted.")


def insert_courses():
    """Insert random courses into the database"""
    print("Inserting courses...")
    courses = []
    for _ in range(COURSE_COUNT):
        creator_id = random.randint(1, 5)  # Random creator_id between 1 and 5
        courses.append((
            fake.company(),
            fake.text(),
            random.uniform(50.0, 500.0),
            fake.date_this_decade(),
            fake.date_this_decade(),
            creator_id
        ))

    execute_batch(cur, """
        INSERT INTO courses (course_name, course_description, course_price, 
            course_end_date, course_purchase_date, course_creator_id) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, courses)
    conn.commit()
    print("Courses inserted.")


def insert_users():
    with conn:
        with conn.cursor() as cur:
            users_data = []
            used_emails = set()  # Keep track of used emails to avoid duplicates
            for _ in range(USER_COUNT):  # Example: inserting 100 users
                email = fake.email()
                
                # Ensure the email is unique
                while email in used_emails:
                    email = fake.email()  # Generate a new email if it's a duplicate
                
                # Add email to the used_emails set
                used_emails.add(email)

                user_data = (
                    fake.first_name(),
                    fake.last_name(),
                    email,
                    fake.password(),
                    fake.phone_number(),
                    fake.address(),
                    fake.city(),
                    fake.state(),
                    fake.zipcode(),
                    fake.country(),
                    fake.date_this_decade(),
                    random.choice([True, False]),  # consent_for_marketing
                    random.choice(['student', 'instructor'])
                )
                users_data.append(user_data)

            query = """
                INSERT INTO users 
                (first_name, last_name, email, password, phone_number, address, city, state, zip_code, country, created_on, consent_for_marketing, role) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            try:
                execute_batch(cur, query, users_data)
            except psycopg2.errors.UniqueViolation as e:
                print(f"Error: Duplicate email found. {e}")




def insert_enrollments():
    """Insert random enrollments into the database"""
    print("Inserting enrollments...")
    enrollments = []
    for _ in range(ENROLLMENT_COUNT):
        course_id = random.randint(1, COURSE_COUNT)
        user_id = random.randint(1, USER_COUNT)
        enrollments.append((
            fake.date_this_year(),
            course_id,
            user_id,
            random.choice([True, False]),
            fake.date_this_year(),
            random.choice([True, False])
        ))

    execute_batch(cur, """
        INSERT INTO enrollments (enrollment_date, course_id, user_id, 
            payment_status, payment_date, completion_status) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, enrollments)
    conn.commit()
    print("Enrollments inserted.")


def insert_feedback():
    with conn:
        with conn.cursor() as cur:
            feedback_data = []
            for _ in range(FEEDBACK_COUNT):  # Example: inserting 200 feedback entries
                user_id = random.randint(1, 100)  # Assuming user IDs range from 1 to 100
                course_id = random.randint(1, 20)  # Assuming course IDs range from 1 to 20
                feedback_text = fake.sentence()
                feedback_date = fake.date_this_decade()  # Generate a random date for feedback_date
                
                # Generate a random rating between 1 and 5 (assuming rating is an integer)
                rating = random.randint(1, 5)

                # Check if the combination of user_id and course_id already exists
                cur.execute("""
                    SELECT 1 FROM feedback WHERE user_id = %s AND course_id = %s
                """, (user_id, course_id))

                if not cur.fetchone():  # If feedback does not exist, insert it
                    feedback_data.append((user_id, course_id, feedback_text, feedback_date, rating))
                else:
                    print(f"Feedback already exists for user_id={user_id}, course_id={course_id}")

            # Use ON CONFLICT to avoid duplicates and insert new feedback
            query = """
                INSERT INTO feedback (user_id, course_id, feedback_text, feedback_date, rating)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (user_id, course_id) DO NOTHING
            """
            execute_batch(cur, query, feedback_data)


def insert_consent_for_marketing():
    """Insert random consent for marketing entries into the database"""
    print("Inserting consent for marketing...")
    consents = []
    for user_id in range(1, USER_COUNT + 1):
        consents.append((
            fake.date_this_decade(),
            user_id,
            random.choice([True, False]),
            fake.date_this_decade()
        ))
    
    execute_batch(cur, """
        INSERT INTO consent_for_marketing (consent_date, user_id, consent, changed_on)
        VALUES (%s, %s, %s, %s)
    """, consents)
    conn.commit()
    print("Consent for marketing inserted.")


def insert_course_prerequisites():
    """Insert unique course prerequisites into the course_prerequisites table."""
    print("Inserting course prerequisites...")
    
    # Fetch existing course-prerequisite pairs to avoid inserting duplicates
    cur.execute("SELECT course_id, prerequisite_course_id FROM course_prerequisites")
    existing_prerequisites = set(cur.fetchall())  # Store existing pairs in a set
    
    course_prerequisite_data = set()  # To store new unique pairs
    
    # Generate unique course-prerequisite pairs
    for course_id in range(1, COURSE_COUNT + 1):
        # Select random prerequisite courses (excluding the course itself)
        num_prerequisites = random.randint(1, 3)  # Each course can have 1 to 3 prerequisites
        prerequisites = random.sample(range(1, COURSE_COUNT + 1), num_prerequisites)
        prerequisites = [p for p in prerequisites if p != course_id]  # Avoid self-prerequisite
        
        # Add unique pairs (course_id, prerequisite_course_id) to the set
        for prerequisite_course_id in prerequisites:
            # Only add if the pair does not already exist
            if (course_id, prerequisite_course_id) not in existing_prerequisites:
                course_prerequisite_data.add((course_id, prerequisite_course_id))
                existing_prerequisites.add((course_id, prerequisite_course_id))  # Add to set to track

    # Convert the set back to a list
    course_prerequisite_data = list(course_prerequisite_data)

    # If there are any new pairs, insert them into the database
    if course_prerequisite_data:
        query = """
            INSERT INTO course_prerequisites (course_id, prerequisite_course_id)
            VALUES (%s, %s)
        """
        execute_batch(cur, query, course_prerequisite_data)
        conn.commit()
        print("Course prerequisites inserted.")
    else:
        print("No new course prerequisites to insert.")


def insert_user_activity():
    """Insert random user activity into the database"""
    print("Inserting user activities...")
    activities = []
    for user_id in range(1, USER_COUNT + 1):
        activity_type = random.choice(["login", "course completion", "feedback submission", "profile update"])
        activities.append((
            user_id,
            activity_type,
            fake.date_this_decade()
        ))
    
    execute_batch(cur, """
        INSERT INTO user_activity (user_id, activity_type, activity_date)
        VALUES (%s, %s, %s)
    """, activities)
    conn.commit()
    print("User activities inserted.")


def insert_groups():
    """Insert random groups into the database"""
    print("Inserting groups...")
    groups = [
        ("Students", "Group for all students enrolled in courses."),
        ("Instructors", "Group for all course instructors."),
        ("Admins", "Group for system administrators.")
    ]
    
    execute_batch(cur, """
        INSERT INTO groups (group_name, group_description)
        VALUES (%s, %s)
    """, groups)
    conn.commit()
    print("Groups inserted.")


def insert_user_groups():
    with conn:
        with conn.cursor() as cur:
            user_group_data = []
            used_combinations = set()  # Track (user_id, group_id) pairs

            for _ in range(USER_GROUP_COUNT):  # Adjust USER_GROUP_COUNT as needed
                user_id = random.randint(1, USER_COUNT)
                group_id = random.randint(1, GROUP_COUNT)

                # Ensure this combination doesn't already exist
                while (user_id, group_id) in used_combinations:
                    user_id = random.randint(1, USER_COUNT)
                    group_id = random.randint(1, GROUP_COUNT)

                used_combinations.add((user_id, group_id))
                user_group_data.append((user_id, group_id))

            query = """
                INSERT INTO user_groups (user_id, group_id) 
                VALUES (%s, %s)
            """

            try:
                # Batch insert user-group data
                execute_batch(cur, query, user_group_data)
            except psycopg2.errors.UniqueViolation as e:
                print(f"Unique violation error: {e}")
                # Optionally: You can log this error or handle it specifically
                # For example, you can skip the duplicate entry and continue with the rest of the data
            except Exception as e:
                print(f"Error during insert: {e}")
                conn.rollback()  # Explicitly rollback the transaction if an error occurs




def insert_events():
    """Insert random events into the database"""
    print("Inserting events...")
    events = []
    for course_id in range(1, COURSE_COUNT + 1):
        events.append((
            course_id,
            fake.company() + " Event",
            fake.text(),
            fake.date_this_decade()
        ))
    
    execute_batch(cur, """
        INSERT INTO events (course_id, event_name, event_description, event_date)
        VALUES (%s, %s, %s, %s)
    """, events)
    conn.commit()
    print("Events inserted.")


def insert_event_enrollments():
    """Insert random event enrollments into the database"""
    print("Inserting event enrollments...")
    event_enrollments = []
    for user_id in range(1, USER_COUNT + 1):
        event_id = random.randint(1, COURSE_COUNT)  # Match event to a course
        event_enrollments.append((
            user_id,
            event_id
        ))
    
    execute_batch(cur, """
        INSERT INTO event_enrollments (user_id, event_id)
        VALUES (%s, %s)
    """, event_enrollments)
    conn.commit()
    print("Event enrollments inserted.")
    
def insert_user_course_creator():
    with conn:
        with conn.cursor() as cur:
            user_course_data = []
            used_combinations = set()  # Set to track (user_id, creator_id) pairs

            for _ in range(USER_COURSE_COUNT):  # Adjust USER_COURSE_COUNT as needed
                user_id = random.randint(1, USER_COUNT)  # Random user_id
                creator_id = random.randint(1, COURSE_CREATOR_COUNT)  # Random creator_id

                # Check if this combination has already been inserted
                while (user_id, creator_id) in used_combinations:
                    user_id = random.randint(1, USER_COUNT)
                    creator_id = random.randint(1, COURSE_CREATOR_COUNT)

                # Add the unique combination to the set
                used_combinations.add((user_id, creator_id))

                # Add the combination to the list for batch insert
                user_course_data.append((user_id, creator_id))

            query = """
                INSERT INTO user_course_creator (user_id, creator_id) 
                VALUES (%s, %s)
            """
            execute_batch(cur, query, user_course_data)


def main():
    """Main function to insert fake data"""
    insert_course_creator()
    insert_courses()
    insert_users()
    insert_enrollments()
    insert_feedback()
    insert_consent_for_marketing()
    insert_course_prerequisites()
    insert_user_activity()
    insert_groups()
    insert_user_groups()
    insert_events()
    insert_event_enrollments()
    insert_user_course_creator()  
    print("All data inserted successfully.")


# Run the script
if __name__ == "__main__":
    main()

    # Close the connection
    cur.close()
    conn.close()
