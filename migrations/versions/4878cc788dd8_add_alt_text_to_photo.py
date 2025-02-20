"""add alt_text to photo

Revision ID: 4878cc788dd8
Revises: 
Create Date: 2025-02-13 13:55:04.200136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4878cc788dd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.alter_column('alt_text',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.alter_column('alt_text',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###
