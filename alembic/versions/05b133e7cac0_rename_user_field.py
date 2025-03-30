"""Rename user field

Revision ID: 05b133e7cac0
Revises: d7cebe77233b
Create Date: 2025-03-28 15:29:51.739159

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "05b133e7cac0"
down_revision: Union[str, None] = "d7cebe77233b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("hashed_password", sa.String(), nullable=True))
    op.drop_column("users", "password")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.drop_column("users", "hashed_password")
    # ### end Alembic commands ###
