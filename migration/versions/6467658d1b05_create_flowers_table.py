"""create tables for the application

Revision ID: 123456789abc
Revises: None
Create Date: 2024-11-20 02:04:32.665570

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'bouquets',
        sa.Column('BouquetsID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('BouquetName', sa.String(length=255), nullable=False),
        sa.Column('BouquetLifeSpan', sa.Integer(), nullable=False),
        sa.Column('BouquetInfo', sa.String(length=255), nullable=False),
        sa.Column('BouquetStock', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('BouquetsID'),
        schema='my_app_schema'
    )

    op.create_table(
        'customers',
        sa.Column('CustomersID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('CustomerName', sa.String(length=255), nullable=False),
        sa.Column('CustomerAdres', sa.String(length=255), nullable=False),
        sa.Column('CustomerSumm', sa.Numeric(precision=15, scale=2), nullable=False),
        sa.Column('CustomerPhone', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('CustomersID'),
        schema='my_app_schema'
    )

    op.create_table(
        'employees',
        sa.Column('EmployeesID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('EmployeeName', sa.String(length=255), nullable=False),
        sa.Column('EmployeePosition', sa.String(length=255), nullable=False),
        sa.Column('EmployeeSalaries', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('EmployeeStash', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('EmployeesID'),
        schema='my_app_schema'
    )

    op.create_table(
        'provider',
        sa.Column('ProviderID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('ProviderType', sa.String(length=255), nullable=False),
        sa.Column('ProviderName', sa.String(length=255), nullable=False),
        sa.Column('ProviderEmail', sa.String(length=255), nullable=False),
        sa.Column('ProviderAdres', sa.String(length=255), nullable=False),
        sa.Column('ProviderNumber', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('ProviderID'),
        schema='my_app_schema'
    )

    op.create_table(
        'provider_add',
        sa.Column('ProviderAddID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('ProviderAddStack', sa.Integer(), nullable=False),
        sa.Column('ProviderAddDate', sa.Date(), nullable=False),
        sa.Column('ProviderAddProductID', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('ProviderAddID'),
        schema='my_app_schema'
    )

    op.create_table(
        'provider_flowers',
        sa.Column('ProviderFlowersID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('ProvidersFlowerStack', sa.Integer(), nullable=False),
        sa.Column('ProvidersFlowerDate', sa.Date(), nullable=False),
        sa.Column('ProvidersFlowerFlowerID', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('ProviderFlowersID'),
        schema='my_app_schema'
    )

    op.create_table(
        'additional_products',
        sa.Column('AdditionalProductsID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('AdditionalProductName', sa.String(length=255), nullable=False),
        sa.Column('AdditionalProductStock', sa.Integer(), nullable=False),
        sa.Column('ProviderAddID', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['ProviderAddID'], ['my_app_schema.provider_add.ProviderAddID']),
        sa.PrimaryKeyConstraint('AdditionalProductsID'),
        schema='my_app_schema'
    )

    op.create_table(
        'bouquets_purchase',
        sa.Column('BouquetsPurchaseID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('CheckID', sa.Integer(), nullable=False),
        sa.Column('BouquetID', sa.Integer(), nullable=False),
        sa.Column('BouquetQuantity', sa.Integer(), nullable=False),
        sa.Column('BouquetPrice', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.ForeignKeyConstraint(['BouquetID'], ['my_app_schema.bouquets.BouquetsID']),
        sa.PrimaryKeyConstraint('BouquetsPurchaseID'),
        schema='my_app_schema'
    )

    op.create_table(
        'flowers',
        sa.Column('FlowersID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('FlowersName', sa.String(length=255), nullable=False),
        sa.Column('FlowerLifeSpan', sa.Integer(), nullable=False),
        sa.Column('FlowerStock', sa.Integer(), nullable=False),
        sa.Column('ProviderFlowerID', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['ProviderFlowerID'], ['my_app_schema.provider_flowers.ProviderFlowersID']),
        sa.PrimaryKeyConstraint('FlowersID'),
        schema='my_app_schema'
    )

    op.create_table(
        'additional_products_purchase',
        sa.Column('AdditionalProductsPurchaseID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('CheckID', sa.Integer(), nullable=False),
        sa.Column('AdditionalProductsID', sa.Integer(), nullable=False),
        sa.Column('AdditionalProductsPrice', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.ForeignKeyConstraint(['AdditionalProductsID'], ['my_app_schema.additional_products.AdditionalProductsID']),
        sa.PrimaryKeyConstraint('AdditionalProductsPurchaseID'),
        schema='my_app_schema'
    )

    op.create_table(
        'flowers_purchase',
        sa.Column('FlowersPurchaseID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('CheckID', sa.Integer(), nullable=False),
        sa.Column('FlowerID', sa.Integer(), nullable=False),
        sa.Column('FlowerQuantity', sa.Integer(), nullable=False),
        sa.Column('FlowerPrice', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.ForeignKeyConstraint(['FlowerID'], ['my_app_schema.flowers.FlowersID']),
        sa.PrimaryKeyConstraint('FlowersPurchaseID'),
        schema='my_app_schema'
    )

    op.create_table(
        'total_checks',
        sa.Column('TotalChecksID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('CashRegisterID', sa.Integer(), nullable=False),
        sa.Column('FlowersPurchaseID', sa.Integer(), nullable=False),
        sa.Column('AdditionalProductsPurchaseID', sa.Integer(), nullable=False),
        sa.Column('BouquetsPurchaseID', sa.Integer(), nullable=False),
        sa.Column('PurchaseDate', sa.Date(), nullable=False),
        sa.Column('TotalCost', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('EmployeesID', sa.Integer(), nullable=False),
        sa.Column('CustomersID', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['AdditionalProductsPurchaseID'], ['my_app_schema.additional_products_purchase.AdditionalProductsPurchaseID']),
        sa.ForeignKeyConstraint(['BouquetsPurchaseID'], ['my_app_schema.bouquets_purchase.BouquetsPurchaseID']),
        sa.ForeignKeyConstraint(['CustomersID'], ['my_app_schema.customers.CustomersID']),
        sa.ForeignKeyConstraint(['EmployeesID'], ['my_app_schema.employees.EmployeesID']),
        sa.ForeignKeyConstraint(['FlowersPurchaseID'], ['my_app_schema.flowers_purchase.FlowersPurchaseID']),
        sa.PrimaryKeyConstraint('TotalChecksID'),
        schema='my_app_schema'
    )

    op.create_table(
        'delivery_checks',
        sa.Column('TotalChecksID', sa.Integer(), nullable=False),
        sa.Column('DeliveryID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('CourierID', sa.Integer(), nullable=False),
        sa.Column('CustomersID', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['CourierID'], ['my_app_schema.employees.EmployeesID']),
        sa.ForeignKeyConstraint(['CustomersID'], ['my_app_schema.customers.CustomersID']),
        sa.ForeignKeyConstraint(['TotalChecksID'], ['my_app_schema.total_checks.TotalChecksID']),
        sa.PrimaryKeyConstraint('DeliveryID'),
        schema='my_app_schema'
    )

def downgrade():
    op.drop_table('delivery_checks', schema='my_app_schema')
    op.drop_table('total_checks', schema='my_app_schema')
    op.drop_table('flowers_purchase', schema='my_app_schema')
    op.drop_table('additional_products_purchase', schema='my_app_schema')
    op.drop_table('flowers', schema='my_app_schema')
    op.drop_table('bouquets_purchase', schema='my_app_schema')
    op.drop_table('additional_products', schema='my_app_schema')
    op.drop_table('provider_flowers', schema='my_app_schema')
    op.drop_table('provider_add', schema='my_app_schema')
    op.drop_table('provider', schema='my_app_schema')
    op.drop_table('employees', schema='my_app_schema')
    op.drop_table('customers', schema='my_app_schema')
    op.drop_table('bouquets', schema='my_app_schema')