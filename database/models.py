# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DECIMAL, Date, Double, ForeignKey, ForeignKeyConstraint, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  September 30, 2024 06:12:02
# Database: sqlite:////opt/projects/029b654b-f1fa-4c4c-9822-b292bfbd2ae2/nw_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    __tablename__ = 'CategoryTableNameTest'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    CategoryName_ColumnName = Column('CategoryName_ColumnName', String(8000), quote = True)
    Description = Column('Description', String(8000), quote = True)
    Client_id = Column('Client_id', Integer, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)



class Customer(SAFRSBaseX, Base):
    __tablename__ = 'Customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', String(8000), primary_key=True, quote = True)
    CompanyName = Column('CompanyName', String(8000), quote = True)
    ContactName = Column('ContactName', String(8000), quote = True)
    ContactTitle = Column('ContactTitle', String(8000), quote = True)
    Address = Column('Address', String(8000), quote = True)
    City = Column('City', String(8000), quote = True)
    Region = Column('Region', String(8000), quote = True)
    PostalCode = Column('PostalCode', String(8000), quote = True)
    Country = Column('Country', String(8000), quote = True)
    Phone = Column('Phone', String(8000), quote = True)
    Fax = Column('Fax', String(8000), quote = True)
    Balance = Column('Balance', DECIMAL, quote = True)
    CreditLimit = Column('CreditLimit', DECIMAL, quote = True)
    OrderCount = Column('OrderCount', Integer, server_default=text("0"), quote = True)
    UnpaidOrderCount = Column('UnpaidOrderCount', Integer, server_default=text("0"), quote = True)
    Client_id = Column('Client_id', Integer, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="Customer")



class CustomerDemographic(SAFRSBaseX, Base):
    __tablename__ = 'CustomerDemographic'
    _s_collection_name = 'CustomerDemographic'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', String(8000), primary_key=True, quote = True)
    CustomerDesc = Column('CustomerDesc', String(8000), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)



class Department(SAFRSBaseX, Base):
    __tablename__ = 'Department'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    DepartmentId = Column('DepartmentId', ForeignKey('Department.Id'), quote = True)
    DepartmentName = Column('DepartmentName', String(100), quote = True)
    SecurityLevel = Column('SecurityLevel', Integer, server_default=text("0"), quote = True)

    # parent relationships (access parent)
    Department : Mapped["Department"] = relationship(remote_side=[Id], back_populates=("DepartmentList"))

    # child relationships (access children)
    DepartmentList : Mapped[List["Department"]] = relationship(back_populates="Department")
    EmployeeList : Mapped[List["Employee"]] = relationship(foreign_keys='[Employee.OnLoanDepartmentId]', back_populates="OnLoanDepartment")
    WorksForEmployeeList : Mapped[List["Employee"]] = relationship(foreign_keys='[Employee.WorksForDepartmentId]', back_populates="WorksForDepartment")



class Location(SAFRSBaseX, Base):
    __tablename__ = 'Location'
    _s_collection_name = 'Location'  # type: ignore
    __bind_key__ = 'None'

    country = Column('country', String(50), primary_key=True, quote = True)
    city = Column('city', String(50), primary_key=True, quote = True)
    notes = Column('notes', String(256), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="Location")



class Product(SAFRSBaseX, Base):
    __tablename__ = 'Product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    ProductName = Column('ProductName', String(8000), quote = True)
    SupplierId = Column('SupplierId', Integer, nullable=False, quote = True)
    CategoryId = Column('CategoryId', Integer, nullable=False, quote = True)
    QuantityPerUnit = Column('QuantityPerUnit', String(8000), quote = True)
    UnitPrice = Column('UnitPrice', DECIMAL, nullable=False, quote = True)
    UnitsInStock = Column('UnitsInStock', Integer, nullable=False, quote = True)
    UnitsOnOrder = Column('UnitsOnOrder', Integer, nullable=False, quote = True)
    ReorderLevel = Column('ReorderLevel', Integer, nullable=False, quote = True)
    Discontinued = Column('Discontinued', Integer, nullable=False, quote = True)
    UnitsShipped = Column('UnitsShipped', Integer, quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="Product")



