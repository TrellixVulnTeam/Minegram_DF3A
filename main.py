import getpass
import login
import extract_users
import bot_comment


stop_minegram = False
stop_login = False
stop_extract = False
stop_config_bot = False
stop_bot = False
print('####################\n'
      '------MINEGRAM------\n'
      '####################\n'
      '--V. PROMPT TEST. --\n')
while not stop_minegram:
    while not stop_login:
        my_user = input('USER: ')
        my_password = getpass.getpass("PASSWORD: ")
        my_login = login.Login(my_user, my_password)
        if my_login.check_login() is True:
            print('Successfully logged!\n')
            stop_login = True
            start_extract = True
        else:
            print('Please, check the informations...\n')

    if start_extract is True:
        while not stop_extract:
            my_extract = extract_users.ExtractUsers(my_login)
            my_account_to_extract = input('Insert a profile for extract followers: ')
            if my_extract.check_profile() is True:
                print('Validated profile!\n'
                      'Start extract followers...\n')
                if my_extract.get_list_of_followers() is True:
                    print('List with {} created!'.format(len(my_extract._list_of_extracted_users)))
                    stop_extract = True
                    config_bot = True
                else:
                    print("This don't working...\n"
                          "Try again...\n")
            else:
                print('Please, check the information or change profile...\n')

    if config_bot is True:
        hard_extract = False
        while not stop_config_bot:
            url = input('Insert the draw URL:  ')
            number_of_users_per_comment = int(input('Insert a number of users per comment (1-3): '))
            if number_of_users_per_comment in (1, 2, 3):
                hard_extract = input("/---------------------------------/\n"
                                     "|Press 'Y' to remove invalid users|\n"
                                     "|---------------------------------|\n"
                                     "|This option remove:              |\n"
                                     "|-Business accounts               |\n"
                                     "|-Famous accounts                 |\n"
                                     "|-Private accounts                |\n"
                                     "|-Accounts with many followers    |\n"
                                     "|----------------------------------\n"
                                     "---> ").upper()
                start_bot = True
                if hard_extract == 'Y':
                    print('Hard extraction enabled!\n')
                    hard_extract = True
                else:
                    print('Hard extraction not enabled!\n')
            else:
                print('Invalid value...\n')

    if start_bot is True:
        errors = 0
        stop_comment = False
        my_bot = bot_comment.BotComment(my_login, url)
        while not stop_bot:
            if my_bot.login_instagram() is True:
                if my_bot.acess_url() is True:
                    while not stop_comment:
                        try:
                            my_bot.comment(my_extract.config_extract(number_of_users_per_comment, hard_extract=hard_extract))
                        except():
                            if my_bot.acess_url() is True:
                                print('Expected error!\n'
                                      'Trying correct...\n')
                                errors += 1
                                if errors == 7:
                                    print('Many errors, please try again later...\n')
                                    stop_bot = True
                            else:
                                stop_comment = True
                else:
                    print('URL not found!')
                    stop_bot = True
                    stop_config_bot = False
            else:
                print('Not working...\n'
                      'Please, try again later...\n')
                stop_bot = True
