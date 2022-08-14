x = 'Asus Radeon RX 6900 XT ROG Strix Gaming LC Topf HDMI 2xDP 16GB'
split_x = x.split(' ')
y_list = ['Asus Radeon RX 6900 XT ROG Strix Gaming LC Top HDMI 2xDP 16GB', 'Asus Radeon RX 6900 XT ROG Strix Gaming LC OC HDMI 2xDP 16GB', 'Tomtefar Radeon RX 6700 XT Gaming HDMI 2xDP 12GB']
full_hit = len(split_x)
return_list = []
for j in y_list:
    hit_count = 0
    for i in split_x:
        if i in j:
            hit_count += 1
    if hit_count / full_hit < 0.8:
        return_list.append(False)
    else:
        return_list.append(True)
print(return_list)
