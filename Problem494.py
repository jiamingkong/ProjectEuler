#include <algorithm>
#include <iostream>
#include <bitset>
#include <unordered_set>
#include "ProblemMap.h"
#include "Utils.h"

/*
https://projecteuler.net/problem=494
*/

void ProblemMap::Problem494()
{ 
    const long long MAX = 10000000;//LLONG_MAX;
    const int familyN = 10;

    long long start = Utils::FibN(familyN);

    int seriesLength;
    int lastCollatzValue;
    long long collatzN;

    std::bitset<familyN-1> seriesFamilyType = std::bitset<familyN-1>(false);

    std::unordered_set<std::bitset<familyN - 1>> seenFamilyTypes = std::unordered_set<std::bitset<familyN - 1>>();

    for (collatzN = 0; collatzN < MAX; ++collatzN)
    {
        seriesLength = 0;
        lastCollatzValue = 0;

        for (int i : Utils::Collatz(collatzN))
        {
            seriesLength++;

            if (seriesLength != 1 && seriesLength < familyN)
                seriesFamilyType[seriesLength-2] = i > lastCollatzValue;

            if (seriesLength > familyN)
                break;

            lastCollatzValue = i;
        }

        if (seriesLength == familyN)
            seenFamilyTypes.insert(seriesFamilyType);

        seriesFamilyType.set(false);
    }

    std::cout << seenFamilyTypes.size() << std::endl;
}