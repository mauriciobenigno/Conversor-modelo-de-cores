import math

def converterHSIparaRGB(h, s, i):
    h = float(h)
    s = float(s)
    i = float(i)
    C=i*s
    X=C*(1-abs(((h/60)%2)-1))
    m=i-C
    r, g, b = 0.0, 0.0, 0.0
    if h >= 0 and h < 60:
        r, g, b = C, X, 0.0
    elif h >= 60 and h <120:
        r, g, b = X, C, 0.0
    elif h >=120 and h <180:
        r, g, b = 0.0, C, X
    elif h >=180 and h <240:
        r, g, b = 0.0, X, C
    elif h >=240 and h <300:
        r, g, b = X, 0.0, C
    elif h >=300 and h <360:
        r, g, b = C, 0.0, X
    R = int((r+m) * 255)
    G = int((g+m) * 255)
    B = int((b+m) * 255)
    return R, G, B

def main():
    print("Conversão H 20, S 0.7529, I 1 para RGB: ")
    rgb = converterHSIparaRGB(20, 0.7529, 1)
    print("Resultado: \nR "+str(rgb[0])+" \nG "+str(rgb[1])+" \nB "+str(rgb[2]))
    
if __name__ == "__main__":
    main()
