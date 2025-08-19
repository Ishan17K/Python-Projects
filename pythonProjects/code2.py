def slower():
    start = "Hello who are you I speak fast"
    x = start.replace(" ","...")
    return x

def lowercase():
    name =  input("Hello Who Are YOU").lower()
    return name

def mc():
    c = 300000000
    m = input("What is m")
    return (int(m)*c*c)

if __name__ == "__main__":
    print(lowercase())