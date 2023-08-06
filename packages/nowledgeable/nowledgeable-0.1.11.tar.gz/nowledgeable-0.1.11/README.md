# Nowledgeable exercice check

This module let student check their answers outside nowledgeable, anywhere. 

Allows exercices to be run outside the nowledgeable application. 

Allow also testing complex applications

Contain also the python exercice unit framework

## installation 

```bash

pip3 install nowledgeable

```

## usage 

### Exercice checking 


Run the following in an exercice containing an exercice with the exercice.yaml specification
```bash

nowledgeable run-checks

```

or 

```bash

nowledgeable run-checks /path/to/exercice.yaml

```


Watching for file update and reruning files automatically

```bash 
nowledgeable watch
``` 


### using the unit testing library 


```python 


from python_utils.utils import AnswerTester

tester = AnswerTester() #singleton pattern

## add assertions


tester.print_test_output()

```
#### Exemples

imagine you have the following wording : 

"Code the function multiply_by_two(x) return 2 * x for each x"

You can use  `compare_function`.

for that you need to : 

1. code the proper function
2. specify a test_inputs variables which will be fed to the student function and the good one.

```python

def solution(x): return 2 * x

tester = AnswerTester()

test_inputs = [
    [3], # la fonction sera testée avec l'argument x=3
    [-2],# la fonction sera testée avec l'argument x=-2
    [random.randint(-3, 3)] #la fonction sera testée avec un x aléatoire entre -3 et 3
]

tester.compare_functions("nom test", multiply_by_two, solution, test_inputs, "message")

result_status = tester.get_test_output()

result = tester.get_test_output() #A la fin on demande de générer le json

```
