import numpy as np
import pandas as pd

class VCInverter:
    
    def __init__( self, df_data, w_nom=376.999 ):
        self.w_nom = w_nom
        self.droop = Droop(df_data)


class Droop: #criar inner class basic data, etc
    def __init__(self, df_data):
        self.kp   = df_data.iloc[5]
        self.kq   = df_data.iloc[6]
        self.w_fp = df_data.iloc[7]
        self.w_fq = df_data.iloc[8]
        self.Rv   = df_data.iloc[9]
        self.Lv   = df_data.iloc[10]
        self.get_lin_ss_model()
        #self.get_nlin_ss_model() 

    def get_nlin_ss_model1( y, t, b, c):
        omega, theta = y
        dydt =  omega     
        return dydt
    
    def get_nlin_ss_model2( y, t, b, c):
        omega, theta = y
        dydt = -b*omega - c*np.sin(theta)    
        return dydt
    
    #def func_agg( self, f_list ):
    #    dydt = [ 0 , 0 ]
    #    def wrapper(self, y, t, b, c):
    #        for i, fun in enumerate(f_list):
    #            dydt[i] = self.fun( y, t, b, c)
    #        return dydt
    #    return wrapper

    def get_lin_ss_model( self ):
        self.Ass      = np.array( [ [ 0 , -self.kp   , 0 ],
                                    [ 0 , -self.w_fp , 0 ],
                                    [ 0 ,  0         , -self.w_fq] ] )
    

        self.Bss_lc   = np.array( [ [ 0 , 0 ,     0      ,     0     ],
                                    [ 0 , 0 , self.w_fp  , self.w_fp ],
                                    [ 0 , 0 , -self.w_fp , self.w_fp ] ] )    

        self.Bss_io   = np.array( [ [     0      ,     0     ],
                                    [ self.w_fp  , self.w_fp ],
                                    [ self.w_fp  ,-self.w_fp ] ] )

        self.Bss_wcom = np.array( [ [ -1 ] , [ 0 ] , [ 0 ] ] )

        self.Bss_pref = np.array( [ [ self.kp ] , [ 0 ], [ 0 ] ] )    
        

    


#teste = VCInverter()
#print(teste.Droop.get_ss_model())