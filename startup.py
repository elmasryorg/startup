#!usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

try:

    print('''

            +=========================+
            |Creator: hemaSayed       |
            |                         |
            |DOC: 11AM 3APR Monday    |
            |                         |
            |Target: Saves time       |
            |                         |
            |OS : Only Linux          |
            +=========================+


    ''');

    print ('\n[ i ] This is the start up program :) I know what you need , Sir');

    print('''\n[ * ] Function : \n[ i ] The Program Starts up lampp , Sublime text , atom , brackets and mysql''')

    if os.path.exists('/opt/lampp') == True:

        os.chdir('/opt/lampp');

        print('\n[ i ] Navigating into lampp folder , Sir');

        print('\n[ i ] Starting Lampp Service\n');

        os.system('sudo ./lampp start');

    else:

        print('\n[ i ] Ignoring lampp starting\n');

    while True:

        b = raw_input('\n[ i ] If you wanna run Sublime just type S , for Brackets type B and for Atom type A\n[ * ] Note That there is no case sens\n[ * ] No or Q = cancel : ')

        if b == 'No' or b == 'no' or b == 'NO' or b == 'nO' or b == 'q' or b == 'Q':

            break;

        elif b == 'b' or b == 'B':

            print('\n[ i ] Starting Brackets');

            os.system('brackets');

            break;

            sys.exit();

        elif b == 's' or b == 'S':

            print('\n[ i ] Starting Sublime Text');

            os.system('sudo subl');

        elif b == 'a' or b == 'A':

            print('\n[ i ] Starting Atom');

            os.system('atom');

        else:

            print('\n[ i ] Sorry It\'s not a valid value');

            break;

            sys.exit();

    while True:

        a = raw_input('\n[ i ] If you wanna run mysql commandline just type Yes [No = cancel] : ')

        if a == 'No' or a == 'no' or a =='NO' or a == 'nO':

            print('\n[ i ] Finished :) have a nice day of programming :D');

            sys.exit();

            break;

        elif a == 'Yes' or a == 'yes' or a == 'YES' or a == 'yEs' or a == 'yeS' or a == 'YeS' or a == 'yES' or a == 'YEs':

            print('\n[ i ] Starting mysql commandline prompt : ');

            os.system('mysql -u root -p');

            break;

        else:

            print('\n[ i ] Sorry It\'s not a valid value');

except KeyboardInterrupt as ki:

    print('\n\n[ * ] Canceled\n');
