import MDAnalysis as mda
import MDAnalysis.analysis.pca as pca
from MDAnalysis.tests.datafiles import PSF, DCD

u = mda.Universe(PSF, DCD)
PSF_pca = pca.PCA(u, select='backbone')
PSF_pca.run()

n_pcs = np.where(PSF_pca.cumulated_variance > 0.95)[0][0]
atomgroup = u.select_atoms('backbone')
pca_space = PSF_pca.transform(atomgroup, n_components=n_pcs)

pca = PCA(universe, select='backbone').run()
pca_space =  pca.transform(universe.select_atoms('backbone'), 3)

# for more details please refer to (https://docs.mdanalysis.org/1.0.0/documentation_pages/analysis/pca.html#pca-tutorial)
