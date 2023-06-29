def calculate_total_price(item1_quantity: object, item2_quantity: object, item3_quantity: object) -> object:
    item1_price = 500.0
    item2_price = 1000.00
    item3_price = 5000.00

    individual_price = (item1_price * item1_quantity) + (item2_price * item2_quantity) + (item3_price * item3_quantity)

    combo_discount = 0.1  # 10% discount for purchasing a combo pack
    gift_discount = 0.25  # 25% discount for purchasing a gift pack

    combo_price = (item1_price + item2_price) * (1 - combo_discount) * min(item1_quantity, item2_quantity)
    gift_price = (item1_price + item2_price + item3_price) * (1 - gift_discount) * min(item1_quantity, item2_quantity,
                                                                                       item3_quantity)

    total_price = individual_price + combo_price + gift_price

    print("-------------------")
    print("-------------------")
    print("Online Store")
    print("-------------------")
    print("-------------------")
    print("Product(s)                                            Price")
    print("-------------------")
    print(f"Item 1                                               {item1_price}")
    print(f"Item 2                                               {item2_price}")
    print(f"Item 3                                               {item3_price}")
    print(f"combo 1(item 1 + 2)                                  {item1_price + item2_price}")
    print(f"combo 2(item 2 + 3)                                  {item2_price + item3_price}")
    print(f"combo 3(item 1 + 3)                                  {item1_price + item3_price}")
    print(f"combo 4(item 1 + 2 + 3)                              {item1_price + item2_price + item3_price}")
    print("Total Price: ", total_price)

calculate_total_price(3, 2, 1)