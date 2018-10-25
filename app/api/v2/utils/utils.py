from flask import abort, request,json
class Validate:
    def validate_empty_product_inputs(self,data):
        if (data['product_name'] == "") :
            abort(400, description="Product name required")
        if data['stock_amount'] == "":
            abort(400, description="Stock amount should not be empty")
        if data['low_inventory_stock'] == "":
            abort(400, description="low inventory stock field should not be empty")
        if data['price'] == "":
            abort(400, description="Price should not be empty")