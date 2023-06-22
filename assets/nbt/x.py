import binascii


def analysis(bin_path: str, out_txt_path: str):
    with open(bin_path, 'rb') as f:
    	# 读取全部行
        all_data = f.readlines()
        
        with open(out_txt_path, 'a+') as new_f:
            for i in all_data:
            	# 二进制（bytes）类型转换成十六进制类型
                hex_str = binascii.b2a_hex(i).decode('unicode_escape')
                # 以str格式逐行写入到文本
                new_f.write(str(hex_str) + '\n')
        print("解析完成")

analysis('a.nbt','a.txt')