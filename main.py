def isOrtogonal (a,m,n) :
      if (m != n ):
            return False

      trans = [[0 for x in range(n)]
               for y in range(n)]

      for i in range(0,n):
            for j in range (0,n):
                  trans[i][j] = a[i][j]

      prod = [[0 for x in range (n)]
              for y in range(n)]

      for i in range(0, n):
            for j in range (0,n):

                  sum =0
                  for k in range(0,n):

                        sum = sum + (a[i][k] * a[j][k])

                  prod[i][j] = sum


      for i in range (0,n):
            for j in range (0,n):

                  if (i != j and prod[i][j] != 0 ):
                        return False

                  if (i == j and prod[i][j] != 1 ):
                        return False

      return True

a = [[0.25, 0.1],
     [0.2, 0.5]]

if (isOrtogonal(a,2,2)):
      print("Evet")

else :
      print("Hayır")