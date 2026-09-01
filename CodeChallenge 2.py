money = 4872

libo = money // 1000
libo_sukli = money % 1000

five_h = libo_sukli // 500
five_sukli = libo_sukli % 500

two_h = five_sukli // 200
two_sukli = five_sukli % 200

one_h = two_sukli // 100
one_sukli = two_sukli % 100

fifty_h = one_sukli // 50
fifty_sukli = one_sukli % 50

twenty_h = fifty_sukli // 20
twenty_sukli = fifty_sukli % 20

ten_h = twenty_sukli // 10
ten_sukli = twenty_sukli % 10

five = ten_sukli // 5
five_sukli = ten_sukli % 5

one = five_sukli // 1

print("1000 - ", libo)
print("500 - ", five_h)
print("200 - ", two_h)
print("100 - ", one_h)
print("50 - ", fifty_h)
print("20 - ", twenty_h)
print("10 - ", ten_h)
print("5 - ", five)
print("1 - ", one)