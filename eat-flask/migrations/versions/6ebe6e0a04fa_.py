"""empty message

Revision ID: 6ebe6e0a04fa
Revises: 
Create Date: 2019-08-05 16:36:36.355365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ebe6e0a04fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('openid', sa.String(length=50), nullable=True),
    sa.Column('nickname', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_user_addtime'), 'user', ['addtime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_addtime'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###