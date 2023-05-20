"""removed email and password added access_token

Revision ID: 42494b5bec14
Revises: f392218bdfa7
Create Date: 2023-05-20 08:34:37.992840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42494b5bec14'
down_revision = 'f392218bdfa7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('access_token', sa.UUID(), nullable=True))
    op.drop_index('ix_user_email', table_name='user')
    op.create_index(op.f('ix_user_access_token'), 'user', ['access_token'], unique=True)
    op.drop_column('user', 'email')
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_access_token'), table_name='user')
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.drop_column('user', 'access_token')
    # ### end Alembic commands ###
