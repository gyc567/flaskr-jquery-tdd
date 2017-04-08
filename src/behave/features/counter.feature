Feature: implements Calculator
  In order to implements plus
  We calc int as example

#  加法
  Scenario Outline: Calc   number
    Given we have two number <number1>,<number2>
    When we calc the plus
    Then we get the sum number <sum_number>

    Examples: Some Numbers
      | number1 | number2 | sum_number |
      | 1       | 1       | 2          |
      | 2       | 1       | 3          |
      | 9       | 34      | 43         |
      | 11      | 55      | 66         |

#减法
  Scenario Outline: minus   number
    Given my have two number <number1>,<number2>
    When my calc the minus
    Then my get the minus number <minus_number>

    Examples: Some Numbers
      | number1 | number2 | minus_number |
      | 1       | 1       | 0            |
      | 2       | 1       | 1            |
      | 9       | 34      | -25          |
      | 11      | 55      | -44          |

#  乘法
  Scenario Outline: ride   number
    Given you have two number <number1>,<number2>
    When you calc the ride
    Then you get the ride number <ride_number>

    Examples: Some Numbers
      | number1 | number2 | ride_number |
      | 1       | 1       | 1           |
      | 2       | 1       | 2           |
      | 9       | 34      | 306         |
      | 11      | 55      | 605         |

#除法
  Scenario Outline: division   number
    Given he have two number <number1>,<number2>
    When he calc the division
    Then he get the division number <division_number>

    Examples: Some Numbers
      | number1 | number2 | division_number |
      | 2       | 1       | 2              |
      | 3       | 1       | 3               |
      | 6       | 2       | 3               |
      | 60      | 3       | 20              |

