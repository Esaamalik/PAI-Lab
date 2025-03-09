class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited = set()  # To keep track of visited states

    def dfs(self, jug1, jug2, path):
        # If we have reached the target
        if jug1 == self.target or jug2 == self.target:
            print("Solution found:", path)
            return True

        # If this state has already been visited, return
        if (jug1, jug2) in self.visited:
            return False

        # Mark this state as visited
        self.visited.add((jug1, jug2))

        # Print the current state
        print(f"Current state: Jug1 = {jug1}, Jug2 = {jug2}")

        # Perform all possible operations
        # 1. Fill Jug 1
        if self.dfs(self.jug1_capacity, jug2, path + [(self.jug1_capacity, jug2)]):
            return True

        # 2. Fill Jug 2
        if self.dfs(jug1, self.jug2_capacity, path + [(jug1, self.jug2_capacity)]):
            return True

        # 3. Empty Jug 1
        if self.dfs(0, jug2, path + [(0, jug2)]):
            return True

        # 4. Empty Jug 2
        if self.dfs(jug1, 0, path + [(jug1, 0)]):
            return True

        # 5. Pour Jug 1 into Jug 2
        pour_to_jug2 = min(jug1, self.jug2_capacity - jug2)
        if self.dfs(jug1 - pour_to_jug2, jug2 + pour_to_jug2, path + [(jug1 - pour_to_jug2, jug2 + pour_to_jug2)]):
            return True

        # 6. Pour Jug 2 into Jug 1
        pour_to_jug1 = min(jug2, self.jug1_capacity - jug1)
        if self.dfs(jug1 + pour_to_jug1, jug2 - pour_to_jug1, path + [(jug1 + pour_to_jug1, jug2 - pour_to_jug1)]):
            return True

        return False

    def solve(self):
        # Start DFS from both jugs being empty
        if not self.dfs(0, 0, [(0, 0)]):
            print("No solution found.")

# Example usage
if __name__ == "__main__":
    jug1_capacity = 4  # Capacity of Jug 1
    jug2_capacity = 3  # Capacity of Jug 2
    target = 2         # Target amount of water

    water_jug = WaterJug(jug1_capacity, jug2_capacity, target)
    water_jug.solve()