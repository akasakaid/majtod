import asyncio
import aiosqlite
from pathlib import Path

loop = asyncio.new_event_loop()
database = Path(__file__).parent.joinpath("database.sqlite3")


async def get_by_id(id):
    query = """
    SELECT * FROM "main"."accounts" WHERE rowid = ?
    """
    values = (id,)
    async with aiosqlite.connect(database=database) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query, values) as cur:
            res = await cur.fetchone()
            if res is None:
                data = None
            else:
                data = {
                    "id": res["id"],
                    "first_name": res["first_name"],
                    "balance": res["balance"],
                    "token": res["token"],
                    "useragent": res["useragent"],
                }
            return data


async def get_all():
    query = """
    SELECT * FROM "main"."accounts"
    """
    out = []
    async with aiosqlite.connect(database=database) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query) as cur:
            result = await cur.fetchall()
            for res in result:
                out.append(
                    {
                        "id": res["id"],
                        "first_name": res["first_name"],
                        "balance": res["balance"],
                    }
                )
            return out


async def insert(id, first_name):
    query = """
    INSERT INTO "main"."accounts" ("id", "first_name") VALUES (?, ?)
    """
    values = (
        id,
        first_name,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def update_balance(id, balance):
    query = """
    UPDATE "main"."accounts" SET "balance" = ? WHERE rowid = ?
    """
    values = (
        balance,
        id,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def update_token(id, token):
    query = """
    UPDATE "main"."accounts" SET "token" = ? WHERE rowid = ?
    """
    values = (
        token,
        id,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def update_useragent(id, useragent):
    query = """
    UPDATE "main"."accounts" SET "useragent" = ? WHERE rowid = ?
    """
    values = (
        useragent,
        id,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def init():
    query0 = "SELECT * FROM accounts IF "
    query1 = """
    CREATE TABLE IF NOT EXISTS "accounts" (
        "id" INTEGER NOT NULL,
        "first_name" TEXT NULL,
        "balance" TEXT NULL,
        "token" TEXT NULL,
        "useragent" TEXT NULL,
        PRIMARY KEY ("id")
    ); 
    """
    query2 = "PRAGMA foreign_keys = true;"
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query1)
        await db.execute(query2)
        await db.commit()


class Config:
    def __init__(self, auto_task):
        self.auto_task = auto_task
