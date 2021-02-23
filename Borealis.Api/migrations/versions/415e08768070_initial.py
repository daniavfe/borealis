"""initial

Revision ID: 415e08768070
Revises: 
Create Date: 2021-02-10 20:01:17.213273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '415e08768070'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('districts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surface', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('holidays',
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('day_of_week', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('scope', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('date')
    )
    op.create_table('pollution_magnitudes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('formula', sa.String(length=5), nullable=False),
    sa.Column('measurement_unit', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pollution_stations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('latitude', sa.String(length=20), nullable=True),
    sa.Column('longitude', sa.String(length=20), nullable=True),
    sa.Column('altitude', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('neighborhoods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surface', sa.Float(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pollution_measurements',
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('magnitude_id', sa.Integer(), nullable=False),
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Float(), nullable=False),
    sa.Column('validation_code', sa.String(length=1), nullable=False),
    sa.ForeignKeyConstraint(['magnitude_id'], ['pollution_magnitudes.id'], ),
    sa.ForeignKeyConstraint(['station_id'], ['pollution_stations.id'], ),
    sa.PrimaryKeyConstraint('datetime', 'magnitude_id', 'station_id')
    )
    op.create_table('pollution_stations_magnitudes',
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.Column('magnitude_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['magnitude_id'], ['pollution_magnitudes.id'], ),
    sa.ForeignKeyConstraint(['station_id'], ['pollution_stations.id'], ),
    sa.PrimaryKeyConstraint('station_id', 'magnitude_id')
    )
    op.create_table('densities',
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('neighborhood_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ),
    sa.ForeignKeyConstraint(['neighborhood_id'], ['neighborhoods.id'], ),
    sa.PrimaryKeyConstraint('district_id', 'neighborhood_id', 'year', 'month')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('densities')
    op.drop_table('pollution_stations_magnitudes')
    op.drop_table('pollution_measurements')
    op.drop_table('neighborhoods')
    op.drop_table('pollution_stations')
    op.drop_table('pollution_magnitudes')
    op.drop_table('holidays')
    op.drop_table('districts')
    # ### end Alembic commands ###