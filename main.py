import pandas as pd
import os
import vc_inverter as inv

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

def main():
    DATA_FILE = 'Sample_data.xlsx'
    sheet_to_read = 'VCInverter_data' #depois fazer lista com os nomes das sheets e func para iterar
    df_sys_data = read_data_from_sheet( DATA_FILE, sheet_to_read )

    print(df_sys_data)
    #print(df_sys_data['kq [V/Var]'] )

    l_vc_invs = get_list_vc_invs( df_sys_data )
    print(l_vc_invs[0].droop.Ap)
    print('o parametro droop é: ', l_vc_invs[0].droop.w_fp)
    print('o parametro droop é: ', l_vc_invs[1].droop.w_fp)
    print(len(l_vc_invs))


if __name__ == '__main__':
    main()