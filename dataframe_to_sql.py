from scrape_my_anime import scrape_mal
import sqlite3


def df_to_sql():
    conn = None
    try:
        conn = sqlite3.connect('my_anime_list.db')
        df = scrape_mal()
        df.to_sql(name='ani_rankings', con=conn, if_exists='replace', index=False)
        conn.commit()
    except (Exception, sqlite3.Error) as err:
        print(err)
    finally:
        if conn:
            conn.close()
# if __name__ == "__main__":
#     df_to_sql()