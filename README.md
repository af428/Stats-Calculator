[![Build Status](https://travis-ci.com/af428/calc2.svg?branch=master)](https://travis-ci.com/af428/calc2)

# Stats Calculator
* Stats Calculator
    1. Properties
        * Result
    3. Math Operation Methods
        * Addition - Calls addition static method
        * Subtraction - Calls subtraction static method
        * Multiplication - Calls multiplication static method
        * Division - Calls division static method
        * Square - Calls square static method
        * Square Root - Calls square root static method
    4. Random Generator
        * listPick Methods
            * return random choice
            * use seed
            * use RandomGenerator.randNum to generate list
    5. Population Sampling Functions
        * randomSampling
        * confidenceInterval
        * marginOfError
        * cochranFormula
        * sampleSize
    6. Descriptive Statistics Functions
        * mean
        * median
        * mode
        * variance
        * standard deviation
        * z-score
 
 # Task Breakdown
* Random Generator Function
    * Description: The random module uses the seed value as a base to generate a random number. if seed value is not present it takes system current time.
    * Tasks 
        * random number without a seed between a range of two numbers 
        * random number with a seed between a range of two numbers(integer and decimal
        * list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
        * selecting random item from list 
        * setting a seed and randomly.select the same value
        * selecting n number of items from a list without a seed 
        * selecting n number of items from a list with a seed
    * Use Functions (make sure to import the random module)
        * <code>.seed()</code>used to initialize the random number generator.
        * <code>.random()</code> for generating random floats
        * <code>.randint()</code> for generating random integers
        * <code>.randrange()</code> for generating random numbers within a range
        * <code>.choice()</code> for randomly selected element 
          
* Populating Sampling Functions
    * Description: Computing statistical functions using statistics module
    * Tasks 
        * Simple random sampling
        * Confidence Interval For a Sample 
        * Margin of Error 
        * Cochran’s Sample Size Formula 
        * How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    * Use functions
        * <code>.sample()</code> to choose sample/multiple items from a Python list, set, and dictionary
        * <code>scipy.stats.t.interval()</code> to find the confidence interval of a sample statistic
                
* Descriptive Statistics Functions
    * Description: Creating functions for basic stats operations
        * Mean - sum of all divided by count
        * Median - middle integer
        * Mode - highest count of instances of a num
        * Variance - subtract the Mean and square the result (the squared difference) then workout the average
        * Standard Deviation - square root of the variance
        * Z-Score - raw score minus the population mean divided by the population standard deviation
    * Use functions:
        * Use <code>import numpy</code> See example
            * <code>np.mean()</code>
            * <code>np.median()</code>
            * <code>np.mode()</code>
            * <code>np.var()</code>
            * <code>np.std()</code>
            * <code>.stats.zscore</code> Make sure to <code>from scipy import stats</code>

# Contributers
* [Alexandra Feeley](https://github.com/af428)
* [Luka Dragoljic](https://github.com/LukaDragolijc)
* [Charles Wicklund]() 