t_ProductDetails_View = Table(
    'ProductDetails_View', metadata,
    Column('Id', Integer, quote = True),
    Column('ProductName', String(8000), quote = True),
    Column('SupplierId', Integer, quote = True),
    Column('CategoryId', Integer, quote = True),
    Column('QuantityPerUnit', String(8000), quote = True),
    Column('UnitPrice', DECIMAL, quote = True),
    Column('UnitsInStock', Integer, quote = True),
    Column('UnitsOnOrder', Integer, quote = True),
    Column('ReorderLevel', Integer, quote = True),
    Column('Discontinued', Integer, quote = True),
    Column('UnitsShipped', Integer, quote = True),
    Column('CategoryName_ColumnName', String(8000), quote = True),
    Column('CategoryDescription', String(8000), quote = True),
    Column('SupplierName', String(8000), quote = True),
    Column('SupplierRegion', String(8000), quote = True)
)


class Region(SAFRSBaseX, Base):
    __tablename__ = 'Region'
    _s_collection_name = 'Region'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    RegionDescription = Column('RegionDescription', String(8000), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)



class SampleDBVersion(SAFRSBaseX, Base):
    __tablename__ = 'SampleDBVersion'
    _s_collection_name = 'SampleDBVersion'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    Notes = Column('Notes', String(800), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)



class Shipper(SAFRSBaseX, Base):
    __tablename__ = 'Shipper'
    _s_collection_name = 'Shipper'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    CompanyName = Column('CompanyName', String(8000), quote = True)
    Phone = Column('Phone', String(8000), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)



class Supplier(SAFRSBaseX, Base):
    __tablename__ = 'Supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    CompanyName = Column('CompanyName', String(8000), quote = True)
    ContactName = Column('ContactName', String(8000), quote = True)
    ContactTitle = Column('ContactTitle', String(8000), quote = True)
    Address = Column('Address', String(8000), quote = True)
    City = Column('City', String(8000), quote = True)
    Region = Column('Region', String(8000), quote = True)
    PostalCode = Column('PostalCode', String(8000), quote = True)
    Country = Column('Country', String(8000), quote = True)
    Phone = Column('Phone', String(8000), quote = True)
    Fax = Column('Fax', String(8000), quote = True)
    HomePage = Column('HomePage', String(8000), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)



class Territory(SAFRSBaseX, Base):
    __tablename__ = 'Territory'
    _s_collection_name = 'Territory'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', String(8000), primary_key=True, quote = True)
    TerritoryDescription = Column('TerritoryDescription', String(8000), quote = True)
    RegionId = Column('RegionId', Integer, nullable=False, quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeTerritoryList : Mapped[List["EmployeeTerritory"]] = relationship(back_populates="Territory")



class Union(SAFRSBaseX, Base):
    __tablename__ = 'Union'
    _s_collection_name = 'Union'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    Name = Column('Name', String(80), quote = True)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="Union")



class Employee(SAFRSBaseX, Base):
    __tablename__ = 'Employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    LastName = Column('LastName', String(8000), quote = True)
    FirstName = Column('FirstName', String(8000), quote = True)
    Title = Column('Title', String(8000), quote = True)
    TitleOfCourtesy = Column('TitleOfCourtesy', String(8000), quote = True)
    BirthDate = Column('BirthDate', String(8000), quote = True)
    HireDate = Column('HireDate', String(8000), quote = True)
    Address = Column('Address', String(8000), quote = True)
    City = Column('City', String(8000), quote = True)
    Region = Column('Region', String(8000), quote = True)
    PostalCode = Column('PostalCode', String(8000), quote = True)
    Country = Column('Country', String(8000), quote = True)
    HomePhone = Column('HomePhone', String(8000), quote = True)
    Extension = Column('Extension', String(8000), quote = True)
    Notes = Column('Notes', String(8000), quote = True)
    ReportsTo = Column('ReportsTo', Integer, index=True, quote = True)
    PhotoPath = Column('PhotoPath', String(8000), quote = True)
    EmployeeType = Column('EmployeeType', String(16), server_default=text("Salaried"), quote = True)
    Salary = Column('Salary', DECIMAL, quote = True)
    WorksForDepartmentId = Column('WorksForDepartmentId', ForeignKey('Department.Id'), quote = True)
    OnLoanDepartmentId = Column('OnLoanDepartmentId', ForeignKey('Department.Id'), quote = True)
    UnionId = Column('UnionId', ForeignKey('Union.Id'), quote = True)
    Dues = Column('Dues', DECIMAL, quote = True)

    # parent relationships (access parent)
    OnLoanDepartment : Mapped["Department"] = relationship(foreign_keys='[Employee.OnLoanDepartmentId]', back_populates=("EmployeeList"))
    Union : Mapped["Union"] = relationship(back_populates=("EmployeeList"))
    WorksForDepartment : Mapped["Department"] = relationship(foreign_keys='[Employee.WorksForDepartmentId]', back_populates=("WorksForEmployeeList"))

    # child relationships (access children)
    EmployeeAuditList : Mapped[List["EmployeeAudit"]] = relationship(back_populates="Employee")
    EmployeeTerritoryList : Mapped[List["EmployeeTerritory"]] = relationship(back_populates="Employee")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="Employee")



