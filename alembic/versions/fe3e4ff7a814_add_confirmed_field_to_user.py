"""Add confirmed field to User

Revision ID: fe3e4ff7a814
Revises: 05b133e7cac0
Create Date: 2025-03-28 20:43:09.744614

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fe3e4ff7a814"
down_revision: Union[str, None] = "05b133e7cac0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("confirmed", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "confirmed")
    # ### end Alembic commands ###
