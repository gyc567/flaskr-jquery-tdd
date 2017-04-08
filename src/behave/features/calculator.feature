Feature: implements Calculator
  In order to implements plus
  We calc int as example

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