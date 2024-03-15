import scanpy as sc

adata = sc.read('./test_6000cell_v4.h5ad')
print(adata.obs)
