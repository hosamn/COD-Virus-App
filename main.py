# import pandas as pd

# df = pd.DataFrame(columns=['name', 'zip', 'Test'])
# print(df)

# data_array = [['a', 34566, 'P'], ['b', 34566, 'N'], ['c', 66666, 'N'], ['d', 65433, 'N'], ['e', 65433, 'P'], ['f', 66666, 'P'], ['g', 34566, 'P'], ['h', 34566, 'P'], ['i', 66666, 'N'], ['j', 66666, 'N'], ['k', 65433, 'N'], ['l', 66666, 'P'], ['z', 11111, 'P']]
data_array = []

while True:

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('COD Virus Tracker\n')
    print('1. Enter Records.')
    print('2. Update Test Results')
    print('3. Run Reports')

    user_inp = input('   Please select an option (Press Enter To Exit): ')

    if   (user_inp == '') or (user_inp not in ['1', '2', '3']): quit()

    elif user_inp == '1':
        dta_in = ['', '', '']
        name_in = input('Enter a name (Press Enter To Exit): ')

        if name_in == '\n': quit()
        else: dta_in[0] = name_in

        while True:
            dta_in[1] = input('Enter a zip code: ')
            if len(dta_in[1]) == 5:
                try:
                    dta_in[1] = int(dta_in[1])
                    break
                except Exception:
                    continue
            print('Input Error, please input zipcode (5 digits)')

        while True:
            try:
                dta_in[2] = input('Enter a test result (P for positive, N for negative, or leave empty): ').upper()
                if dta_in[2] == 'P' or dta_in[2] == 'N' or dta_in[2] == '':
                    break
            except Exception:
                continue
            print('Enter a test result (P, N, or empty): ')

        data_array.append(dta_in)

        print('Data Saved to array!')

    elif user_inp == '2':
        while True:
            srch_str = input('Enter a name to search (Press Enter To Exit): ')

            if   (srch_str == ''): quit()

            elif srch_str in [i[0] for i in data_array]:
                str_pos = [i[0] for i in data_array].index(srch_str)
                print(data_array[str_pos][0])
                print('Current test result: ', data_array[str_pos][2])

                while True:
                    try:
                        new_res = input('Enter a new test result (P, N, or empty): ').upper()
                        if new_res == 'P' or new_res == 'N' or new_res == '':
                            data_array[str_pos][2] = new_res
                            break
                    except Exception:
                        continue

            else:
                print('Name not found!')


    elif user_inp == '3':

        zip_counts = {i[1]: 0 for i in data_array}

        for i in zip_counts:
            pos = len([j[1] for j in data_array if (j[1] == i) and (j[2] == 'P')])
            neg = len([j[1] for j in data_array if (j[1] == i) and (j[2] == 'N')])
            tot = len([j[1] for j in data_array if j[1] == i])
            zip_counts[i] = [pos, neg, tot]

        while True:
            print('1. Display test results by zip code.')
            print('2. Display total test results.')
            report_choice = input('   Please select an option (Press Enter To Exit): ')

            if report_choice == '': quit()

            elif report_choice == '1':
                print('Test results by zip code:\n')
                print('Zip code', 'Positive', 'Negative', 'Percent positive', sep='\t')

                for i in zip_counts:
                    print(i, zip_counts[i][0], zip_counts[i][1], round(100 * zip_counts[i][0] / zip_counts[i][2], 1), sep='\t\t')

            elif report_choice == '2':
                print('Total test results:\n')
                print('Positive', 'Negative', 'Percent positive', sep='\t')

                poses = sum([zip_counts[k][0] for k in zip_counts])
                neges = sum([zip_counts[k][1] for k in zip_counts])
                prcnt = round(100 * poses / (poses + neges), 1)
                print(poses, neges, prcnt, sep='\t\t')


    # print(data_array)