class EmployeeAudit(SAFRSBaseX, Base):
    __tablename__ = 'EmployeeAudit'
    _s_collection_name = 'EmployeeAudit'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    Title = Column('Title', String, quote = True)
    Salary = Column('Salary', DECIMAL, quote = True)
    LastName = Column('LastName', String, quote = True)
    FirstName = Column('FirstName', String, quote = True)
    EmployeeId = Column('EmployeeId', ForeignKey('Employee.Id'), quote = True)
    CreatedOn = Column('CreatedOn', Text, quote = True)
    UpdatedOn = Column('UpdatedOn', Text, quote = True)
    CreatedBy = Column('CreatedBy', Text, quote = True)
    UpdatedBy = Column('UpdatedBy', Text, quote = True)

    # parent relationships (access parent)
    Employee : Mapped["Employee"] = relationship(back_populates=("EmployeeAuditList"))

    # child relationships (access children)



class EmployeeTerritory(SAFRSBaseX, Base):
    __tablename__ = 'EmployeeTerritory'
    _s_collection_name = 'EmployeeTerritory'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', String(8000), primary_key=True, quote = True)
    EmployeeId = Column('EmployeeId', ForeignKey('Employee.Id'), nullable=False, quote = True)
    TerritoryId = Column('TerritoryId', ForeignKey('Territory.Id'), quote = True)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Employee : Mapped["Employee"] = relationship(back_populates=("EmployeeTerritoryList"))
    Territory : Mapped["Territory"] = relationship(back_populates=("EmployeeTerritoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    __tablename__ = 'Order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'
    __table_args__ = (
        ForeignKeyConstraint(['Country', 'City'], ['Location.country', 'Location.city']),
    )

    Id = Column('Id', Integer, primary_key=True, quote = True)
    CustomerId = Column('CustomerId', ForeignKey('Customer.Id'), nullable=False, index=True, quote = True)
    EmployeeId = Column('EmployeeId', ForeignKey('Employee.Id'), nullable=False, index=True, quote = True)
    OrderDate = Column('OrderDate', String(8000), quote = True)
    RequiredDate = Column('RequiredDate', Date, quote = True)
    ShippedDate = Column('ShippedDate', String(8000), quote = True)
    ShipVia = Column('ShipVia', Integer, quote = True)
    Freight = Column('Freight', DECIMAL, server_default=text("0"), quote = True)
    ShipName = Column('ShipName', String(8000), quote = True)
    ShipAddress = Column('ShipAddress', String(8000), quote = True)
    ShipCity = Column('ShipCity', String(8000), quote = True)
    ShipRegion = Column('ShipRegion', String(8000), quote = True)
    ShipPostalCode = Column('ShipPostalCode', String(8000), quote = True)
    ShipCountry = Column('ShipCountry', String(8000), quote = True)
    AmountTotal = Column('AmountTotal', DECIMAL(10, 2), quote = True)
    Country = Column('Country', String(50), quote = True)
    City = Column('City', String(50), quote = True)
    Ready = Column('Ready', Boolean, server_default=text("TRUE"), quote = True)
    OrderDetailCount = Column('OrderDetailCount', Integer, server_default=text("0"), quote = True)
    CloneFromOrder = Column('CloneFromOrder', ForeignKey('Order.Id'), quote = True)

    # parent relationships (access parent)
    Order : Mapped["Order"] = relationship(remote_side=[Id], back_populates=("OrderList"))
    Location : Mapped["Location"] = relationship(back_populates=("OrderList"))
    Customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    Employee : Mapped["Employee"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="Order")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="Order")



class OrderDetail(SAFRSBaseX, Base):
    __tablename__ = 'OrderDetail'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    Id = Column('Id', Integer, primary_key=True, quote = True)
    OrderId = Column('OrderId', ForeignKey('Order.Id'), nullable=False, index=True, quote = True)
    ProductId = Column('ProductId', ForeignKey('Product.Id'), nullable=False, index=True, quote = True)
    UnitPrice = Column('UnitPrice', DECIMAL, quote = True)
    Quantity = Column('Quantity', Integer, server_default=text("1"), nullable=False, quote = True)
    Discount = Column('Discount', Double, server_default=text("0"), quote = True)
    Amount = Column('Amount', DECIMAL, quote = True)
    ShippedDate = Column('ShippedDate', String(8000), quote = True)

    # parent relationships (access parent)
    Order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    Product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)
