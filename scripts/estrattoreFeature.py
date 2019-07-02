from tsfresh import extract_relevant_features, extract_features
import utilFeatExtr as util
import pandas as pd

if __name__ == '__main__': 

	# Series ti restituisce anche le classi di appartenenza perché vi servono se volete estrarre
	# le features rilevanti
    listOut,series = util.adaptTimeSeries("C:/Users/Donato/Desktop/UCRArchive_2018/ECG5000/ECG5000_TEST.tsv")
    
    # Questa è la funzione che vi estrae quelle interessanti
    features_filtered_direct = extract_relevant_features(listOut,series, column_id='id', column_sort='time')

    # Questa è la funzione che vi estrae tutte le features
    features_filtered_direct = extract_features(listOut,column_id='id', column_sort='time')
    print(len(features_filtered_direct))
    
    # Questa funzione consente di salvare le features che avete estratto, senza doverle riestrarre di nuovo
    # Occhio all'estensione perché se no jastemmate pur francese, esperienza personale.
    features_filtered_direct.to_pickle("./nomeAPiacere.pkl")

    # Questa funzione invece vi consente di estrarre le features dal pickle creato
    features_filtered_direct = pd.read_pickle("./nomeAPiacere.pkl")