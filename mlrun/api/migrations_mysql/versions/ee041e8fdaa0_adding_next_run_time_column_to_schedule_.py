"""adding next_run_time column to schedule table

Revision ID: ee041e8fdaa0
Revises: 5f1351c88a19
Create Date: 2022-08-16 17:56:47.826661

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "ee041e8fdaa0"
down_revision = "5f1351c88a19"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "schedules_v2",
        sa.Column("next_run_time", mysql.TIMESTAMP(fsp=3), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("schedules_v2", "next_run_time")
    # ### end Alembic commands ###