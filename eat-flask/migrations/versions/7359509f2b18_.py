"""empty message

Revision ID: 7359509f2b18
Revises: 36b486b542ad
Create Date: 2019-08-08 11:05:29.803009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7359509f2b18'
down_revision = '36b486b542ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('pwd', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('food', sa.String(length=255), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_addtime'), 'record', ['addtime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_record_addtime'), table_name='record')
    op.drop_table('record')
    op.drop_table('admin')
    # ### end Alembic commands ###
