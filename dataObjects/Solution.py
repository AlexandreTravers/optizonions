class Solution:
    def __init__(self, entities_count, fields_count):
        self.matrix = self.initMatrix(entities_count, fields_count)

    def initMatrix(self, entities_count, fields_count):
        matrice = []
        for entities_row in range(entities_count):
            for entities_column in range(entities_count):
                matrice.append([])
                for field_row in range(fields_count):
                    matrice[entities_row * entities_count + entities_column].append([])
                    for field_column in range(fields_count):
                        matrice[entities_row * entities_count + entities_column][field_row].append(False)
        return matrice

    def print_solution_matrix(self):
        for i, row in enumerate(self.matrix):
            for j, entity_row in enumerate(row):
                print(f"Entity {i + 1} - Field {j + 1} Matrix:")
                for entity_col in entity_row:
                    print(entity_col)
                print()