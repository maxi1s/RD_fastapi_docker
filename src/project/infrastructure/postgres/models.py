from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Numeric, Date
from project.infrastructure.postgres.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=True)

class Study(Base):
    __tablename__ = "studies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

class UserMarks(Base):
    __tablename__ = "user_marks"

    id: Mapped[int] = mapped_column(primary_key=True)
    mark: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"))
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.id", ondelete="CASCADE", onupdate="CASCADE"))

class Provider(Base):
    __tablename__ = 'provider'
    
    id: Mapped[int] = mapped_column('ProviderID', Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column('ProviderType', String(255))
    name: Mapped[str] = mapped_column('ProviderName', String(255))
    email: Mapped[str] = mapped_column('ProviderEmail', String(255))
    address: Mapped[str] = mapped_column('ProviderAdres', String(255))
    number: Mapped[str] = mapped_column('ProviderNumber', String(255))

class ProviderFlowers(Base):
    __tablename__ = 'provider_flowers'
    
    id: Mapped[int] = mapped_column('ProviderFlowersID', Integer, primary_key=True, autoincrement=True)
    stack: Mapped[int] = mapped_column('ProvidersFlowerStack', Integer)
    date: Mapped[Date] = mapped_column('ProvidersFlowerDate', Date)
    flower_id: Mapped[int] = mapped_column('ProvidersFlowerFlowerID', Integer)

class ProviderAdd(Base):
    __tablename__ = 'provider_add'
    
    id: Mapped[int] = mapped_column('ProviderAddID', Integer, primary_key=True, autoincrement=True)
    stack: Mapped[int] = mapped_column('ProviderAddStack', Integer)
    date: Mapped[Date] = mapped_column('ProviderAddDate', Date)
    product_id: Mapped[int] = mapped_column('ProviderAddProductID', Integer)

class Flowers(Base):
    __tablename__ = 'flowers'
    
    id: Mapped[int] = mapped_column('FlowersID', Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column('FlowersName', String(255))
    lifespan: Mapped[int] = mapped_column('FlowerLifeSpan', Integer)
    stock: Mapped[int] = mapped_column('FlowerStock', Integer)
    provider_flower_id: Mapped[int] = mapped_column('ProviderFlowerID', Integer, ForeignKey('provider_flowers.ProviderFlowersID'))
    flower_price: Mapped[int] = mapped_column('FlowerPrice', Integer)

class FlowersPurchase(Base):
    __tablename__ = 'flowers_purchase'
    
    id: Mapped[int] = mapped_column('FlowersPurchaseID', Integer, primary_key=True, autoincrement=True)
    check_id: Mapped[int] = mapped_column('CheckID', Integer)
    flower_id: Mapped[int] = mapped_column('FlowerID', Integer, ForeignKey('flowers.FlowersID'))
    quantity: Mapped[int] = mapped_column('FlowerQuantity', Integer)
    price: Mapped[Numeric] = mapped_column('FlowerPrice', Numeric(10, 2))

class AdditionalProducts(Base):
    __tablename__ = 'additional_products'
    
    id: Mapped[int] = mapped_column('AdditionalProductsID', Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column('AdditionalProductName', String(255))
    stock: Mapped[int] = mapped_column('AdditionalProductStock', Integer)
    provider_add_id: Mapped[int] = mapped_column('ProviderAddID', Integer, ForeignKey('provider_add.ProviderAddID'))

class AdditionalProductsPurchase(Base):
    __tablename__ = 'additional_products_purchase'
    
    id: Mapped[int] = mapped_column('AdditionalProductsPurchaseID', Integer, primary_key=True, autoincrement=True)
    check_id: Mapped[int] = mapped_column('CheckID', Integer)
    additional_product_id: Mapped[int] = mapped_column('AdditionalProductsID', Integer, ForeignKey('additional_products.AdditionalProductsID'))
    price: Mapped[Numeric] = mapped_column('AdditionalProductsPrice', Numeric(10, 2))

class Bouquets(Base):
    __tablename__ = 'bouquets'
    
    id: Mapped[int] = mapped_column('BouquetsID', Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column('BouquetName', String(255))
    lifespan: Mapped[int] = mapped_column('BouquetLifeSpan', Integer)
    info: Mapped[str] = mapped_column('BouquetInfo', String(255))
    stock: Mapped[int] = mapped_column('BouquetStock', Integer)

class BouquetsPurchase(Base):
    __tablename__ = 'bouquets_purchase'
    
    id: Mapped[int] = mapped_column('BouquetsPurchaseID', Integer, primary_key=True, autoincrement=True)
    check_id: Mapped[int] = mapped_column('CheckID', Integer)
    bouquet_id: Mapped[int] = mapped_column('BouquetID', Integer, ForeignKey('bouquets.BouquetsID'))
    quantity: Mapped[int] = mapped_column('BouquetQuantity', Integer)
    price: Mapped[Numeric] = mapped_column('BouquetPrice', Numeric(10, 2))

class Employees(Base):
    __tablename__ = 'employees'
    
    id: Mapped[int] = mapped_column('EmployeesID', Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column('EmployeeName', String(255))
    position: Mapped[str] = mapped_column('EmployeePosition', String(255))
    salaries: Mapped[Numeric] = mapped_column('EmployeeSalaries', Numeric(10, 2))
    stash: Mapped[Date] = mapped_column('EmployeeStash', Date)

class Customers(Base):
    __tablename__ = 'customers'
    
    id: Mapped[int] = mapped_column('CustomersID', Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column('CustomerName', String(255))
    address: Mapped[str] = mapped_column('CustomerAdres', String(255))
    summ: Mapped[Numeric] = mapped_column('CustomerSumm', Numeric(15, 2))
    phone: Mapped[str] = mapped_column('CustomerPhone', String(255))

class TotalChecks(Base):
    __tablename__ = 'total_checks'
    
    id: Mapped[int] = mapped_column('TotalChecksID', Integer, primary_key=True, autoincrement=True)
    cash_register_id: Mapped[int] = mapped_column('CashRegisterID', Integer)
    flowers_purchase_id: Mapped[int] = mapped_column('FlowersPurchaseID', Integer, ForeignKey('flowers_purchase.FlowersPurchaseID'))
    additional_products_purchase_id: Mapped[int] = mapped_column('AdditionalProductsPurchaseID', Integer, ForeignKey('additional_products_purchase.AdditionalProductsPurchaseID'))
    bouquets_purchase_id: Mapped[int] = mapped_column('BouquetsPurchaseID', Integer, ForeignKey('bouquets_purchase.BouquetsPurchaseID'))
    purchase_date: Mapped[Date] = mapped_column('PurchaseDate', Date)
    total_cost: Mapped[Numeric] = mapped_column('TotalCost', Numeric(10, 2))
    employee_id: Mapped[int] = mapped_column('EmployeesID', Integer, ForeignKey('employees.EmployeesID'))
    customer_id: Mapped[int] = mapped_column('CustomersID', Integer, ForeignKey('customers.CustomersID'))

class DeliveryChecks(Base):
    __tablename__ = 'delivery_checks'
    
    total_checks_id: Mapped[int] = mapped_column('TotalChecksID', Integer, ForeignKey('total_checks.TotalChecksID'))
    delivery_id: Mapped[int] = mapped_column('DeliveryID', Integer, primary_key=True, autoincrement=True)
    courier_id: Mapped[int] = mapped_column('CourierID', Integer, ForeignKey('employees.EmployeesID'))
    customer_id: Mapped[int] = mapped_column('CustomersID', Integer, ForeignKey('customers.CustomersID'))