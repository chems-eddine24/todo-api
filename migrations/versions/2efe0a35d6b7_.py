"""empty message

Revision ID: 2efe0a35d6b7
Revises: df8931d574d5
Create Date: 2025-12-21 11:41:39.126244

"""
from typing import Sequence, Union
from sqlalchemy import DateTime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2efe0a35d6b7'
down_revision: Union[str, Sequence[str], None] = 'df8931d574d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('tasks', 'date',
               existing_type=sa.DateTime(),
               type_=DateTime(timezone=True),
               nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('tasks', 'date',
               existing_type=DateTime(timezone=True),
               type_=sa.DateTime(),
               nullable=True)   
