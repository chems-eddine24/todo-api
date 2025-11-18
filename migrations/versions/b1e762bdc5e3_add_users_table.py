"""add users table

Revision ID: b1e762bdc5e3
Revises: d47aafac2b92
Create Date: 2025-11-18 11:31:05.781134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as UUid
import uuid



# revision identifiers, used by Alembic.
revision: str = 'b1e762bdc5e3'
down_revision: Union[str, Sequence[str], None] = 'd47aafac2b92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', UUid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4),
        sa.Column('email', sa.String, unique=True, index=True, nullable=False),
        sa.Column('password_hash', sa.String, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
