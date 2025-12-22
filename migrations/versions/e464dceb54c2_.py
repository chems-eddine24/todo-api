"""empty message

Revision ID: e464dceb54c2
Revises: b1e762bdc5e3
Create Date: 2025-12-18 11:19:43.283198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e464dceb54c2'
down_revision: Union[str, Sequence[str], None] = 'b1e762bdc5e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('tasks', sa.Column('user_id', sa.Uuid(), sa.ForeignKey('users.id'), nullable=True))
    op.create_foreign_key(None, 'tasks', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('tasks', 'user_id')
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    