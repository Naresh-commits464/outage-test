import psycopg2
from settings import DATABASE_URL, STRIPE_API_KEY


def run():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM orders")
    print(cur.fetchone())


if __name__ == "__main__":
    run()
