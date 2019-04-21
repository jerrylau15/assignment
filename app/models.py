import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.filemanager import ImageManager
from flask import Markup, url_for, g
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                Column('id', Integer, primary_key=True),
                                Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                Column('employee_id', Integer, ForeignKey('employee.id'))
                                )


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name


class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")


class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")


class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date)
    mobile = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    contact_group = relationship("ContactGroup")

    def __repr__(self):
        return self.name


class Movie(Model):
    id = Column(Integer, primary_key=True)
    photo = Column(ImageColumn(size=(500, 500, True), thumbnail_size=(30, 30, True)))
    name = Column(String(150), unique=False, nullable=False)
    Type = Column(String(100), nullable=False)
    rating = Column(String(10))
    opening = Column(Date)
    time = Column(String(20))
    subtitle = Column(String(50))
    synopsis = Column(Text())
    cinema = Column(String(200))
    Director = Column(String(30))
    Cast = Column(String(300))
    event_group_id = Column(Integer, ForeignKey("event_group.id"))
    event_group = relationship("EventGroup")

    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('MovieModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="' + im.get_url(self.photo) + \
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('MovieModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('MovieModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) + \
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('MovieModelView.show', pk=str(self.id)) + \
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def __repr__(self):
        return self.name


class EventGroup(Model):
    id = Column(Integer, primary_key=True)
    Type = Column(String(100), nullable=False)
    name = Column(String(150), unique=False, nullable=False)

    def __repr__(self):
        return self.name
