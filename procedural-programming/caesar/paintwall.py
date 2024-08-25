print(f"1 can of paint can cover 5 square meters of wall, given a random height and width of wall, calculate hom many can of paint can can be used to paint the wall")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5


def paint_calc(height,width,cover):
  number_of_cans = (height * width) / cover
  number_of_cans = round(number_of_cans)
  print(f"You'll need {number_of_cans} cans of paint.")



paint_calc(height=test_h,width=test_w,cover=coverage)
