import pandas as pd

#prosze zastosowac komende ctrl+alt+l i zwrocic uwage co sie dzieje z linijka ponizej, jezeli nie zauwaza panstwo zmiany, mozna cofnac klikajac cntr+z
d = {'col1': [4,8,13, 7], 'col2': [11, 4, 5, 14]}
df = pd.DataFrame(data=d)

from sklearn.decomposition import PCA

#definiujemy ile komponentow chcemy otrzymac z PCA (ile wyznaczyc wektorow wlasnych, patrz liczenie PCA z zajec nr1, link na wykladzie)
pca = PCA(n_components=1)

X_train = pca.fit_transform(df)


explained_variance = pca.explained_variance_ratio_

#omowic variance