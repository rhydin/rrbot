"""Create base tables

Revision ID: a2bc71b837b9
Revises: 
Create Date: 2020-09-10 13:17:47.716118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2bc71b837b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'channels',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('prefix', sa.String(10), nullable=True),
        sa.Column('muted', sa.Boolean, nullable=False, default=False),
        sa.Column('voiced', sa.Boolean, nullable=False, default=False),
        sa.Column('jsondata', sa.JSON)
    )
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('muted', sa.Boolean, nullable=False, default=False),
        sa.Column('voiced', sa.Boolean, nullable=False, default=False),
        sa.Column('moderator', sa.Boolean, nullable=False, default=False),
        sa.Column('jsondata', sa.JSON)
    )
    op.create_table(
        'servers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('prefix', sa.String(10), nullable=True),
        sa.Column('muted', sa.Boolean, nullable=False, default=False),
        sa.Column('jsondata', sa.JSON)
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('muted', sa.Boolean, nullable=False, default=False),
        sa.Column('voiced', sa.Boolean, nullable=False, default=False),
        sa.Column('moderator', sa.Boolean, nullable=False, default=False),
        sa.Column('jsondata', sa.JSON)
    )
    op.create_table(
        'warnings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False, index=True),
        sa.Column('server_id', sa.Integer, nullable=False, index=True),
        sa.Column('channel_id', sa.Integer, nullable=False, index=True),
        sa.Column('context', sa.Text, default='')
    )


def downgrade():
    op.drop_table('channels')
    op.drop_table('roles')
    op.drop_table('servers')
    op.drop_table('users')
    op.drop_table('warnings')
