import os
os.system("cls")

print("="*30)
print(f"{" TYPE HINTS ":^30}")
print("="*30)


## penggunaan type hints
import string

# int kuadrat(int nilai)
def kuadrat(angka : int) -> int :
    kuadrat = angka**2
    return kuadrat
a = kuadrat(2)
print(a)

def display(argument:string) -> str:
    print(argument)
display("cup")
    