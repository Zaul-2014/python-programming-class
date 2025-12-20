def notes(a):
  q = [1000, 500, 100, 50, 20, 10]
  x = 0

  for i in range(6):
    r = q[i]
    x = a//r

    print('notes of {} = {}'.format(r, x))
    a = a%r

notes(9800)