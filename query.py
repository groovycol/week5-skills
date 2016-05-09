"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(brand_name="Chevrolet", name="Corvette").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued.is_(None))).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    results = Model.query.filter(Model.year == year).all()

    for item in results:
        if item.car == None:
            print "Model: {}\tBrand: {}".format(item.name, item.brand_name)
        else:
            print "Model: {}\tBrand: {}\tHeadquarters: {}".format(
                                                    item.name,
                                                    item.brand_name,
                                                    item.car.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     # results = Model.query.order_by('brand_name').all()

     # for item in results:
     #    print "Brand: {} Models: {}"

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# It's a class object. The value is a sql query.
# >>> Brand.query.filter_by(name='Ford')
# <flask_sqlalchemy.BaseQuery object at 0x6fffef11810>
# >>> stuff = Brand.query.filter_by(name='Ford')
# >>> type(stuff)
# <class 'flask_sqlalchemy.BaseQuery'>
# >>> print stuff
# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
# FROM brands
# WHERE brands.name = :name_1

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table contains references (usually foreign keys) to other tables.
# It helps map the relationships between columns from multiple tables. It is used
# to manage many-to-many relationships
# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    """Find any names in the brands table that contain or match the string passed in """

    search_string = "%" + mystr + "%"
    return Brand.query.filter(Brand.name.like(search_string)).all()


def get_models_between(start_year, end_year):
    """Return a list of objects that fall between year1 (inclusive)
    and year 2(exclusive)"""

    return Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()
