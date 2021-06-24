from models.Product import Product

class ProductController():

  def __init__(self):
    self.product_model = Product()

  def list(self, search=None, category_id=None):
    products = []

    if search is not None:
      products = self.product_model.get_by_title(search)
    elif category_id is not None:
      products = self.product_model.get_by_category(category_id)
    else:
      products = self.product_model.get_all()
    
    return products

  def find_one(self, product_id):
    return self.product_model.get_by_id(product_id)