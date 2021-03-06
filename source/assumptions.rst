.. _understanding:

Understanding and Assumptions
===============================

It was understood clearly from the challenge description that a farm will have N pens - A room/barn where cows of same breed are put in.
The objective of the challenge is to find out

1. Estimated milk each pen will produce
2. Cost to maintain each pen/Overall farm
3. Greenhouse gas generated in this scenario

In order to achieve the result, following assumptions and decision were made:

1. Each cow will produce 1 gallon of milk
2. Few calculation were reduced to basic assumptions.
    * Milk Estimate = Number of days * number of cows in the pen
    * **Cost estimation = Number of days * number of cows in the pen * cost per cow**

3.Since, each pen will have one breed, the need for having a separate cow class was eliminated as no proper reasoning for having one was laid out.


.. _classdiagram:

Class and Relation
---------------------

.. image:: class.png
    :align: center


.. _implement:

Implementation
-------------------------

1.  To achieve the result, I made use of Python and have implemented the solution incorporation OOP as instructed.

2.  Python- unittest library was used to perform the unit test.

The final result allows the user to 

1.  create pen(s) - User can create a single or multiple pens. Few details will be asked for each pen.Such as

    *  Name of the breed

    *  Total capacity of the pen

    *  Cost for feeding one cow in the pen

2.  Add cows - Allows user to add cows in the pen. Will prevent the user to add cows of breed for which pen doesn't exist

3.  Milk Estimate - Provide the estimate of the milk that can be produced in N days

4.  Cost of Pen - Provides the estimated cost to feed pen for N days

5.  Cost of Farm - Provides the estimated cost to feed all pens for N days


.. _code:

Run the code
------------

1.  Command : ** ./job.sh **

2.  If required, mark it executable using ** chmod u+x job.sh **

Python 3.6 was used.






