from scipy.stats import nbinom
import pandas as pd


def nb_draws(mean, k, num_draws):
    variance = mean + (mean**2)/k
    p = mean/variance
    n = mean**2 / (variance - mean)
    draws = nbinom.rvs(n=n,p=p,size=num_draws)
    #print(draws)
    return sum(draws)


def get_outbreak_cutoff(R0, k, I, thresh):
    variance = R0 + (R0**2)/k
    prob_die = ((R0/(variance**2))**(R0**2/(variance**2-R0)))**I  # prob that all gens give 0 infections and inf dies
    if prob_die < thresh:
        return True
    else:
        return False


def NB_outbreak_sim(R0, I0, k, thresh):
    I = I0
    new_infections = 1
    while new_infections > 0:
        # print(f'k={k}, I={I}')
        new_infections = nb_draws(R0, k, I)
        I = I + new_infections
        infinite = get_outbreak_cutoff(R0, k, I, thresh)
        if infinite is True:
            # print('Outbreak is infinite!')
            return 0
    # print('Outbreak dies')
    return 1


def main():
    k_vals = [0.1,0.5,1,5,10]
    R0 = 3 # Mean R0
    q_vals = []

    thresh = 0.0001
    I0 = 1
    num_trials = 1000

    for k in k_vals:
        trial = 1
        death_counter = 0
        while trial <= num_trials:
            death_counter = death_counter + NB_outbreak_sim(R0, I0, k, thresh)
            trial = trial + 1
        q = death_counter/num_trials
        q_vals.append(q)
    
    results = pd.DataFrame({'k': k_vals, 'q': q_vals})
    # results.to_excel('Q3_res.xlsx',index=False)
    print(results)


if __name__ == '__main__':
    main()
