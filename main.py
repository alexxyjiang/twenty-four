import itertools

def twentyfour(int_input):
  for nums in itertools.permutations(int_input):
    for ops in itertools.product('+-*/', repeat=3):
      formula1 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)
      formula2 = '({0}{4}({1}{5}{2})){6}{3}'.format(*nums, *ops)
      formula3 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)
      formula4 = '{0}{4}(({1}{5}{2}){6}{3})'.format(*nums, *ops)
      formula5 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)

      for formula in [formula1, formula2, formula3, formula4, formula5]:
        try:
          if abs(eval(formula) - 24.0) < 1e-8:
            print(formula)
        except ZeroDivisionError:
          continue

def main():
  str_input = input('Numbers: ')
  int_input = [int(x) for x in str_input.split(' ')]
  twentyfour(int_input)

if __name__ == '__main__':
  main()
