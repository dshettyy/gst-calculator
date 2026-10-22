
def calculate_total(subtotal):

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    
    if subtotal > 300:
        subtotal = subtotal * 0.90

    
    total = subtotal * 1.05

    return round(total, 2)



print(calculate_total(200))  
print(calculate_total(400))  
