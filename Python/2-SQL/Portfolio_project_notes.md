I have a website that has online courses in it.  I'd like to keep track of the people that register for my courses, all their contact information, what they enroll for and when, any feedback they had, and whether or not we can contact them with further course opportunities.  How would I set this up with the various relationships? 

Entities & Relationships
1. Users
Description: This table stores all the personal contact information of your users.

Attributes:

user_id (Primary Key, auto-generated)
first_name
last_name
email
phone_number
address
created_at (timestamp of registration)
consent_for_marketing (boolean to track whether they consent to be contacted for further opportunities)
Relationship:

1-to-many: A user can enroll in many courses (1 user, many enrollments).
1-to-many: A user can leave multiple feedbacks for courses (1 user, many feedbacks).
2. Courses
Description: This table holds information about the courses available on your platform.

Attributes:

course_id (Primary Key)
course_name
description
instructor_name
start_date
end_date
price
Relationship:

1-to-many: A course can have many enrollments (1 course, many enrollments).
1-to-many: A course can have multiple feedbacks (1 course, many feedbacks).
3. Enrollments
Description: This table tracks which users are enrolled in which courses and when they enrolled.

Attributes:

enrollment_id (Primary Key)
user_id (Foreign Key referencing Users)
course_id (Foreign Key referencing Courses)
enrollment_date (timestamp)
completion_status (e.g., "Completed", "In Progress", "Dropped")
payment_status (e.g., "Paid", "Pending")
Relationship:

Many-to-many: A user can enroll in many courses, and a course can have many users. This is achieved via the enrollments table.
4. Feedback
Description: This table stores feedback that users provide for the courses they have enrolled in.

Attributes:

feedback_id (Primary Key)
user_id (Foreign Key referencing Users)
course_id (Foreign Key referencing Courses)
rating (numerical rating, e.g., 1-5 stars)
comments (text of user feedback)
submitted_at (timestamp)
Relationship:

Many-to-one: A user can leave feedback for many courses, but a feedback record will belong to only one user and one course.
5. Consent
Description: This table tracks consent for marketing communications. While you can keep this field in the Users table, having a separate table makes it easy to manage consent histories (if applicable).

Attributes:

consent_id (Primary Key)
user_id (Foreign Key referencing Users)
consent_given (boolean, whether the user consented or not)
consent_date (timestamp)
Relationship:

1-to-1: Each user can have one consent record, meaning each user can give or revoke marketing consent.