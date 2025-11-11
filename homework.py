def matrix(rows, numbers):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Количество строк должно быть положительным целым числом")
    if not isinstance(numbers, int) or numbers <= 0:
        raise ValueError("Количество чисел в строке должно быть положительным целым числом")
    number=1
    for i in range(rows):
        for j in range(numbers):
            print(number,end=" ")
            number+=1
        print()


def treugolnik():
    number=1
    n=int(input())
    for i in range (1,n+1):
        for j in range (i):
            print (number,end=" ")
            number+=1
        print()

def obt_treugolnik(n):
    number=6
    #n=number=int(input())
    for i in range (n,0,-1):
        print("" * (n - i), end=" ")
        for j in range (i):
            print(number,end=" ")
            number-=1
        print()

def my_range(stop: float, start: float = 0.0, step: float =1.0):
    result=start
    li=[]

    while result<stop:
        li.append(result)
        result = result + step

def my_rangerator(stop: float, start: float = 0.0, step: float =1.0):
    result=start
    while (result<stop):
        yield result
        result += step


def chain_sum(value: int = None):
    total=value or 0

    def vnutri(value: int = None):
        nonlocal total
        if value == 0 or value is None:
            return total
        else:total+=value
        return vnutri
    return vnutri

def dictionnary_to_string(value, indent=0):
        result=[]
        if isinstance(value, int):
            result.append(f"value={str(value)}")
        elif isinstance(value, list):
            result.append(f"array={str(value)}")
        elif isinstance(value, dict):
            for key,value in value.items():
                row= f'\n{" " * indent}{key}: {dictionnary_to_string(value, indent + 2)}'
                result.append(row)
        return ''.join(result)


def is_substring(string: str, sub_string: str):
    string=string.lower()
    sub_string=sub_string.lower()
    result=(sub_string in string)
    return result

def to_snake_case(value: str):
    new_string=value.replace(" ","_")
    return new_string.lower()

def is_valid_tupoe(value: str):
    krugl_l=value.count('(')
    krugl_r=value.count(')')
    figur_l=value.count('{')
    figur_r=value.count('}')
    kvadrat_l=value.count('[')
    kvadrat_r=value.count(']')
    if krugl_l==krugl_r and figur_l==figur_r and kvadrat_l==kvadrat_r:
        return True
    else:
        return False

def is_valid_umnoe(value:str):
    proverka=[]
    mapping={')': '(', '}': '{', ']': '['}
    for char in value:
        if char in mapping.values():
            proverka.append(char)
        elif char in mapping:
            if not proverka or proverka[-1] != mapping[char]:
                return False
            proverka.pop()
    return not proverka


matrix(1,5)