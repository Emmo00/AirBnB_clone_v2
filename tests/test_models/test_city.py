#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.city import City
from models import storage


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        new_city = City()
        self.assertTrue(hasattr(new_city, "name"))
        self.assertTrue(hasattr(new_city, "state_id"))
        if storage == 'db':
            self.assertEqual(new_city.name, None)
            self.assertEqual(new_city.state_id, None)
        else:
            self.assertEqual(new_city.name, "")
            self.assertEqual(new_city.state_id, "")
        new_dict = new_city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(new_dict["__class__"], "City")
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in new_city.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)
