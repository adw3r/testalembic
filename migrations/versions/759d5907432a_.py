"""'...'

Revision ID: 759d5907432a
Revises: 9ca990a7e964
Create Date: 2023-04-21 13:59:26.934855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '759d5907432a'
down_revision = '9ca990a7e964'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('surname', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('user_info', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('advertisements',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('advertisements')
    op.drop_table('users')
    # ### end Alembic commands ###
