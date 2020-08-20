def get_null_productions(grammar):
    null_productions = []

    #It executes twice to make sure null production has been located
    #On the second iteration, it'll use an updated null_productions arrays to produce correct results
    coun=0
    while(coun<2):
        for i in grammar:
            if '$' in i:
                if(i[0] in null_productions):
                    pass
                else:
                    null_productions.append(i[0])

        for k in grammar:
            if('$' in k):
                pass
            else:
                string = []
                
                for letter in k[1:]:
                    if(letter in null_productions):
                        pass
                    elif (len(letter.strip())==0):
                        pass
                    else:
                        string.append(letter)
                        
                

                if (len(string)==1):
                    if(k[0] in null_productions):
                        pass
                    else:
                        null_productions.append(k[0])
        coun += 1
                
            
    return null_productions
    
def remove_null_productions(grammar):
    null_productions = get_null_productions(grammar)
    print("1. Removal of null productions")
    print("\nNull productions: {0}".format(null_productions))
    new_productions = []

    seen = set()
    for rule in grammar:
        if('$' in rule):
            continue
        else:
            new_productions.append(rule.split(" "))

    print("\nProductions before nulls processed")
    for i in new_productions:
        print(i)
        
    for null in null_productions:

        for param in new_productions:
            for i, word in enumerate(param):
                if i < 2:   # don't degenerate LHS
                    continue
                if word == null:
                    temp = param[:i] + param[i+1:]
                    
                    temp_tup = tuple(temp)
                    if len(temp) > 2 and temp_tup not in seen:
                        new_productions.append(temp)
                        seen.add(temp_tup)

    print("\nResultant Productions after nulls have been processed")
    for rule in new_productions:
        print(rule)
    return new_productions

def get_unit_productions(grammar):
    productions = remove_null_productions(grammar)

    unit_productions = []
    temp_productions = []
    print("\n2. Removing Unit productions")
    for rule in productions:
        if(len(rule[2:])==1):
            if(rule[2].isupper()):
                unit_productions.append(rule)
                #print(rule)
        else:
            pass

    for rule in unit_productions:
        for values in unit_productions:
            #print("Rule: {0}, Values: {1}".format(rule[2], values[0]))
            if(rule[2] == values[0]):
                if(rule[0] == values[2]):
                    pass
                else:
                    temp_arr = [rule[0], "=", rule[2], "=", values[2]]
                    temp_productions.append(temp_arr)
                #print(rule[0]+"="+rule[2]+"="+values[2])
    for rule in temp_productions:
        unit_productions.append(rule)

    print("Unit productions")
    for rule in unit_productions:
        print(rule)

    #code area to minimize transitive rules A=>B=>C gives A=>C
    storage = []
    for rule in unit_productions:
        if(len(rule)==5):
            storage.append(rule)

    
    for rule in storage:
        if(rule in unit_productions):
            unit_productions.remove(rule)
            
    for rule in storage:
        if([rule[0], "=", rule[4]] in unit_productions):
            print("Its there")
        else:
            unit_productions.append([rule[0], "=", rule[4]])
    
    #print("Storage")
    #for i in storage:
     #   print(i)

    print("\nUpdated unit productions after minimization of transitive dependencies")
    for rule in unit_productions:
        print(rule)
    return unit_productions, productions

def remove_unit_productions(grammar):
    unit_productions, productions = get_unit_productions(grammar)

    temp_productions = []
    for rule in unit_productions:
        for prod in productions:
            if(rule[2] == prod[0]):
                contains_nt = False
                for val in prod[2:]:
                    if(val.isupper()):
                        contains_nt = True
                    #print("Rule:{0}, Val: {1}".format(rule[2], val))

                if(contains_nt):
                    pass
                else:
                    temp_arr = [rule[0], "="]
                    for val in prod[2:]:
                        temp_arr.append(val)
                    temp_productions.append(temp_arr)
            
                 
    #print("Temp productions: {0}".format(temp_productions))
    for i in unit_productions:
        if(i in productions):
            productions.remove(i)

    for i in temp_productions:
        if(i in productions):
            #print("Its there")
            pass
        else:
            productions.append(i)
    print("\nResultant productions")
    for i in productions:
        print(i)
        
    return productions

