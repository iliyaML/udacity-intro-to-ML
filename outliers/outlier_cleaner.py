#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    import numpy

    print predictions
    print ages
    for i in range(0, 90):
        error = numpy.subtract(predictions, net_worths)
        print numpy.power(error, 2)

    return cleaned_data
