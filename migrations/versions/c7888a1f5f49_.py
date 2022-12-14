"""empty message

Revision ID: c7888a1f5f49
Revises: 5d194b7f8c35
Create Date: 2022-08-11 10:04:39.083829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7888a1f5f49'
down_revision = '5d194b7f8c35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('height', sa.String(length=100), nullable=False),
    sa.Column('mass', sa.String(length=100), nullable=False),
    sa.Column('hair_color', sa.String(length=100), nullable=False),
    sa.Column('skin_color', sa.String(length=100), nullable=False),
    sa.Column('eye', sa.String(length=100), nullable=False),
    sa.Column('birth_year', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('birth_year'),
    sa.UniqueConstraint('birth_year'),
    sa.UniqueConstraint('eye'),
    sa.UniqueConstraint('eye'),
    sa.UniqueConstraint('gender'),
    sa.UniqueConstraint('gender'),
    sa.UniqueConstraint('hair_color'),
    sa.UniqueConstraint('hair_color'),
    sa.UniqueConstraint('height'),
    sa.UniqueConstraint('height'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('skin_color'),
    sa.UniqueConstraint('skin_color')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###
