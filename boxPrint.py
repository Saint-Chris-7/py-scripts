def boxPrint(symbol,height,width):
    if len(symbol)!= 1:
        raise Exception("Symbol must be a single character string")
    if height <=2:
        raise "height must be greater thann two"
    if width <=2 :
        raise Exception("width must be greater than two")
    
    print(symbol*width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
        print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err)) 

