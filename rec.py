def body( ITR=None ):
    print( "Printing from inside of body()" ,  1 * ITR )
    return 1 * ITR

def loop( var = None , con = None , itr = None , body = None , arg = None , fout = None ):

    '''
        Inputs:
            `var` = Iteration variable for looping
            `con` = Condition for looping
            `itr` = Iteration condition
            `body` = Function applied as loop's body
            `arg` = Arguments supplied to body of loop
            `fout` = Output of the function will be saved in this list
        
        Outputs:
            Output of body function is returned
    '''

    # initialize
    if type(var) == str :
        g = {}
        l = {}
        exec( var , g , l )

        # Variable name will be before `=` like for instance, in XYZ=... , XYZ will be variable name
        variable_name = var[ : var.index('=') ]

        var = l[ variable_name ]

    # condition
    if type(con) == str and not eval(con):
        if type(fout) == list :
            return fout
        else:
            return

    if not body:
        print( f"\nvar : {var}\ncon : {con}\nitr : {itr}" )
    else:
        if arg == "ITR":
            if type(fout) == list :
                fout.append( body( var ) )
            else:
                body( var )
        else:
            if type(fout) == list :
                fout.append( body( arg ) )
            else:
                body( arg )
    
    # iteration
    if itr:
        if "+" in itr:
            count = itr.replace('+','')
            var += count or 1

        elif "-" in itr:
            count = itr.replace('-','')
            var -= count or 1

        elif "*" in itr:
            count = itr.replace('*','')
            var *= count or 1

        elif "/" in itr:
            count = itr.replace('/','')
            var /= count or 1
        
    return loop( var , con , itr , body , arg , fout )

# loop( "var=5" , "var<10" , "+" , body , "ITR" )
outputs = loop( "var=1" , "var<=10" , "+" , body , "ITR", [] )
print( outputs )
