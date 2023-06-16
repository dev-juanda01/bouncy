class Bouncy:
    def __init__(self, porcentage):
        print(self.percentage_bouncies_inverse(99))


    def digits_number(self, num):
      return [int(x) for x in str(num)]


    def is_bouncy(self, num):
      if num <= 100:
        return False

      numbers = self.digits_number(num)
      temp = numbers[0]
      is_increasing = False
      is_decreasing = False
      
      for num in numbers:
        if num > temp:
          is_increasing = True
        elif num < temp:
          is_decreasing = True
        temp = num
        if is_increasing and is_decreasing:
          return True
      return False


    def percentage_bouncies(self, num, bouncy):
      return (bouncy / num)*100


    def percentage_bouncies_inverse(self, percentage):
      len_num = 100
      len_bouncy = 0
      
      while self.percentage_bouncies(len_num, len_bouncy) < percentage:
        if self.is_bouncy(len_num):
          len_bouncy = len_bouncy + 1
        len_num = len_num + 1
      return len_num

test = Bouncy(99)