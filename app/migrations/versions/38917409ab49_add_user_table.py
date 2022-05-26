"""add user table

Revision ID: 38917409ab49
Revises: 
Create Date: 2022-05-24 09:25:00.252444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, DATETIME
from app.utils.date_utils import get_now

# revision identifiers, used by Alembic.
revision = '38917409ab49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        Column('id', INTEGER, primary_key=True, index=True, autoincrement=True),
        Column('email', VARCHAR(255), unique=True, nullable=False),
        Column('username', VARCHAR(255), nullable=True),
        Column('password', VARCHAR(255), nullable=False),
        Column('is_active', BOOLEAN, default=True),
        Column('is_superuser', BOOLEAN, default=False),
        Column('created_at', DATETIME, nullable=True, default=get_now),
        Column('updated_at', DATETIME, nullable=True, default=get_now, onupdate=get_now)
    )


def downgrade():
    pass
