from models.Product import Product

class ProductController():

  def __init__(self):
    self.product_model = Product()

  def list(self, title=None):
    products = []

    if title is not None:
      products = self.product_model.get_by_title(title)
    else:
      products = self.product_model.get_all()
    
    return products

  def find_one(self, product_id):
    return self.product_model.get_by_id(product_id)