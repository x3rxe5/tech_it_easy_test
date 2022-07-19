"""init

Revision ID: ca5de7317f00
Revises: 
Create Date: 2022-07-19 13:59:25.953142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca5de7317f00'
down_revision = None
branch_labels = None
depends_on = None



def upgrade() -> None:

    op.create_table(
        'bilty_master',
        sa.Column('bilty_id',sa.Integer,primary_key=True),
        sa.Column('bilty_no',sa.Integer,nullable=False),
        sa.Column('bill_type',sa.Integer,nullable=False),
        sa.Column('amt',sa.Integer,nullable=False),
    )

    op.create_table(
        'chalan_master',
        sa.Column('chalan_id',sa.Integer,primary_key=True),
        sa.Column('chalan_no',sa.Integer,nullable=False),
        sa.Column('chalan_date',sa.DateTime,nullable=False),
        sa.Column('inwarded',sa.Integer,nullable=False),
        sa.Column('created_from',sa.Integer,nullable=False),
    )

    op.create_table(
        'vehicle_master',
        sa.Column('vehicle_id',sa.Integer,primary_key=True),
        sa.Column('vehicle_no',sa.Integer,nullable=False),
        sa.Column('owner_name',sa.String,nullable=False)
    )

    op.create_table(
        'branch',
        sa.Column('branch_id',sa.Integer,primary_key=True),
        sa.Column('branch_name',sa.String,nullable=False)
    )


def downgrade() -> None:
    op.drop_table("bilty_master")
    op.drop_table("chalan_master")
    op.drop_table("vehicle_master")
    op.drop_table("branch")