function calcuateWeighted(fives, fours, threes, twos, ones, zeroes) {
    return (5*fives + 4*fours + 3*threes + 2*twos + 1*ones)/(fives + fours + threes + twos + ones +zeroes)
}

function calcuateUnweighted(fives, fours, threes, twos, ones, zeroes) {
    return (4*(fours + fives) + 3*threes + 2*twos + 1*ones)/(fives + fours + threes + twos + ones +zeroes)
}

