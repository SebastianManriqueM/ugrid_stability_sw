import numpy as np

class VCInverter:
    
    def __init__( self, kp=1.6e-3, kq=7.5e-4, wf_p=30, wf_q=30, Rv=0, Lv=0, w_nom=376.999 ):
        self.kp   = kp
        self.kq   = kq
        self.wf_p = wf_p
        self.wf_q = wf_q
        self.Rv   = Rv
        self.Lv   = Lv

        self.Ap   = np.array([])

        self.w_nom = w_nom

    def get_ss_model( self ):
        self.Ap = np.array( [ [ 0 , -self.kp   , 0 ],
                              [ 0 , -self.wf_p , 0 ],
                              [ 0 ,  0         , -self.wf_q] ] )
        
        return self.Ap

    


teste = VCInverter()
print(teste.get_ss_model())