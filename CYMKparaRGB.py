import math

def converterCYMKparaRGB(c, y, m, k):
    r = int(255*((1-c)*(1-k)))
    g = int(255*((1-m)*(1-k)))
    b=  int(255*((1-y)*(1-k)))
    return r, g, b

def main():
    print("Conversão C 0.0, Y 0.75, M 0.5 e K  0.0 para RGB: ")
    rgb = converterCYMKparaRGB(0.0, 0.75, 0.5,0.0)
    print("Resultado: \nR "+str(rgb[0])+" \nG "+str(rgb[1])+" \nB "+str(rgb[2]))
    
if __name__ == "__main__":
    main()
