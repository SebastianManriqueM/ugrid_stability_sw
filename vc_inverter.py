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

        self.Ap   = self.get_ss_model()    
        #self.Ap   = np.array([])
        
    def get_ss_model( self ):
        self.Ap = np.array( [ [ 0 , -self.kp   , 0 ],
                              [ 0 , -self.w_fp , 0 ],
                              [ 0 ,  0         , -self.w_fq] ] )
            
        return self.Ap

    


#teste = VCInverter()
#print(teste.Droop.get_ss_model())