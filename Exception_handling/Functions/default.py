# 2. default paramter


def emp_info(emp_name , emp_sal , emp_age , emp_country = 'banglore' ,  ):
    print(emp_name)
    print(emp_sal)    
    print(emp_age) 
    print(emp_country)    

dic = {'employe1' : {'name':'afsan' , 'emp_sal':20 , 'age':24 , 'country':'kerela'},
       'employe2' : {'name':'vineet' , 'emp_sal':20 , 'age':24 , 'country':'delhi'},
       'employe3' : {'name':'xyz' , 'emp_sal':20 , 'age':24 , 'country':''},
       'employe4' : {'name':'abc' , 'emp_sal':20 , 'age':24 , 'country':''},
       'employe5' : {'name':'alok' , 'emp_sal':20 , 'age':24 , 'country':'delhi'},
       'employe6' : {'name':'harish' , 'emp_sal':20 , 'age':24 , 'country':'delhi'},
       'employe7' : {'name':'chandra' , 'emp_sal':20 , 'age':24 , 'country':'kerela'}
      }
 
for i in dic.values(): 
    try:
        emp_info(i['name'] , i['emp_sal'] , i['age'] , i['country'])
    except:
        emp_info(i['name'] , i['emp_sal'] , i['age'] )
        
for i in dic.values(): 
    if i['country']== ''
        emp_info(i['name'] , i['emp_sal'] , i['age'])
    else:
        emp_info(i['name'] , i['emp_sal'] , i['age'] )