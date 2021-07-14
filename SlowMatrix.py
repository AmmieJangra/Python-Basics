class SlowMatrix:

	def __init__(self, matrix):
          self.n = matrix
          self.rows = len(matrix)
          self.columns = len(matrix[0])


	def __matmul__(self, mat2):
           m = [[0 for x in range(mat2.columns)] for x in range(self.rows)]
           for i in range(self.rows):
                for j in range(self.columns):
                   z = 0
                   for k in range(self.columns):
                      z = z + self.n[i][k]*mat2.n[k][j]
                m[i][j] = z
           mat = SlowMatrix(m)
           return mat
# to see output run print(s.__matmul__(mat2).n


	def __mul__(self, mat2):
	     m = [[0 for x in range(self.columns)] for x in range(mat2.rows)]
             for i in range(self.rows):
                 for j in range(self.columns):
                    m[i][j] = self.n[i][j]*mat2.n[i][j]
             mat = SlowMatrix(m)
             return mat
# to see output run print(s.__mul__(mat2).n


	def __add__(self, mat2):
	    m = [[0 for x in range(self.columns)] for x in range(self.rows)]
            for i in range(self.rows):
              for j in range(self.columns):
                 m[i][j] = self.n[i][j] + mat2.n[i][j]
           mat = SlowMatrix(m) 
           return mat            
# to get output, run print(s.__add__(mat2).n)



	def __sub__(self, mat2):
	   m = [[0 for x in range(self.columns)] for x in range(mat2.rows)]
           for i in range(self.rows):
              for j in range(self.columns):
                 m[i][j] = self.n[i][j] - mat2.n[i][j]
           mat = SlowMatrix(m)
           return mat
# to get output run print(s.__sub__(mat2).n)


	def __eq__(self, mat2):
	    for i in range(self.rows):
              for j in range(self.columns):
                if self.n[i][j] != mat2.n[i][j] : 
                  return 0
            return 1 

	
	def transpose(self):
	    m = [[0 for x in range(self.rows)] for x in range(self.columns)]
            for i in range(self.columns):
               for j in range(self.rows):
                  m[i][j] = self.n[j][i]
            mat = SlowMatrix(m)
            return mat    
 # to see the transpose, run print(s.transpose().n)


	def ones(shape):
	    m = shape[0]
            n = shape[1]
            arr = [[1 for x in range(m)] for x in range(n)]
            p = SlowMatrix(arr)
            return p
 # to use this, run print(SlowMatrix.ones((rows,columns)))


	def zeros(shape):
            m = shape[0]
            n = shape[1]
            arr = [[0 for x in range(m)] for x in range(n)]
            p = SlowMatrix(arr)
            return p
 #to use this, run print(SlowMatrix.zeros((rows,columns)))


	def __getitem__(self, key = []):
		return self.n[key[0]][key[1]]

	def __setitem__(self, key, value):
		self.n[key[0]][key[1]] = value
                return

	## Converts SlowMatrix to a Python string
	def __str__(self):
	   b = str()
           for i in range(self.rows):
               for j in range(self.columns):
               b  = b + str(self.n[i][j])
           return b   
