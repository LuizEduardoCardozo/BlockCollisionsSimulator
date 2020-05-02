def colision(cube1, cube2):

    cube1 = [float(cube1.mass), float(cube1.vel)]
    cube2 = [float(cube2.mass), float(cube2.vel)]

    final_velocity1  = ((cube1[0] - cube2[0]) / (cube1[0] + cube2[0])) * cube1[1]
    final_velocity1 += ((2*cube2[0])/(cube1[0] + cube2[0])) * cube2[1]

    deltaV = cube1[1] - final_velocity1

    final_velocity2 = (cube1[0] * deltaV) + (cube2[0] * cube2[1])
    final_velocity2 = final_velocity2 / (cube2[0])

    return final_velocity1, final_velocity2
    
