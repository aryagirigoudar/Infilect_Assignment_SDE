
class Max_Rect:
    def __init__(self):
        pass

    def check_dims(self, matrix):
        '''
        Checks dimensions of the given matrix and appends zeros to rows with fewer elements
        to make all rows of equal length.

        Parameters:
        matrix (list): The input matrix.

        Returns:
        None
        '''
        max_dim = 0
        for row in matrix:
            max_dim = max(max_dim, len(row))

        for row in matrix:
            if len(row) != max_dim:
                row.append(0)

    def unique(self, matrix):
        '''
        Returns a list of unique elements present in the matrix.

        Parameters:
        matrix (list): The input matrix.

        Returns:
        list: A list of unique elements present in the matrix.
        '''
        uni_set = set()

        for row in matrix:
            for data in row:
                uni_set.add(data)

        return list(uni_set)

    def max_rect(self, matrix, vertex):
        '''
        Finds the maximal rectangle area containing the given vertex value in the matrix.

        Parameters:
        matrix (list): The input matrix.
        vertex: The vertex to search for in the matrix.

        Returns:
        int: The area of the maximal rectangle containing the given vertex value.
        '''
        self.check_dims(matrix)
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        
        # heights will store the height of each column
        heights = [0] * (cols + 1)  # Include an extra element for easier calculation
        
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == vertex else 0
            
            # Calculate max area using histogram method
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    min_height = min(heights[stack[-1]], heights[i]) if stack else heights[i]
                    if w * min_height == max_area:  # Skip rectangles with width equal to the min height
                        continue
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area              
        
    
    def get_result(self):
        '''
        Returns the result of the execution.

        Returns:
        tuple: A tuple containing the maximal rectangle area and the vertex value.
        '''
        return self.result
    
    def execute(self, matrix):
        '''
        Executes the algorithm on the given matrix and stores the result.

        Parameters:
        matrix (list): The input matrix.

        Returns:
        None
        '''
        res = [0, 0]

        vertices = list(self.unique(matrix))

        for vertex in vertices:
            area = self.max_rect(matrix, vertex)
            if res[0] < area:
                res[0] = area
                res[1] = vertex
        
        self.result = tuple(res)
