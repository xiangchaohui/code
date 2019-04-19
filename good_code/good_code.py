

import os
def find_all_file(fir_path):
    '''
    获取该路径下所有子和孙的文件
    '''
    all_path = [os.path.join(fir_path, x) for x in os.listdir(fir_path)]
    get_file_path = [ x for x in all_path if os.path.isfile(x)]
    second_file = [find_all_file(x) for x in all_path if os.path.isdir(x)]
    result = get_file_path + sum(second_file, [])
    return result