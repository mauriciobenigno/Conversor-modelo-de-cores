import math

def converterRGBparaHSI(r, g, b):
    r, g, b= round(r/255.0, 4), round(g/255.0, 4), round(b/255.0, 4)
    Cmax = max(r, g, b)
    Cmin = min(r, g, b)
    delta = round(Cmax-Cmin, 4)
    if delta == 0:
        h = 0
    elif Cmax == r:
        h = (((g-b)/delta)%6)*60
    elif Cmax == g:
        h = (60 * ((b-r)/delta)+2)
    elif Cmax == b:
        h = (60 * ((r-g)/delta)+4)   
    if Cmax == 0:
        s = 0
    else:
        s = delta/Cmax
    i = Cmax
    return h, s, i

def main():
    print("Conversão r 255, g 127, b 63 para HSI: ")
    hsi = converterRGBparaHSI(255, 127, 63)
    print("Resultado: \nH "+str(round(hsi[0],0))+" \nS "+str(round(hsi[1]*100, 2))+"% \nI "+str(round(hsi[2]*100, 2))+"%")
    
if __name__ == "__main__":
    main()
