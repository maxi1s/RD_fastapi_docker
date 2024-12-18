from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Numeric, Date
from project.infrastructure.postgres.database import Base
import datetime

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


class DeliveryChecks(Base):
    __tablename__ = "delivery_checks"

    total_checks_id: Mapped[int] = mapped_column(ForeignKey("total_checks.total_checks_id"), nullable=False)
    delivery_id: Mapped[int] = mapped_column(primary_key=True)
    courier_id: Mapped[int] = mapped_column(ForeignKey("employees.employees_id"), nullable=False)
    customers_id: Mapped[int] = mapped_column(ForeignKey("customers.customers_id"), nullable=False)


class TotalChecks(Base):
    __tablename__ = 'total_checks'

    id: Mapped[int] = mapped_column('TotalChecksID', Integer, primary_key=True, autoincrement=True)
    cash_register_id: Mapped[int] = mapped_column('CashRegisterID', Integer)
    flowers_purchase_id: Mapped[int] = mapped_column('FlowersPurchaseID', Integer,
                                                     ForeignKey('flowers_purchase.FlowersPurchaseID'))
    additional_products_purchase_id: Mapped[int] = mapped_column('AdditionalProductsPurchaseID', Integer, ForeignKey(
        'additional_products_purchase.AdditionalProductsPurchaseID'))
    bouquets_purchase_id: Mapped[int] = mapped_column('BouquetsPurchaseID', Integer,
                                                      ForeignKey('bouquets_purchase.BouquetsPurchaseID'))
    purchase_date: Mapped[Date] = mapped_column('PurchaseDate', Date)
    total_cost: Mapped[Numeric] = mapped_column('TotalCost', Numeric(10, 2))
    employee_id: Mapped[int] = mapped_column('EmployeesID', Integer, ForeignKey('employees.EmployeesID'))
    customer_id: Mapped[int] = mapped_column('CustomersID', Integer, ForeignKey('customers.CustomersID'))



class Provider(Base):
    __tablename__ = 'provider'
    
    id: Mapped[int] = mapped_column('ProviderID', Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column('ProviderType', String(255))
    name: Mapped[str] = mapped_column('ProviderName', String(255))
    email: Mapped[str] = mapped_column('ProviderEmail', String(255))
    address: Mapped[str] = mapped_column('ProviderAdres', String(255))
    number: Mapped[str] = mapped_column('ProviderNumber', String(255))

class ProviderFlowers(Base):
    __tablename__ = "provider_flowers"

    provider_flowers_id: Mapped[int] = mapped_column("ProviderFlowersID", Integer, primary_key=True, autoincrement=True)
    providers_flower_stack: Mapped[int] = mapped_column("ProvidersFlowerStack", Integer, nullable=False)
    providers_flower_date: Mapped[datetime.date] = mapped_column("ProvidersFlowerDate", Date, nullable=False)
    providers_flower_flower_id: Mapped[int] = mapped_column("ProvidersFlowerFlowerID", Integer, nullable=False)
    provider_id: Mapped[int] = mapped_column("ProviderID", Integer, ForeignKey("provider.provider_id"), nullable=False)

class ProviderAdd(Base):
    __tablename__ = "provider_add"

    provider_add_id: Mapped[int] = mapped_column(primary_key=True)
    provider_add_stack: Mapped[int] = mapped_column(nullable=False)
    provider_add_date: Mapped[Date] = mapped_column(nullable=False)
    additional_product_id: Mapped[int] = mapped_column(nullable=False)
    provider_id: Mapped[int] = mapped_column(ForeignKey("provider.provider_id"), nullable=False)

class Flowers(Base):
    __tablename__ = "flowers"

    flowers_id: Mapped[int] = mapped_column("FlowersID", Integer, primary_key=True, autoincrement=True)
    flowers_name: Mapped[str] = mapped_column("FlowersName", String(255), nullable=False)
    flower_life_span: Mapped[int] = mapped_column("FlowerLifeSpan", Integer, nullable=False)
    flower_stock: Mapped[int] = mapped_column("FlowerStock", Integer, nullable=False)
    provider_flower_id: Mapped[int] = mapped_column("ProviderFlowerID", Integer, ForeignKey("provider_flowers.ProviderFlowersID"), nullable=True)
    flower_price: Mapped[Numeric] = mapped_column("FlowerPrice", Numeric(10, 2), nullable=False)
    
class AdditionalProducts(Base):
    __tablename__ = "additional_products"

    additional_products_id: Mapped[int] = mapped_column("AdditionalProductsID", Integer, primary_key=True, autoincrement=True)
    additional_product_name: Mapped[str] = mapped_column("AdditionalProductName", String(255), nullable=False)
    additional_product_stock: Mapped[int] = mapped_column("AdditionalProductStock", Integer, nullable=False)
    provider_add_id: Mapped[int] = mapped_column("ProviderAddID", Integer, ForeignKey("provider_add.provider_add_id"), nullable=False)


class Employees(Base):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column("EmployeesID", Integer, primary_key=True, autoincrement=True)
    employee_name: Mapped[str] = mapped_column("EmployeeName", String(255), nullable=False)
    employee_position: Mapped[str] = mapped_column("EmployeePosition", String(255), nullable=False)
    employee_salaries: Mapped[Numeric] = mapped_column("EmployeeSalaries", Numeric(10, 2), nullable=False)
    employee_stash: Mapped[Date] = mapped_column("EmployeeStash", Date, nullable=False)

class Customers(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column("CustomersID", Integer, primary_key=True, autoincrement=True)
    customer_name: Mapped[str] = mapped_column("CustomerName", String(255), nullable=False)
    customer_adres: Mapped[str] = mapped_column("CustomerAdres", String(255), nullable=False)
    customer_summ: Mapped[Numeric] = mapped_column("CustomerSumm", Numeric(15, 2), nullable=False)
    customer_phone: Mapped[str] = mapped_column("CustomerPhone", String(255), nullable=False)

class FlowersPurchase(Base):
    __tablename__ = "flowers_purchase"

    flowers_purchase_id: Mapped[int] = mapped_column(primary_key=True)
    check_id: Mapped[int] = mapped_column(ForeignKey("total_checks.total_checks_id"), nullable=False)
    flower_id: Mapped[int] = mapped_column(ForeignKey("flowers.flowers_id"), nullable=False)
    flower_quantity: Mapped[int] = mapped_column(nullable=False)
    flowers_price: Mapped[Numeric] = mapped_column(nullable=False)

class BouquetsPurchase(Base):
    __tablename__ = "bouquets_purchase"

    bouquets_purchase_id: Mapped[int] = mapped_column(primary_key=True)
    check_id: Mapped[int] = mapped_column(ForeignKey("total_checks.total_checks_id"), nullable=False)
    bouquet_id: Mapped[int] = mapped_column(ForeignKey("bouquets.bouquets_id"), nullable=False)
    bouquet_quantity: Mapped[int] = mapped_column(nullable=False)
    bouquets_price: Mapped[Numeric] = mapped_column(nullable=False)

к