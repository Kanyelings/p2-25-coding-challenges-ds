def is_intersecting(circleAx, circleAy, circleAr, circleBx, circleBy, circleBr):
    distnce = findDistance(circleAx, circleAy, circleBx, circleBy)
    return distance <= circleAr + circleBr
