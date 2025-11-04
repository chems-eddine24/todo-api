"""added a db

Revision ID: 9690711caa48
Revises: 
Create Date: 2025-11-04 18:43:37.148454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9690711caa48'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'tasks',
        sa.Column('id', sa.Uuid, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('description', sa.String, index=True),
        sa.Column('status', sa.String, index=True),
        sa.Column('created_date', sa.DateTime, server_default=sa.func.now())
    )
    

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('tasks')