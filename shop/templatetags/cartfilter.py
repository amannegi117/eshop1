from django import template
register  = template.Library()

@register.filter(name="in_cart")
def in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            return True
                
    return False
    
@register.filter(name="quant")
def quant(product,cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            return cart.get(id)
                
    return 0
@register.filter(name="multiply")
def multiply(product,cart):
    return product.price * quant(product,cart)

@register.filter(name="total")
def total(product,cart):
    s = 0
    
    for i in product:
        s+= multiply(i,cart)
    return s