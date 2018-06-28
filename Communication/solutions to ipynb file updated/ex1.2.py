def create_master_turnstile_file(filenames, output_file):
    check_dir(output_file.rsplit("/", 1)[0])
    
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in filenames:
            with open(filename, 'r') as f_in:
                f_in.readline()
                master_file.write(f_in.read())
    
    return output_file

print "Merging files..."
output_dir = "output"
turnstile_file = create_master_turnstile_file(datapath, output_dir + "/turnstile_1706.txt")
print "Files merged..."