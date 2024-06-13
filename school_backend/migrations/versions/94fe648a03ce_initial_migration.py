"""Initial migration.

Revision ID: 94fe648a03ce
Revises: 
Create Date: 2024-06-13 18:28:48.542417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94fe648a03ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('endereco', sa.String(length=200), nullable=True),
    sa.Column('ano_letivo', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('materia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prova',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_aluno', sa.Integer(), nullable=False),
    sa.Column('id_materia', sa.Integer(), nullable=False),
    sa.Column('nota', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_aluno'], ['aluno.id'], ),
    sa.ForeignKeyConstraint(['id_materia'], ['materia.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prova')
    op.drop_table('materia')
    op.drop_table('aluno')
    # ### end Alembic commands ###
