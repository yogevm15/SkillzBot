def closest_to(to, from_arr, min_dist = -1):
    closest = None
    closest_dist = None
    for entity in from_arr:
        if ((min_dist != -1 and entity.distance(to) <= min_dist) or min_dist == -1) and (closest_dist is None) or (entity.distance(to) < closest_dist):
            closest = entity
            closest_dist = entity.distance(to)
    return closest
