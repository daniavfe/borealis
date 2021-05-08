"""initital

Revision ID: eea40f0056a9
Revises: 
Create Date: 2021-05-08 02:48:00.602938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eea40f0056a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('districts',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surface', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('events',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('event_type', sa.String(length=100), nullable=False),
    sa.Column('details', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('holidays',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('day_of_week', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('scope', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('date')
    )
    op.create_table('magnitudes',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('formula', sa.String(length=5), nullable=True),
    sa.Column('measurement_unit', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timelines',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('life_start', sa.DateTime(), nullable=False),
    sa.Column('life_end', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('details', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('neighborhoods',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surface', sa.Float(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('densities',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('neighborhood_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ),
    sa.ForeignKeyConstraint(['neighborhood_id'], ['neighborhoods.id'], ),
    sa.PrimaryKeyConstraint('district_id', 'neighborhood_id', 'year', 'month')
    )
    op.create_table('stations',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('latitude', sa.String(length=20), nullable=True),
    sa.Column('longitude', sa.String(length=20), nullable=True),
    sa.Column('altitude', sa.Integer(), nullable=True),
    sa.Column('neighborhood_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['neighborhood_id'], ['neighborhoods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('measurements',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('town_id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('magnitude_id', sa.Integer(), nullable=False),
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Float(), nullable=False),
    sa.Column('validation_code', sa.String(length=1), nullable=False),
    sa.ForeignKeyConstraint(['magnitude_id'], ['magnitudes.id'], ),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('town_id', 'datetime', 'magnitude_id', 'station_id')
    )
    op.create_table('stations_magnitudes',
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.Column('magnitude_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['magnitude_id'], ['magnitudes.id'], ),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('station_id', 'magnitude_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stations_magnitudes')
    op.drop_table('measurements')
    op.drop_table('stations')
    op.drop_table('densities')
    op.drop_table('neighborhoods')
    op.drop_table('timelines')
    op.drop_table('magnitudes')
    op.drop_table('holidays')
    op.drop_table('events')
    op.drop_table('districts')
    # ### end Alembic commands ###