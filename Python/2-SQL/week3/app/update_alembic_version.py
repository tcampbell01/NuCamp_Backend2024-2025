import psycopg2

def update_alembic_version(new_version):
    try:
        # Connect to your PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="",  # Add your password if required
            host="pg",
            port="5432",
            database="week3"
        )
        cursor = connection.cursor()

        # Update the alembic_version table
        update_query = f"UPDATE alembic_version SET version_num = '{new_version}';"
        cursor.execute(update_query)
        connection.commit()

        print(f"Successfully updated alembic_version to {new_version}")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    new_version = "45bd4c0c6235"  # Replace with the desired revision ID
    update_alembic_version(new_version)