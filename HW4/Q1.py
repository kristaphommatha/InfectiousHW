import pandas as pd


def I_from_incidence(data_file):
    data = pd.read_csv(data_file)
    incidence = data['New Cases']

    week_count = 1
    infections = []
    curr_incidence = 0
    prev_incidence = [0,0]  # first index is infections from the week before,
                            # second index is infections from two weeks before
    for i in incidence:
        if week_count == 1:
            infection_count = i
            infections.append(infection_count)
            prev_incidence[0] = i

        elif week_count == 2:
            infection_count = infection_count + i
            infections.append(infection_count)
            prev_incidence[1] = prev_incidence[0]
            prev_incidence[0] = i

        else:
            infection_count = infection_count + i - prev_incidence[1]
            infections.append(infection_count)
            prev_incidence[1] = prev_incidence[0]
            prev_incidence[0] = i

        week_count = week_count + 1

    data['I(t)'] = infections
    data.to_excel('data/Q1data.xlsx', index=False)


def main():
    I_from_incidence('data/all_weeks.csv')


if __name__ == '__main__':
    main()