def get_mixed_and_long_rules_productions(grammar):
    productions = remove_unit_productions(grammar)
    print("\n3. Separating Terminals from Non-terminal")

    temp_productions = []
    new_temp_productions = []


    for rule in productions:
        contains_non_terminal=False
        contains_terminal=False
        number_terminals = 0
        
        for val in rule[2:]:
            if(val.isupper() and (val.isdigit() == False)):
                contains_non_terminal=True
            else:
                contains_terminal=True
                number_terminals+=1
                
        if(contains_non_terminal and contains_terminal):
            temp_productions.append(rule)
        elif(number_terminals>1):
            temp_productions.append(rule)
            
        
    counter = 1
    storage = []
    for rule in temp_productions:
        #print("Rule in focus: {0}".format(rule))
        temp_arr = [rule[0], "="]
        temp_arr_2 = []
        
        for val in rule[2:]:
            #print("Tem arr 2: {0}".format(temp_arr_2))
            temp_replacer = "C"+str(counter)
            if(val.islower() or val.isdigit()):
                

                found=False
                for temp_rules in storage:
                    #print("Temp rules: {0}".format(temp_rules))
                    if(val in temp_rules):
                        found = True
                        temp_replacer = temp_rules[0]
                        break
                    else:
                        #print("Its not there")
                        pass
                temp_arr.append(temp_replacer)
                
                if(found):
                    if([temp_replacer, "=", val] in storage):
                        pass
                    else:
                        temp_arr_2.append([temp_replacer, "=", val])
                else:
                    temp_arr_2.append([temp_replacer, "=", val])
                    counter+=1
                #temp_arr_2.append(temp_replacer)
                #temp_arr_2.append()
                #temp_arr_2.append(val)
            else:
                temp_arr.append(val)   
            
        
        new_temp_productions.append(temp_arr)
        for num in temp_arr_2:
            new_temp_productions.append(num)
            storage.append(num)
    
    print("\nMixed rules to be separated:")
    for i in temp_productions:
        print(i)
        if(i in productions):
            productions.remove(i)
            
    for rule in new_temp_productions:
        productions.append(rule)
        
    #print("Temp productions: {0}".format(temp_productions))
    print("\nMixed rules after separation")
    for rule in new_temp_productions:
        print(rule)
    
    print("\nResultant productions")
    for i in productions:
        print(i)

    print("\n4. Removal of long rules")
    print("\nRules to be focused")
    temp_productions = []
    new_temp_productions = []

    counter=0
    should_not_repeat = True
    storage = []
    while True:
        print("\nHere")
        should_not_repeat=True
        for rule in productions:
            if(len(rule[2:])>2):
                print(rule)
                temp_productions.append(rule)
                should_not_repeat = False
            
        for num in temp_productions:
            #print(num)
            if(num in productions):
                productions.remove(num)
            
        if(should_not_repeat):
            break
        
        for rule in temp_productions:
            incremeter = "R"+str(counter)
            temp_rule = rule[2:4]
            temp_arr = [rule[0], "=", incremeter]

            rule_appender = [incremeter,"="]
            for val in temp_rule:
                rule_appender.append(val)

            
            rule_exists =False
            for stored_rule in storage:
                #print("Rule app: {0} comparison: {1}".format(rule_appender[2:], stored_rule[2:]))
                if(rule_appender[2:] == stored_rule[2:]):
                    print("You should use: {0} to replace {1}".format(stored_rule, rule_appender))
                    temp_arr[2] = stored_rule[0]
                    rule_appender[0] = stored_rule[0]
                    rule_exists=True
                    break
                else:
                    continue
                
            #append new rule to productions
            if(rule_exists == False):
                new_temp_productions.append(rule_appender)
                storage.append(rule_appender)
                counter+=1
            
            
            for i in rule[4:]:
                #print(i)
                temp_arr.append(i)
            

            #appends old rules with new rules with extracted rules e.g S=>R1 A
            new_temp_productions.append(temp_arr)
            

        print("\nLong rules after removal")
        for rule in new_temp_productions:
            print(rule)
            productions.append(rule)

        temp_productions.clear()
        new_temp_productions.clear()
        
    print("\nTherefore, the chomsky normal form is")
    for i in productions:
        print(i)

    

    
def chomski_size():
    #to handle errors
    try:
        storage = []
        temp_arr = []
        modded_arr=[]
        print("\nNote: For the program to work efficiently, , Non-terminals are uppercase and Terminals are lowercase")
        values = int(input("Enter the number of productions: "))
        print("Enter production in the form of (S=ABC where ABC can be eiter terminals or non-terminals, $ is lambda) with no spaces: ")
        for value in range(0, values):
            string = str(input("{0}: ".format(value+1)))
            temp_arr.append(string)

        #convert input into single elements array
        for k in temp_arr:
            storage.append([ i for i in k])

        print(temp_arr)
        print("\nYou have entered")
        #display output
        for rule in storage:
            modded_arr.append(" ".join(rule))
            print(rule)

        
        print("\n-----------Now Proceding with chomsky")
        get_mixed_and_long_rules_productions(modded_arr)
        
    except ValueError:
        print("Invalid parameters")

chomski_size()
