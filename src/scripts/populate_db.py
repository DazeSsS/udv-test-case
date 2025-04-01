import json
import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.data.models import Comment, News
from app.domain.entities import CommentResponse, NewsResponse
from config import settings


DATABASE_URL = settings.get_db_url()

engine = create_async_engine(DATABASE_URL)


async def upload_news(session: AsyncSession):
    print('Deleting news data...')
    await session.execute(text('TRUNCATE TABLE news RESTART IDENTITY CASCADE;'))
    await session.commit()

    print('Reading news.json...')
    with open('src/seed_data/news.json', 'r', encoding='utf-8') as file:
        news_data = json.load(file)

    news_list = news_data.get('news')
    async with session.begin():
        for idx, news in enumerate(news_list):
            news_schema = NewsResponse(**news)
            news_obj = News(**news)
            session.add(news_obj)
            print(f'Loading news {idx+1}/{len(news_list)}')

async def upload_comments(session: AsyncSession):
    print('Deleting comments data...')
    await session.execute(text('TRUNCATE TABLE comments RESTART IDENTITY CASCADE;'))
    await session.commit()

    print('Reading comments.json...')
    with open('src/seed_data/comments.json', 'r', encoding='utf-8') as file:
        comments_data = json.load(file)

    comments_list = comments_data.get('comments')
    async with session.begin():
        for idx, comment in enumerate(comments_list):
            comment_schema = CommentResponse(**comment)
            comment_obj = Comment(**comment)
            session.add(comment_obj)
            print(f'Loading comments {idx+1}/{len(comments_list)}')

async def populate():
    async with AsyncSession(engine) as session:
        await upload_news(session)
        await upload_comments(session)


if __name__ == '__main__':
    confirm = input('WARNING: This will REPLACE ALL EXISTING DATA with start seed data. Are you sure? [y/n]: ')
    if confirm.lower() == 'y':
        asyncio.run(populate())
    else:
        print('Operation cancelled.')
