
def count_characters(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vo=co=dig=spechr=0
    for i in str:
        if i in vowels:
            vo += 1
        elif i.isalpha():
            co += 1
        elif i.isdigit():
            dig += 1
        else:
            spechr += 1
    return (vo,co,dig,spechr)

def main():
    str = input("enter string ").lower()
    vo, co, dig, spechr = count_characters(str)
    print(f"vowels={vo} consonents={co} digits={dig} special characters={spechr}")
    print(str[::-1])
main()