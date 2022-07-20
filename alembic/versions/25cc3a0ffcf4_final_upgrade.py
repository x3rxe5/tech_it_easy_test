"""final_upgrade

Revision ID: 25cc3a0ffcf4
Revises: 64326adc7730
Create Date: 2022-07-20 13:55:46.194502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25cc3a0ffcf4'
down_revision = '64326adc7730'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        'bilty_master',
        sa.Column('bilty_id',sa.Integer,primary_key=True),
        sa.Column('bilty_no',sa.Integer,nullable=False),
        sa.Column('bill_type',sa.Integer,nullable=False),
        sa.Column('amt',sa.Integer,nullable=False),
        sa.Column("chalan_id",sa.Integer,nullable=False),

        # sa.PrimaryKeyConstraint('bilty_id'),
        # sa.ForeignKeyConstraint(['chalan_id','chalan_master.chalan_id'],)

    )

    op.create_table(
        'chalan_master',
        sa.Column('chalan_id',sa.Integer,primary_key=True),
        sa.Column('chalan_no',sa.Integer,nullable=False),
        sa.Column('chalan_date',sa.DateTime,nullable=False),
        sa.Column('inwarded',sa.Integer,nullable=False),
        sa.Column('created_from',sa.Integer,nullable=False),
        sa.Column('station_from',sa.Integer,nullable=False),
        sa.Column('station_to',sa.Integer,nullable=False),
        sa.Column('vehicle_id',sa.Integer,nullable=False),

        # sa.PrimaryKeyConstraint('chalan_id'),
        # sa.ForeignKeyConstraint(
        #     ['station_from','branch.branch_id'], 
        #     ['station_to','branch.branch_id'],
        #     ['vehicle_id','vehicle_master.vehicle_id']
        # ),


    )

    op.create_table(
        'vehicle_master',
        sa.Column('vehicle_id',sa.Integer,primary_key=True),
        sa.Column('vehicle_no',sa.Integer,nullable=False),
        sa.Column('owner_name',sa.String,nullable=False),
        
        # sa.PrimaryKeyConstraint('vehicle_id'),

    )

    op.create_table(
        'branch',
        sa.Column('branch_id',sa.Integer,primary_key=True),
        sa.Column('branch_name',sa.String,nullable=False),
        
        # sa.PrimaryKeyConstraint('branch_id'),

    )


def downgrade() -> None:
    op.drop_table("bilty_master")
    op.drop_table("chalan_master")
    op.drop_table("vehicle_master")
    op.drop_table("branch")