import asyncio
import aiosqlite
from pathlib import Path

loop = asyncio.new_event_loop()
database = Path(__file__).parent.joinpath("database.sqlite3")


async def get_by_id(id):
    query = """
    SELECT * FROM "main"."reports" WHERE rowid = ?
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
                }
            return data


async def get_all():
    query = """
    SELECT * FROM "main"."reports"
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


async def insert(id, first_name, balance):
    query = """
    INSERT INTO "main"."reports" ("id", "first_name", "balance") VALUES (?, ?, ?)
    """
    values = (
        id,
        first_name,
        balance,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


async def update(id, balance):
    query = """
    UPDATE "main"."reports" SET "balance" = ? WHERE rowid = ?
    """
    values = (
        balance,
        id,
    )
    async with aiosqlite.connect(database=database) as db:
        await db.execute(query, values)
        await db.commit()


# asyncio.run(get_by_id(1))


class Config:
    def __init__(self, auto_task):
        self.auto_task = auto_task
