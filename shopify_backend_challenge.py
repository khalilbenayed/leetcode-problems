import requests
import json


def get_total_before_discount(products):
    total = 0
    for product in products:
        total += product.get("price")
    return total

def get_total_after_product_discount(products, discount):
    total = 0
    discount_value = discount.get("discount_value")
    for product in products:
        price = product.get("price")
        if ("collection" in discount and discount.get("collection") == product.get("collection") or
                ("product_value" in discount and product.get("price") >= discount.get("product_value"))):
            price = 0 if price < discount_value else price - discount_value

        total += price

    return total



def get_cart_api_response(cart_id, page):
    cart_api_url = "http://backend-challenge-fall-2018.herokuapp.com/carts.json?id=" + str(cart_id) + "&page=" + str(page)
    response = requests.get(cart_api_url)
    return response.json()

def get_total_amounts():
    data = raw_input()
    discount = json.loads(data)

    page = 1
    page_data = get_cart_api_response(discount.get("id"), page)

    products = page_data.get("products")
    pagination = page_data.get("pagination")
    
    number_of_pages = pagination.get("total")/pagination.get("per_page")
    if pagination.get("total") % pagination.get("per_page") != 0:
        number_of_pages += 1

    total_amount = get_total_before_discount(products)
    total_after_discount = get_total_after_product_discount(products, discount) if discount.get("discount_type") == "product" else 0


    for i in range(1, number_of_pages): # we start at 1 because we already processed the first page
        page += 1
        page_data = get_cart_api_response(discount.get("id"), page)
        products = page_data.get("products")

        total_amount += get_total_before_discount(products)
        if discount.get("discount_type") == "product":
            total_after_discount += get_total_after_product_discount(products, discount)

    if discount.get("discount_type") == "cart":
        discount_value = discount.get("discount_value")
        cart_value = discount.get("cart_value")
        total_after_discount = total_amount - discount_value if total_amount >= cart_value else total_amount
        if total_after_discount < 0:
            total_after_discount = 0

    data = {
        "total_amount": total_amount,
        "total_after_discount": total_after_discount
    }

    return data

print(json.dumps(get_total_amounts(), indent=2))