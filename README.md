# 1. Introduction
## a. What is the goal of the coursework?
All programmers sooner or later move from simple tasks to more complex projects.Although I am not a programmer, successful coursework allows you to become more deeply familiar with the principles of OOP, the principles of SOLID, and architectural solutions. My goal is not just to write working code, but to use the knowledge accumulated in lectures and lab work to make the code applicable for its further improvement and innovation.
## b. What is your application? 
The theme of my project work is snake. Why this theme? The thing is that I always wanted to create some kind of my own game, but I never found the time for it, and the game itself is very well suited for the implementation of OOP principles, which I will try to prove in the main part. The aplication of snake is a simple entertainment.
## c. How to use the program?
Install Pygame `pip install pygame`.Then the program works very simply. We press the RUN CODE button(Cltr+Alt+N) in game.py module, launch the compiler and see the snake. By using the UP, DOWN, LEFT, RIGHT buttons in the keyboard, we move the snake in the direction we need, if the snake goes beyond the map, the game ends. If the snake collects fruit, it increases by 1 cell, the more fruits we collect, the more will be score.
# 2. Body/Analysis
## a. Polymorphysm
- **Polymorphism** is a programming concept that lets a method perform different tasks depending on the object it's working with, even if the objects are of different types. 

 - In my code polymorphism is implemented through the abstract class `MoveStrategy` and its subclasses `KeyboardMoveStrategy` and `AIMoveStrategy`.

 - In abstract class `MoveStrategy` we use method `def get_direction` that does nothing:

```Python
class MoveStrategy(ABC):
    @abstractmethod
    def get_direction(self, current_direction, snake=None, fruit=None):
        pass
```
 - Then we use the same method for writing our own movement strategy:

```Python 
class KeyboardMoveStrategy(MoveStrategy):
    def get_direction(self, current_direction, snake=None, fruit=None):
	{
		...
	}
```
```Python 
class AIMoveStrategy(MoveStrategy):
    def get_direction(self, current_direction, snake=None, fruit=None):
	{
		...
	}
```
- It is convinient, because it is easier to switch behaviour, your code is open for extensions, but closed for modifications, you avoid using if else statements
## b. Abstraction
- **Abstraction** means hiding internal implementation details and exposing only what’s necessary to the outside world.
- In my code abstraction is implemented in abstract class `class MoveStrategy(ABC)`. This defines what a strategy should do: it must provide `get_direction`. It does not define how — this is left to subclasses like `KeyboardMoveStrategy` and `AIMoveStrategy`:
```Python
class MoveStrategy(ABC):
    @abstractmethod
    def get_direction(self, current_direction, snake=None, fruit=None):
        pass
```
- It means that I abstract the concept of moving logic from the game logic. It makes code more readable.
## c. Inheritance
- **Inheritance** allows you to create new classes (subclasses) that inherit properties and behaviors from existing classes (superclasses). 
- You can see inheritance in *strategies.py* module, where my parent class is `MoveStrategy` and child classes are `KeyboardMoveStrategy`, `AIMoveStrategy`.
- Inheritance helps to avoid the dupllication of the code and specialize behaviour in child class
## d. Encapsulation
- **Encapsulation** is a way to hide internal data of attributes, methods.
- There are 3 types of access controls: *public*, *private*, *protected*.
- In mu course work more often I was using private access control. For example: `_body`, `_direction`, `_positions_set` and e.t.c.
- I do not access private attributes directly but through *get methods*, so that theu would not be changed directly, outside the class.
## e. Composition
- **Composition** is a case when one object can not indepentelntly exict without.
```Python
  class Game:
    def __init__(self):
        self._snake = Snake()
        self._fruit = Fruit()
        self._strategy = KeyboardMoveStrategy()
 ```
 - In this code inside game class we create attributes, that can not exict independently without Game class.
## f. Strategy design pattern
  - **Strategy design pattern** allows easily change the behaviour of the object
  - *Strategy* consists of 3 main components: 
  
  - *context* (class which uses strategy)
  ```Python
	self._strategy = KeyboardMoveStrategy()
	...
	direction = self._strategy.get_direction(...)
```
- *strategy interface* (abstract class that describes behaviour in general)
```Python
class MoveStrategy(ABC):
    @abstractmethod
    def get_direction(self, current_direction, snake=None, fruit=None):
        pass
```
- *concrete strategies* (strategies, that implement abstract class in their own way)
```Python
  class KeyboardMoveStrategy(MoveStrategy):
    def get_direction(...): ...
```
```Python
	class AIMoveStrategy(MoveStrategy):
    	def get_direction(...): ...
```
- Strategy design patterns allows to add new functionality, without changing the code, which makes the code more flexible and extensible
## g. Reading from file
- `_load_highscore` method checks if `scores.txt` exict, reads all numeric lines, extracts the maximum score:
 ```Python
  def _load_highscore(self):
        if not os.path.exists(SCORES_FILE):
            return 0
        with open(SCORES_FILE, 'r') as file:
            scores = [int(line.strip())
                      for line in file if line.strip().isdigit()]
            return max(scores) if scores else 0
```
## h. Writing to file
- `_save_score` adds the new score, limits the list to `MAX_SCORES` value, write the updated scores to `scores.txt`:
  
```Python
def _save_score(self):
        scores = []
        if os.path.exists(SCORES_FILE):
            with open(SCORES_FILE, 'r') as file:
                scores = [int(line.strip())
                          for line in file if line.strip().isdigit()]
        scores.append(self._score)
        scores = sorted(scores, reverse=True)[:MAX_SCORES]
        with open(SCORES_FILE, 'w') as file:
            for score in scores:
                file.write(f"{score}\n")
```
# Results and Summary
- Althogh the code is not ideal and has some serious issues such as absense of unit tests, which means that code not always might work as it should be, it still covers most of the requirements. Because of the *Strategy* design pattern, it is a lot more easier to add some new functionality related with movement or even add a new *Strategy* design pattern, that might be responsible for different type of foods, different type of snakes and e.t.c.. The biggest issue for me was the fact that I was not able to write unit tests, because compilor could not find modules like *snake*, *fruit*. I did everything ti fix this problem but unfortunately because of the lack of time I was not able to figure out this problem.
