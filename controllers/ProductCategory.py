from models.ProductCategory import ProductCategory

class ProductCategoryController():

  def __init__(self):
    self.product_category_model = ProductCategory()

  def list(self, title=None, product_id=None):
    return self.product_category_model.get_all()
