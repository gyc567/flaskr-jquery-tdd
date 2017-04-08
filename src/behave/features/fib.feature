Feature:Calc Fib
  In order to introduce Behave
  We calc fib as example

  Scenario Outline: Calc fib number
    Given we have the number <number>
    When we calc the fib
    Then we get the fib number <fib_number>

    Examples: Some Numbers
      | number | fib_number |
      | 1      | 1          |
      | 2      | 1          |
      | 9      | 34         |
      | 10     | 55         |