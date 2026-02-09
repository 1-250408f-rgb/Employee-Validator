
class Person:
    def __init__(self, Name: str, Age: int):
        self._name = Name
        self._age = Age
    
    @staticmethod
    def NameValidator(name: str):
        """Check if the name's are valid"""
        if len(name) < 0 or name == "":
            raise ValueError
        elif isinstance(name, int):
            raise TypeError
        else:
            return f'Name: {name.title().split()}'
    @staticmethod  
    def AgeValidator(age: int):
        """Age validator"""
        if age < 0 or isinstance(age, str):
            raise ValueError
        else:
            return f'Age: {age}'
        
    def __str__(self) -> str:
        return f'Name: {self._name} \n Age: {self._age}'
        
class Account:
    
    @staticmethod
    def UsernameValidator(username: str): 
         """username must be unique"""
         if username.islower() and username.title():
            return True
         else:
            return False
    
    @staticmethod       
    def passwordvalidator(password: str):
        """password need to be strong"""
        
        if len(password) < 7:
            return 'This password is weak'
        elif len(password) > 8:
            return 'Password is Strong'
        else:
            return 'Error try again'
        
class Employee:

    @staticmethod
    def EmployeeIdCreator(employee_id):
        """Employee id must be unique"""
        employee_id = [i for i in range(1, 1000)]
        return employee_id
    

class Position:
    
    position_list = ['Manager', 'Developer', 'Designer', 'Tester', 'HR']
    
    @staticmethod
    def PositionValidator(position: str):

        if position in Position.position_list:
            return f'Position: {position}'
        else:
            raise ValueError('Position not found')
        
class Main:
    def __init__(person: Person, account: Account, employee: Employee, position: Position):
        self._person = person
        self._account = account
        self._employee = employee
        self._position = position

if __name__ == "__main__":
    person1 = Person('John Doe', 30)
    print(person1)
    
    account1 = Account()
    print(account1.UsernameValidator('johndoe'))
    print(account1.passwordvalidator('password123'))
    
    employee1 = Employee()
    print(employee1.EmployeeIdCreator(12))
    
    position1 = Position()
    print(position1.PositionValidator('Developer'))

   

            


