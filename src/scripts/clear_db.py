import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from database import Base
from config import settings


DATABASE_URL = settings.get_db_url()

engine = create_async_engine(DATABASE_URL)

metadata = Base.metadata


async def truncate_all_tables():
    print('Clearing all tables...')
    async with engine.begin() as conn:
        await conn.execute(text(f'TRUNCATE TABLE news, comments RESTART IDENTITY CASCADE;'))
    print('Done')
    

if __name__ == '__main__':
    confirm = input('WARNING: This will CLEAR ALL DATA FROM ALL TABLES. Are you sure? [y/n]: ')
    if confirm.lower() == 'y':
        asyncio.run(truncate_all_tables())
    else:
        print('Operation cancelled')