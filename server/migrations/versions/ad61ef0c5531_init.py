"""init

Revision ID: ad61ef0c5531
Revises: 
Create Date: 2021-02-04 11:46:35.574891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad61ef0c5531'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.Unicode(), nullable=False),
        sa.Column('password', sa.Unicode(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(), nullable=False),
        sa.Column('count', sa.Integer(), nullable=False),
        sa.Column('price', sa.Numeric(10,2), nullable=False),
        sa.Column('date_add', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('user')
    op.drop_table('product')
