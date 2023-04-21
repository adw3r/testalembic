"""added user_info field to users table

Revision ID: 1ed9f3ba0fd4
Revises: c53d2634bcba
Create Date: 2023-04-21 13:43:17.547261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ed9f3ba0fd4'
down_revision = 'c53d2634bcba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_info', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_info')
    # ### end Alembic commands ###
