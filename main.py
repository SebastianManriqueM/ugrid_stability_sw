import pandas as pd
import numpy as np
import os
import vc_inverter as inv
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def read_data_from_sheet( DATA_FILE , sheet_to_read ):
    abs_path = os.path.dirname(__file__)
    rel_path = "Data"
    full_path = os.path.join(abs_path, rel_path)
    df_data = pd.read_excel( full_path+'\\'+DATA_FILE , sheet_name=sheet_to_read )
    return df_data

def get_list_vc_invs( df_sys_data ):
    l_vc_invs = []
    for i in range( len(df_sys_data.index) ):
        l_vc_invs.append( inv.VCInverter( df_sys_data.iloc[i,:]) )
    return l_vc_invs

def func_agg( f_list ):
    dydt = [ 0 , 0 ]
    def wrapper( y, t, b, c):
        for i, fun in enumerate(f_list):
            dydt[i] = fun( y, t, b, c)
        return dydt
    return wrapper

def main():
    DATA_FILE = 'Sample_data.xlsx'
    sheet_to_read = 'VCInverter_data' #depois fazer lista com os nomes das sheets e func para iterar
    df_sys_data = read_data_from_sheet( DATA_FILE, sheet_to_read )

    print(df_sys_data)
    #print(df_sys_data['kq [V/Var]'] )

    l_vc_invs = get_list_vc_invs( df_sys_data )
    print(l_vc_invs[0].droop.Ass)
    print('o parametro droop é: ', l_vc_invs[0].droop.w_fp)
    print('o parametro droop é: ', l_vc_invs[1].droop.w_fp)
    
    f_list = [ l_vc_invs[0].droop.get_nlin_ss_model1, l_vc_invs[0].droop.get_nlin_ss_model2 ]
    fun = func_agg( f_list )
    b = 0.25
    c = 5.0
    y0 = [np.pi - 0.1, 0.0]
    t = np.linspace(0, 10, 101)
    sol = odeint(fun, y0, t, args=(b, c))
    plt.plot(t, sol[:, 0], 'b', label='theta(t)')
    plt.plot(t, sol[:, 1], 'g', label='omega(t)')
    plt.show()
    print(len(l_vc_invs))


if __name__ == '__main__':
    main()