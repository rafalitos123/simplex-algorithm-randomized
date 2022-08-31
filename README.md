# simplex-algorithm-randomized

## Installation

```bash
cd gilp
pip install -e .[dev]
```

## How to run

```bash
python main.py
```

## Output

Dantzig simplex algorithm on Klee-Minty 3D cube
![image](https://user-images.githubusercontent.com/104710636/187679787-f3c62e48-a025-40d0-8a62-532364893d76.png)



Randomized simplex algorithm on Klee-Minty 3D cube
![image](https://user-images.githubusercontent.com/104710636/187679846-5ffb7ac9-0463-44a0-857a-2a05d66b9de6.png)


(Note the difference in number of iterations and path)

```bash
Running dantzig, bland and random-edge simplex algorithm for various examples and compare results

Running Simplex algorithm on case RANDOM_INTEGER_7D_LP:
With Bland rule: 9 pivots
With Dantzig rule: 10 pivots
With Randon-Edge rule: 6.4 pivots (average over 10 executions)

Running Simplex algorithm on case ALL_INTEGER_2D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 3.8 pivots (average over 10 executions)

Running Simplex algorithm on case LIMITING_CONSTRAINT_2D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 4.0 pivots (average over 10 executions)

Running Simplex algorithm on case DEGENERATE_FIN_2D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 4.0 pivots (average over 10 executions)

Running Simplex algorithm on case KLEE_MINTY_2D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 3.4 pivots (average over 10 executions)

Running Simplex algorithm on case ALL_INTEGER_3D_LP:
With Bland rule: 5 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 4.6 pivots (average over 10 executions)

Running Simplex algorithm on case MULTIPLE_OPTIMAL_3D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 4.0 pivots (average over 10 executions)

Running Simplex algorithm on case SQUARE_PYRAMID_3D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 4.0 pivots (average over 10 executions)

Running Simplex algorithm on case KLEE_MINTY_3D_LP:
With Bland rule: 6 pivots
With Dantzig rule: 8 pivots
With Randon-Edge rule: 4.6 pivots (average over 10 executions)

Running Simplex algorithm on case DODECAHEDRON_3D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 4.0 pivots (average over 10 executions)

Running Simplex algorithm on case STANDARD_2D_IP:
With Bland rule: 3 pivots
With Dantzig rule: 3 pivots
With Randon-Edge rule: 3.0 pivots (average over 10 executions)

Running Simplex algorithm on case EVERY_FATHOM_2D_IP:
With Bland rule: 2 pivots
With Dantzig rule: 2 pivots
With Randon-Edge rule: 2.0 pivots (average over 10 executions)

Running Simplex algorithm on case VARIED_BRANCHING_3D_IP:
With Bland rule: 4 pivots
With Dantzig rule: 3 pivots
With Randon-Edge rule: 3.6 pivots (average over 10 executions)

Running Simplex algorithm on case CLRS_INTEGER_2D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 3.3 pivots (average over 10 executions)

Running Simplex algorithm on case CLRS_SIMPLEX_EX_3D_LP:
With Bland rule: 3 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 3.5 pivots (average over 10 executions)

Running Simplex algorithm on case CLRS_DEGENERATE_3D_LP:
With Bland rule: 4 pivots
With Dantzig rule: 4 pivots
With Randon-Edge rule: 3.3 pivots (average over 10 executions)
```
