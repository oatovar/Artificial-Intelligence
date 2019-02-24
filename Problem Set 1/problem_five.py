#!/usr/bin/env python3
import random

points = []

def prettyPrint(vector):
    for coordinate in range(len(vector)):
        vector[coordinate] = round(vector[coordinate], 3)

def RHC(sp, p, r, seed):
    # Initialize seed
    random.seed(seed)
    # Add in Starting Point
    points.append(sp)
    # Save neighbor number that's best solution
    max_solution_index = 0
    # Pass in x,y,z coordinates from SP
    max_solution_value = func(sp[0], sp[1], sp[2])
    # Save the amount of solutions generated.
    solutions_count = 0
    while True:
        # Generate neighbors
        for x in range(0, p):
            # Add to the solutions counter
            solutions_count += 1
            vector_v = []
            # Use uniform distribution to generate random vectors
            for i in range(1, 4):
                vector_v.append(round(random.uniform(-float(r), float(r)), 2))
            # Add randomly generated vector to original starting point
            # This simulates annealing
            for i in range(0, 3):
                vector_v[i] += sp[i]
                points.append(vector_v)
        for index, point in enumerate(points):
            if (func(point[0], point[1], point[2]) > max_solution_value):
                max_solution_index = index
                # max_solution_value = func(point[0], point[1], point[2])
        if max_solution_value >= func(points[max_solution_index][0], points[max_solution_index][1], points[max_solution_index][2]):
            return [solutions_count, points[max_solution_index], max_solution_value]
        else:
            max_vector = points[max_solution_index]
            max_solution_value = func(max_vector[0], max_vector[1], max_vector[2])
            points.clear()
            points.append(max_vector)


def func(x, y, z):
    return abs(x-y-0.2)*abs(x*z-0.8)*abs(0.3-z*z*y)+(x*y*(1-z)*abs(z-0.5))

if __name__ == "__main__":
    print("Running Randomized Hill Climbing")
    # Seeds used for RNG. Python allows for strings to be used.
    seed_one = "ASDFJASLKFJAA134328FSDV"
    seed_two = "ASDFcadf90ASDFJ0VDAdkld"
    seed_three = "a8034jmCART$CC9392l;anv9_391"
    # Starting points
    sp_one = [0.5, 0.5, 0.5]
    sp_two = [0.0, 0.5, 1.0]
    sp_three = [0.9, 0.6, 0.3]

    # Solutions
    solution = RHC(sp_one,20,0.02,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,20,0.05,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,100,0.02,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #1")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,100,0.05,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #1")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,20,0.02,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #2")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,20,0.05,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #2")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,100,0.02,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #2")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,100,0.05,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #2")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,20,0.02,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #3")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,20,0.05,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #3")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,100,0.02,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #3")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_one,100,0.05,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_one))
    print("Run #3")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,20,0.02,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,20,0.05,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,100,0.02,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #1")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,100,0.05,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #1")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,20,0.02,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #2")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,20,0.05,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #2")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,100,0.02,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #2")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,100,0.05,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #2")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,20,0.02,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #3")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,20,0.05,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #3")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,100,0.02,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #3")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_two,100,0.05,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_two))
    print("Run #3")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,20,0.02,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,20,0.05,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,100,0.02,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #1")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,100,0.05,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #1")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,20,0.02,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #2")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,20,0.05,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #2")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,100,0.02,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #2")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,100,0.05,seed_two)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #2")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,20,0.02,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #3")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,20,0.05,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #3")
    print("P: " + str(20) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,100,0.02,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #3")
    print("P: " + str(100) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]
    print("\n")

    solution = RHC(sp_three,100,0.05,seed_three)
    solution[2] = round(solution[2], 6)
    print("SP: " + str(sp_three))
    print("Run #3")
    print("P: " + str(100) + " R: " + str(0.05))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]

    print("\n")
    print("37th Run")
    solution = RHC([0.00, 0.5, 1.0],30,0.07,seed_one)
    solution[2] = round(solution[2], 6)
    print("SP: " + str([0.00, 0.5, 1.0]))
    print("Run #1")
    print("P: " + str(20) + " R: " + str(0.02))
    print("# of Solutions Generated " + str(solution[0]))
    print("Solution " + str(solution[1]))
    print("Solution Value for f(x,y,z) " + str(solution[2]))
    del points[:]