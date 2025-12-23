import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_IAS(conn, entity):
    """
    update IAS of an entity
    :param conn:
    :param entity:
    :return: entity id
    """
    sql = ''' UPDATE entities
              SET IAS = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, entity)
    conn.commit()

def update_PAS(conn, entity, update_amount):
    """
    update PAS of an entity
    :param conn:
    :param entity:
    :return: entity id
    """

    

    sql = ''' UPDATE entities
              SET PAS = ?
              WHERE name = ?'''
    cur = conn.cursor()
    ent_PAS = cur.execute(f"SELECT PAS FROM entities WHERE name=?", [entity]).fetchall()[0][0]
    cur.execute(sql, (update_amount+ent_PAS, entity))
    conn.commit()


def update_elo(update_amount, ent_id):
    database = r"/home/debin/WebCrawling/Entities.db"
    
    conn = create_connection(database)
    cur = conn.cursor()
    ent_IAS = cur.execute(f"SELECT IAS FROM entities WHERE id = {ent_id}").fetchall()[0][0]

    with conn:
        update_IAS(conn, (update_amount+ent_IAS, ent_id))

