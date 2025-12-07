"""added db

Revision ID: d47aafac2b92
Revises: 
Create Date: 2025-11-09 21:19:00.093911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd47aafac2b92'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'tasks',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, default=sa.text('gen_random_uuid()')),
        sa.Column('title', sa.String, index=True),
        sa.Column('description', sa.String, index=True),
        sa.Column('status', sa.String, index=True),
        sa.Column('Date', sa.DateTime, server_default=sa.func.now())
    )
    op.alter_column

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('tasks')
