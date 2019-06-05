import math

def converterRGBparaCYMK(r, g, b):
    r, g, b= round(r/255.0, 4), round(g/255.0, 4), round(b/255.0, 4)
    K = 1-max(r, g, b)
    C = ((1-r-K)/(1-K))
    M = ((1-g-K)/(1-K))
    Y = ((1-b-K)/(1-K))
    return C, Y, M, K

def main():
    print("Conversão r 255, g 127, b 63 para CYMK: ")
    cymk = converterRGBparaCYMK(255, 127, 63)
    print("Resultado: \nC "+str(round(cymk[0]*100, 0))+" \nY "+str(round(cymk[1]*100, 0))+" \nM "+str(round(cymk[2]*100, 0))+" \nK "+str(round(cymk[3]*100, 0)))
    
if __name__ == "__main__":
    main()
