import cisco
import syslog

sh_mod_op_str = cli ('show module')

sh_mod_op_list = sh_mod_op_str.split('\\n')
newlist = []
for each_line in sh_mod_op_list:
    if (each_line != ''):
        newlist.append(each_line)
    else:
        break

sh_mod_op_list = []

for each_line in newlist:
    if ('Supervisor' not in each_line and each_line[0].isdigit()):
        sh_mod_op_list.append(each_line)

for each_line in show_mod_op_list:
    sh_fwd_con_string = cli ('show forwarding consistency l2 ' + each_line[0] + ' | be VLAN')
    sh_fwd_con_list = sh_fwd_con_string.split('\\n')
    if (sh_fwd_con_list[5] != ''):
        sh_fwd_con_list = sh_fwd_con_list[5: len(sh_fwd_con_list) - 2]
        for each_line in sh_fwd_con_list:
            info_list = each_line.split(" ")
            formatted_list = []
            for line in info_list:
                if line!= "":
                    formatted_list.append(line)
            syslog.syslog(3, 'Mac inconsistency detected on module ' + each_line[0]+ ' : VLAN: ' + formatted_list[0]+ 'MAC: ' + formatted_list[1] + 'Port: ' + formatted_list[6])
            cli ('show tech l2fm detail > bootflash:l2fmt.txt')
            cli ('show tech eltm detail > bootflash:eltm.txt')
        

