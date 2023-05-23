import sqlite3
from dataframe_to_sql import df_to_sql

def modify_MAL():
    conn = None
    try:
        conn = sqlite3.connect('my_anime_list1.db')
        cur = conn.cursor()
        # Delete superfluous rows
        sql_delete = """DELETE FROM ani_rankings WHERE rank='Rank'"""
        # Add col for watch status
        sql_add_col = "ALTER table ani_rankings ADD COLUMN watched BOOLEAN NOT NULL DEFAULT FALSE"
        cur.execute(sql_delete)
        cur.execute(sql_add_col)
        #For printing
        cur.execute("SELECT * FROM ani_rankings")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except (Exception, sqlite3.Error) as err:
        print(err)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    df_to_sql()
    modify_MAL()